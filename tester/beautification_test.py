import os
from yapf.yapflib.yapf_api import FormatFile
from logger import logger


def check_beautification(path):
    logger.info(f"Проверка файлов будет происходить в {path} и во вложенных папках")
    try:
        if os.path.exists(path):
            for root, _, files in os.walk(path):
                if files == []:
                    logger.warning(f"В папке {root} нет файлов")
                    continue
                py_files = [file for file in files if file.endswith('.py')]
                if py_files:
                    for file in py_files:
                        filepath = os.path.join(root, file)
                        _, _, changed = FormatFile(
                            filepath,
                            style_config='yapf',
                            print_diff=True
                        )
                        if changed:
                            logger.error(f"Обнаружены отклонения от стиля yapf в файле {filepath}")
                        else:
                            logger.info(f"Код уже отформатирован по стилю yapf в файле {filepath}")
                else:
                    logger.warning(f'В папке {root} нет файлов .py')
                    continue
        else:
            logger.warning(f'Путь "{path}" не существует.')
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    logger.debug("---")
    logger.info("Проверка соответствия стилю yapf")
    check_beautification("./app")
    logger.debug("---")