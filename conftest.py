import pytest
from tests.step_defs.framework.driver import *



caps = {}


# Command line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="To run locally use - 'chrome'. To run on a remote browser use grid_chrome "
    )
    parser.addoption(
        "--env", action="store", default="qa-us",
        help="One of the values: dev, qa-us, qa-ca, qa-uk, stage-us, stage-ca, stage-uk, prod-us, prod-ca, prod-uk"
    )


# BDD step error handling
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    pass


# Report generation hook
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

