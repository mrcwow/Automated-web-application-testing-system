import os
import subprocess
from logger import logger


var_for_check = "daniil"
plugin_dir="."


def check_static(path):
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
                        result = subprocess.run(
                            [
                                "pylint",
                                "--score=no",
                                "--load-plugins=var_name_checker",
                                "--disable=all",
                                f"--enable=var-{var_for_check}-found",
                                f"{filepath}"
                            ],
                            capture_output=True,
                            text=True,
                            env={**os.environ, "PYTHONPATH": plugin_dir}
                        )

                        if f"var-{var_for_check}-found" in result.stdout:
                            logger.error(result.stdout.strip())
                        else:
                            logger.info(f"Переменная {var_for_check} не найдена в {filepath}")

                        if result.stderr.strip():
                            logger.error(result.stderr.strip())
                else:
                    logger.warning(f'В папке {root} нет файлов .py')
                    continue
        else:
            logger.warning(f'Путь "{path}" не существует.')
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    logger.debug("---")
    logger.info("Статический анализ кода (pylint + свой критерий)")
    check_static("./app")
    logger.debug("---")