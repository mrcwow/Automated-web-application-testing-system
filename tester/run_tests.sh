#!/bin/bash

run_beautification_test() {
    echo "---"
    echo "Запускаем тест бьютификации"
    echo "---"
    python3 beautification_test.py
}

run_static_test() {
    echo "---"
    echo "Запускаем тест статического анализа"
    echo "---"
    python3 static_test.py
}

run_integration_test() {
    echo "---"
    echo "Запускаем интеграционный тест"
    echo "---"
    python3 integration_test.py
}

echo "---"
echo "Запускаем тестирование"

if [ $# -eq 0 ]; then
    run_beautification_test
    run_static_test
    run_integration_test
else
    case "$1" in
        beautification)
            run_beautification_test
            ;;
        static)
            run_static_test
            ;;
        integration)
            run_integration_test
            ;;
        *)
            echo "Неизвестный аргумент: $1"
            echo "Правильный запуск: sh $0 [ |beautification|static|integration]"
            ;;
    esac
fi