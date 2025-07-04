# Вариант 5.
Тест бьютификации. Проверка соответствия стилю yapf.

Тест статический анализ кода. Pylint + мой критерий. Проверка на наличие переменных, название которых совпадает с моим именем, т.е. `daniil`.

Интеграционный тест. Проверка на загрузку файла.

SSH доступ в tester контейнер по паролю. Пароль автоматически генерируется при каждом запуске контейнера. В дополнение порт SSH регулируется через .env.

Логи выводятся как в консоль пользователя, так и в docker logs.

Порт сервера приложения app регулируется в .env.

ОЗУ контейнеров ограничено до 150 МБ ввиду варианта 5.

# Инструкция по работе с проектом

## Сборка и запуск контейнеров

```
docker compose up --build
```

## Проведение тестирования

### Запуск всех тестов: бьютификации, статического анализа, интеграционного.

```
docker compose exec tester sh ./run_tests.sh
```

### Запуск теста бьютификации.

```
docker compose exec tester sh ./run_tests.sh beautification
```

### Запуск теста статического анализа.

```
docker compose exec tester sh ./run_tests.sh static
```

### Запуск интеграционного теста.

```
docker compose exec tester sh ./run_tests.sh integration
```

### Замечания:

* **Если Вы введете неверный аргумент, то скрипт подскажет правильный формат.**

* **sh необходим для запуска скриптов, поскольку скрипт неисполняемый по умолчанию.**

* **Тест статического анализа проверяет код на наличие переменной с названием в виде моего имени. Вы можете поменять имя в файлах `static_test.py`, `var_name_checker.py` в переменной `var_for_check`. Эта переменная не была вынесена в `.env`.**

* **Чтобы увидеть отдельно логи tester, можно использовать команду:**
```
docker compose logs tester
```
* **Время логов в UTC0**

## Подключение по SSH к tester

```
ssh root@127.0.0.1 -p 2222
```
Далее введите сгенерированный пароль, который создается при каждом запуске контейнера `tester`. Его можно найти в логах докера, т.е. в консоли, где вы запустили контейнеры по инструкции выше, или с помощью команды (ориентируйтесь на последний пароль):
```
docker compose logs tester
```

### Замечание:

* **Порт SSH определен как 2222 в переменной `SSH_PORT` в `.env`.**
* **Время логов в UTC0**

## Приложение app

Порт работы веб-сервера приложения зависит от переменной `SERVER_PORT` в `.env`. Он определен как 5000. Если с переменной окружения что-то случится, app будет работать на 5000 по умолчанию, как и интеграционный тест будет проводить проверку относительно 5000.
