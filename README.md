# Сайт спортивного клуба "Ариадна"

Реализация новой версии сайта http://ariadna.tpu.ru.
2020 год.

## Roadmap / Планы

- в 1
    - на движок Джанго натягиваем шаблон Олега
    - обновляем Джанго
    - выкатываем вместо текущего сайта

- далее...
    - заменяем шаблоны Джанго на JS приложение.
    - пилим Приложения из списка ниже.

## Приложения

### Мероприятия
- создание событий
- синхронизация с событиями из ВК группы

### Материалы
- размещаем ссылки на внешние источники с возможностью комментирования
- сохраняем копию материала (текст и скриншот), вдруг потеряется
- показываем авторизованным материал, как есть, чтобы читать у нас на сайте

### Фотографии
- прикручиваем хранилище из Облака

### Обратная связь
- форма для общения с незарегистрированными


---

## Run locally
```shell script
$ cd <PROJECT FOLDER>

$ django-admin runserver --settings=app.config.settings.local --pythonpath=<PROJECT FOLDER/app>
```

```shell script
export PYTHONPATH=${PYTHONPATH}:${PWD}
```
