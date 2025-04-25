import os
import requests
from logger import logger


def check_integration(url):
    logger.info(f"Проверка загрузки файла по адресу {url}")
    try:
        test_file_path = "testfile.txt"
        test_file_text = "This file is part of integration test."

        with open(test_file_path, "w") as f:
            f.write(test_file_text)
            
        logger.debug(f"Создан файл {test_file_path} для интеграционного тестирования, содержащий следующие данные: {test_file_text}")

        with open(test_file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, files=files)

        os.remove(test_file_path)

        if response.status_code == 200:
            if test_file_path in response.text:
                logger.info(f"Файл {test_file_path} успешно загружен и отображается в списке файлов.")
            else:
                logger.warning(f"Файл {test_file_path} загружен, но не отображается в списке файлов.")
        else:
            logger.error(f"Ошибка при загрузке файла. Статус: {response.status_code}. Ответ: {response.text}")
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    logger.debug("---")
    logger.info("Интеграционный тест (загрузка файла)")
    check_integration(f"http://app:{int(os.environ.get('SERVER_PORT', 5000))}/upload")
    logger.debug("---")