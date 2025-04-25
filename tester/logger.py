import os
import sys
import logging

class LogLevelFilter(logging.Filter):
    def __init__(self, levels):
        self.levels = levels

    def filter(self, record):
        return record.levelno in self.levels

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# stdout levels: DEBUG, INFO.
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.addFilter(LogLevelFilter([logging.DEBUG, logging.INFO]))
stdout_handler.setFormatter(formatter)

# stderr levels: WARNING, ...
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING)
stderr_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# check fd availability
def open_fd(path):
    try:
        if os.path.exists(path) and os.path.islink(path):
            return open(path, 'w')
    except Exception as e:
        logger.error(f"Не удалось добавить обработчик для docker logs. Ошибка: {e}")
    return None

# loggers for docker logs
docker_stdout = open_fd('/proc/1/fd/1')
if docker_stdout:
    docker_stdout_handler = logging.StreamHandler(docker_stdout)
    docker_stdout_handler.addFilter(LogLevelFilter([logging.DEBUG, logging.INFO]))
    docker_stdout_handler.setFormatter(formatter)
    logger.addHandler(docker_stdout_handler)

docker_stderr = open_fd('/proc/1/fd/2')
if docker_stderr:
    docker_stderr_handler = logging.StreamHandler(docker_stderr)
    docker_stderr_handler.setLevel(logging.WARNING)
    docker_stderr_handler.setFormatter(formatter)
    logger.addHandler(docker_stderr_handler)