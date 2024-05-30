import pytest
import logging

logging.basicConfig(filename='logs/test_log.log', level=logging.INFO)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = 'report.html'
    config.option.self_contained_html = True
