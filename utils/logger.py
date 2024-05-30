import logging

def setup_logger(name):
    """
    Настраивает и возвращает логгер с указанным именем.

    :param name: Имя логгера
    :return: Конфигурированный логгер
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Установить уровень логирования

    # Настроить обработчик для вывода логов в консоль
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # Установить уровень для обработчика

    # Настроить формат логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Добавить обработчик к логгеру
    logger.addHandler(ch)
    return logger
