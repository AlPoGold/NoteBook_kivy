from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

import controller.commands

store = JsonStore('notebook.json')


class MainWindow(Screen):
    pass


class MenuWindow(Screen):
    pass
class AddWindow(Screen):
    def press_title(self):
        title = self.ids.note_title_input.text

    def press_body(self):
        text = self.ids.note_body_input.text
class ShowWindow(Screen):
    note_text = StringProperty(controller.commands.show_notes())
    # def __init__(self, note_text_prop=None, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.note_text = note_text_prop


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("notebook.kv")


class NoteBookApp(App):
    text_notes = controller.commands.show_notes()
    def close_application(self):
        App.get_running_app().stop()
        Window.close()
    def open_file(instance):
        controller.commands.open_file()

    def build(self):
        return kv


if __name__ == "__main__":
    NoteBookApp().run()

