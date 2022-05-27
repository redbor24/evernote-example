from decouple import config


class Settings:
    def __init__(self):
        pass

    EVERNOTE_CONSUMER_KEY = config('EVERNOTE_CONSUMER_KEY', '')
    EVERNOTE_CONSUMER_SECRET = config('EVERNOTE_CONSUMER_SECRET', '')
    EVERNOTE_PERSONAL_TOKEN = config('EVERNOTE_PERSONAL_TOKEN', '')

    JOURNAL_TEMPLATE_NOTE_GUID = config('JOURNAL_TEMPLATE_NOTE_GUID', '')
    JOURNAL_NOTEBOOK_GUID = config('JOURNAL_NOTEBOOK_GUID', '')

    INBOX_NOTEBOOK_GUID = config('INBOX_NOTEBOOK_GUID', '')
    sandbox = True if config('sandbox', True) in ['True', '1'] else False
