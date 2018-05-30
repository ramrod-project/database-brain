
from os import environ
from .brain.environment import check_log_env, check_stage_env, check_dev_env, check_prod_env, log_env_gte

def test_default_loglevel():
    if "LOGLEVEL" in environ:
        del(environ['LOGLEVEL'])
    assert check_log_env() == "TEST"

def test_emergency_loglevel():
    environ['LOGLEVEL'] = "EMERGENCY"
    assert log_env_gte("EMERGENCY")
    assert not log_env_gte("TEST")

def test_warning_loglevel():
    environ['LOGLEVEL'] = "WARNING"
    assert log_env_gte("WARNING")
    assert not log_env_gte("TEST")

def test_debug_loglevel():
    environ['LOGLEVEL'] = "DEBUG"
    assert log_env_gte("WARNING")
    assert log_env_gte("DEBUG")
    assert not log_env_gte("TEST")

def test_test_loglevel():
    environ['LOGLEVEL'] = "TEST"
    assert log_env_gte("WARNING")
    assert log_env_gte("DEBUG")
    assert log_env_gte("TEST")

def test_stage_env():
    if "STAGE" in environ:
        del(environ['STAGE'])
    assert check_stage_env() == "TESTING"

def test_dev_env():
    if "STAGE" in environ:
        del (environ['STAGE'])
    assert check_dev_env()


def test_not_dev_env():
    if "STAGE" in environ:
        del (environ['STAGE'])
    assert not check_prod_env()

def test_set_bad_stage():
    environ['STAGE'] = "PRODUCTION"
    assert not check_prod_env()

def test_set_bad_stage():
    environ['STAGE'] = "DEV"
    assert check_dev_env()
