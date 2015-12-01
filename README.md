# Midnigth CMS

CMS на django фреймворке для быстрого развертывания web проектов

## Системные требования

* Python 3.4
* Pip
* Bower
* Postgresql 9.3 и выше

## Установка

Прописать настройки соединения с базой данных в файле **midnight/env/dev/settings_local.py**.
Делее выполнить следующие команды в корне проекта:

```
$ cp midnight/env/dev/settings_local.py midnight/settings_local.py

$ pip install -r requirements

$ bower install

$ python manage.py migrate

$ python manage.py loaddata data

$ python manage.py collectstatic
```

## В состав входят следующие модули:

### Главный модуль
Включает в себя следующие компоненты:

* Текстовые страницы
* Меню
* Включаемые области
* Фотогалерея
* Комментарии к страницам

#### Доступные настройки

* MIDNIGHT_MAIN_ADMIN_EMAIL = 'admin@example.com'
* MIDNIGHT_MAIN_MAIL_FROM = 'admin@example.com'
* MIDNIGHT_MAIN_PAGE_TPL_CHOICES = models.Page.PAGE_TPL_CHOICES

#### Доступные теги
Подключение библиотеки тегов

```

{% load midnight_main %}

```

**Подключение меню.** Принимает символьный код меню и атрибуты обертывающего тега.

```

{% show_menu "menu_slug" class='menu-class' %}

```

**Подключение фотогалереи.** Принимает символьный код фотогалереи, размер миниатюр, режим кропа и атрибуты обертывающего тега.

```

{% show_gallery "gallery-slug" "150x110" "center" class='gallery-class' %}

```

**Подключение включаемой области.** Принимает символьный код включаемой области.

```

{% show_area "area_slug" %}

```

**Подключение ajax формы.** Принимает имя класса формы, имя представления обрабатывающего форму, 
идентификатор оборачевающего тега, признак необходимости открывать ворму в fancybox (modal). 
В примере использована форма обратной связи входящая в состав модуля. 

```

{% ajax_form 'midnight_main.forms.Feedback' 'midnight_main:page_feedback' tag_id='feedback_form' modal=True %}

```

**Отображение панели пользователя**.

```

{% user_info %}

```

**Отображение хлебных крошек** Принимает список хлебных крошек и атрибуты оборачивающего тега.

```

{% breadcrumbs crumbs class='breadcrumb' %}

```



### Новости
Позволяет создать новостной раздел с возможностью рубрикации

### Баннерный модуль
Позволяет размещеть баннеры на страницах сайта. Поддерживает следующие форматы:

* JPG
* GIF
* PNG
* SWF

### Каталог
Позволяет организовать каталог товаров с иерархической рубрикацией и настраиваемым набором свойств.