## Тестовое для TeamUp

### Как пользоваться:
1) Первый вариант: запустить через ```docker build -t test-iq-eq . && docker run -p 8000:8000 test-iq-eq```
2) Второй вариант: запустить через ```poetry install && poetry shell && cd test_iqeq && python manage.py runserver```

### Что здесь есть:
- Сериалайзеры с валидацией
- Модель TestUser
- Докерфайл для запуска проекта
- pyproject.toml 

### Чего здесь нет (а хотелось бы)
- Документации к функциям на английском
- Чуть более бережного отношения к тестам и pyproject.toml
- Хорошей истории коммитов (писал локально)

### Примеры запросов
```http GET 'http://127.0.0.1:8000/api/get_test_res?login=ooykbilkja'```


```http POST 'http://127.0.0.1:8000/api/fill_eq' eq=аббаб login=ooykbilkja```


```http POST 'http://127.0.0.1:8000/api/fill_iq' iq=40 login=ooykbilkja```


```http POST 'http://127.0.0.1:8000/api/create_user'```

### Демонстрация 

[![asciicast](https://asciinema.org/a/KK34pX13WfU5uwW2yM1IRTK5y.svg)](https://asciinema.org/a/KK34pX13WfU5uwW2yM1IRTK5y)

