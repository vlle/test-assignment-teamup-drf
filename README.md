## Тестовое для TeamUp

### Как пользоваться:
1) Первый вариант: запустить через ``` docker build -t test-iq-eq . && docker run -p 8000:8000 test-iq-eq  `` 
2) Второй вариант: запустить через ``` poetry install && poetry shell && cd test_iqeq && python manage.py runserver ```

### Что здесь есть:
- Сериалайзеры с валидацией
- Модель TestUser
- Докерфайл для запуска проекта
- pyproject.toml 

### Чего здесь нет (а хотелось бы)
- Документации к функциям на английском
- Чуть более бережного отношения к тестам и pyproject.toml

### Демонстрация запросов

[![asciicast](https://asciinema.org/a/KK34pX13WfU5uwW2yM1IRTK5y.svg)](https://asciinema.org/a/KK34pX13WfU5uwW2yM1IRTK5y)
