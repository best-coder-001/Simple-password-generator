from views import MainScreenView
from utils.tools import generate_random_string
from kivy.logger import Logger
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar.snackbar import (
    MDSnackbarText,
    MDSnackbar
)

from string import (
    digits,
    ascii_uppercase,
    ascii_lowercase,
    punctuation
)


class MainScreenController:
    def __init__(self, model):
        self.model = model
        self.view = MainScreenView(model=model, controller=self)

    def get_view(self) -> MainScreenView:
        return self.view

    def set_data(self, key, value):
        self.model.set_data(key, value)

    def generate_password(self):
        alphabet = ''
        try:
            if self.model.data['enable-uppercase']:
                alphabet += ascii_uppercase

            if self.model.data['enable-lowercase']:
                alphabet += ascii_lowercase

            if self.model.data['enable-digits']:
                alphabet += digits

            if self.model.data['enable-punctuation']:
                alphabet += punctuation + ' '

            if not self.model.data['psw-length']:
                ...

            psw_len = int(self.model.data['psw-length'])
            generated_password = generate_random_string(psw_len, alphabet)

        except Exception as ex:
            Logger.info(ex)
        else:
            self.model.set_data('field-psw', generated_password)
            self.view.ids.field_psw.text = generated_password
            self.view.ids.field_psw.cursor = (0, 0)
            Logger.info(f'PASSWORD GENERATED SUCCESSFULLY: {generated_password}')

    def on_copy_text_btn(self):
        Clipboard.copy(self.model.data['field-psw'])
        MDSnackbar(
            MDSnackbarText(
                text="Text copied",
                pos_hint={"center_x": 0.5},
            ),
            y=24,
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()
