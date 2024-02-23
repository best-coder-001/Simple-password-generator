from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from views.screens import screens


class Application(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files('views/')
        self.screen_manager = ScreenManager(transition=FadeTransition(duration=0.1))

    def build(self):
        return self.generate_app_screens()

    def generate_app_screens(self):
        for name in screens.keys():
            model = screens[name]['model']()
            controller = screens[name]['controller'](model)
            view = controller.get_view()
            view.name = name
            view.manager_screens = self.screen_manager
            self.screen_manager.add_widget(view)
        return self.screen_manager


if __name__ == '__main__':
    Application().run()
