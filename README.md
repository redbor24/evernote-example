# Урок **devman** "[Оставляем заметки](https://dvmn.org/modules/novice-code-reading/lesson/evernote-example/)"

Скрипты этого проекта позволяют выполнить базовые действия с блокнотами и заметками [Evernote](http://evernote.com):
- просмотреть список блокнотов пользователя;
- получить список заметок одного блокнота;
- добавить в блокнот заметку, используя другую заметку в качестве шаблона.

## Установка и конфигурация

Библиотека для работы с API Evernote имеет [официальный релиз](https://pypi.org/project/evernote/1.25.3/) 
только для Python 2, поэтому для запуска проекта требуется установка Python версии 2.x 
([Python 2.7](https://www.python.org/download/releases/2.7/)).

### Скачивание проекта с GitHub
Запустите `cmd.exe`

Перейдите в папку, где вы хотите создать проект, например 

`cd X:\MyProjects`, где `X` ваш диск

Выполните 
```
git clone https://github.com/redbor24/evernote-example
cd evernote-example
```

### Создание виртуального окружения
Если у вас на компьютере установлено несколько версий Python, то для запуска проекта вам потребуется создать
виртуальное окружение и указать в нём нужную версию интерпретатора Python. Например, для этого можно
использовать `VirtualEnv`.

```
pip install virtualenv
virtualenv env27 -p <путь к установленному Python27>\python.exe
```
где `env27` наименование виртуального окружения.

#### Активация виртуального окружения
`env27\scripts\activate`

### Установка зависимостей
`pip install -r requirements.txt`

### Конфигурация проекта
Для работы с API Evernote потребуется:
- зарегистрироваться на [dev.evernote.com](https://dev.evernote.com/) для получения `Consumer Secret` и `Developer token`;
- получить [Developer Token для песочницы](https://sandbox.evernote.com/api/DeveloperToken.action).
  
Прописать в файле `.env` следующие ключи:
- `EVERNOTE_CONSUMER_KEY`=Evernote Username, указанное при регистрации;
- `EVERNOTE_CONSUMER_SECRET`=ключ, полученный при регистрации;
- `EVERNOTE_PERSONAL_TOKEN`=Developer Token, полученный при регистрации;

После прохождения регистрации откроется страница с заметкой в единственном блокноте. Из адресной строки браузера
нужно вытащить следующие значения и добавить их в файл `.env`:
- `JOURNAL_NOTEBOOK_GUID`= значение-GUID ключа `b=` 
- `INBOX_NOTEBOOK_GUID`= значение-GUID ключа `b=` 

Для работы с песочницей Evernote укажите в `.env`-файле

`sandbox=True` 

### Использование

#### list_notebooks.py
Выводит в консоль список всех блокнотов пользователя.

`python list_notebooks.py`

#### dump_inbox.py
Выводит в консоль список заметок из одного блокнота.

`python dump_inbox.py`

#### add_note2journal.py
Добавляет в блокнот заметку, используя другую заметку в качестве шаблона.

Создайте заметку с заголовком вида

`Новая заметка {date}, {dow}` 

Добавьте в `.env`-файл ключ:
- `JOURNAL_TEMPLATE_NOTE_GUID`= значение-GUID ключа `n=` из адресной строки браузера этой заметки.

Выполните в консоли команду:

`python add_note2journal.py`

Обновите страницу с заметками в браузере. Первой в списке будет заметка с заголовком, заданным в шаблонной заметке.