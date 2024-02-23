class MainScreenModel:
    def __init__(self):
        self.data = {
            'field-psw': '',
            'enable-uppercase': False,
            'enable-lowercase': False,
            'enable-digits': False,
            'enable-punctuation': False,
            'psw-length': 100
        }

    def set_data(self, key, value):
        self.data[key] = value
