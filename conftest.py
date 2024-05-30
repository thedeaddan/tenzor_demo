import pytest
from utils.logger import setup_logger

logger = setup_logger(__name__)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Инициализация логгера и конфигурация
    logger.info('Starting test session')

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    # Логгирование завершения тестов и их статуса
    logger.info('Tests finished with status: %s', exitstatus)
