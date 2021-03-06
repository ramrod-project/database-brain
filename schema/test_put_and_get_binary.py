"""
test CRUD ops

put, list_dir, get, delete

"""
from os import environ
from dict_to_protobuf import protobuf_to_dict
from pytest import fixture, raises
import docker
from time import time

from .brain import connect, r
from .brain.binary.data import put, get, list_dir, delete, put_buffer
from .brain.queries import RBF
from .brain.brain_pb2 import Binary


CLIENT = docker.from_env()
TEST_FILE_NAME = "TEST_FILE.txt"
BIG_TEST_FILE_NAME = "BIG_TEST_FILE.txt"
TEST_FILE_CONTENT = "content data is binary 灯火 标 and string stuff ".encode('utf-8')
TEST_TEXT_NAME = "TEST_TEXT.txt"
TEST_TEXT_CONTENT = "standard text stuff"


@fixture(scope='module')
def rethink():
    tag = environ.get("TRAVIS_BRANCH", "dev").replace("master", "latest")
    container_name = "brainmoduletestCRUD"
    CLIENT.containers.run(
        "ramrodpcp/database-brain:{}".format(tag),
        name=container_name,
        detach=True,
        ports={"28015/tcp": 28015},
        remove=True
    )
    yield True
    # Teardown for module tests
    containers = CLIENT.containers.list()
    for container in containers:
        if container.name == container_name:
            container.stop()
            break


def test_ensure_files_table_exists(rethink):
    try:
        r.db("Brain").table_create("Files").run(connect())
    except r.ReqlOpFailedError:
        pass  # table may already exist and that's ok
    RBF.run(connect())  # test it can pull a cursor


def test_put_binary(rethink):
    bin_obj = Binary()
    bin_obj.Name = TEST_FILE_NAME
    bin_obj.Content = TEST_FILE_CONTENT
    obj_dict = protobuf_to_dict(bin_obj)
    put(obj_dict)
    assert TEST_FILE_NAME in list_dir()


def test_put_binary_again(rethink):
    assert TEST_FILE_NAME in list_dir()
    response = put_buffer(TEST_FILE_NAME, TEST_FILE_CONTENT)
    assert response['errors'] == 1


def test_obj_in_listing(rethink):
    assert TEST_FILE_NAME in list_dir()


def test_get_file(rethink):
    assert get(TEST_FILE_NAME)['Content'] == TEST_FILE_CONTENT


def test_remove_file(rethink):
    assert TEST_FILE_NAME in list_dir()
    assert delete(TEST_FILE_NAME)
    assert TEST_FILE_NAME not in list_dir()


def test_remove_non_existant_file(rethink):
    assert TEST_FILE_NAME not in list_dir()
    assert delete(TEST_FILE_NAME)


def test_verify_put_command(rethink):
    bin_obj = Binary()
    bin_obj.Name = TEST_FILE_NAME
    bin_obj.Content = TEST_FILE_CONTENT
    obj_dict = protobuf_to_dict(bin_obj)
    put(obj_dict, verify=True)


def test_huge_insert_split(rethink):
    """
    134217727 is the biggest query size
    make an object bigger than that
    add the overhead of the other query params, should be over
    :param rethink:
    :return:
    """
    big_content = ("a"*134217727).encode("utf-8")
    bin_obj = Binary()
    bin_obj.Name = BIG_TEST_FILE_NAME
    bin_obj.Content = TEST_FILE_CONTENT
    bin_obj.Timestamp = time()
    obj_dict = protobuf_to_dict(bin_obj)
    obj_dict["Content"] = big_content
    resp = put(obj_dict)
    assert resp["inserted"] == 3

def test_huge_insert_again(rethink):
    assert BIG_TEST_FILE_NAME in list_dir()
    post_count = RBF.count().run(connect())
    big_content = ("a" * 134217727).encode("utf-8")
    response = put_buffer(BIG_TEST_FILE_NAME, big_content)
    post_count_after = RBF.count().run(connect())
    assert post_count_after == post_count
    assert response['errors'] == 1


def test_list_dir_large_files(rethink):
    the_dir = list_dir()
    assert BIG_TEST_FILE_NAME in the_dir
    assert BIG_TEST_FILE_NAME + "001" not in the_dir


def test_huge_split_read(rethink):
    assert get(BIG_TEST_FILE_NAME)["Content"] == ("a"*134217727).encode("utf-8")


def test_delete_split(rethink):
    pre_count = RBF.count().run(connect())
    assert delete(BIG_TEST_FILE_NAME)
    assert BIG_TEST_FILE_NAME not in list_dir()
    post_count = RBF.count().run(connect())
    assert pre_count - post_count == 3


def test_put_text_file(rethink):
    basic_put_object = {"Name": TEST_TEXT_NAME,
                        "Content": TEST_TEXT_CONTENT}
    put(basic_put_object)
    assert get(TEST_TEXT_NAME)["Content"] == TEST_TEXT_CONTENT
