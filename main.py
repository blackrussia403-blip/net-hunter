from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import requests

Window.clearcolor = (0, 0, 0, 1)

class NetHunterUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=25, spacing=15, **kwargs)
        self.add_widget(Label(text='[ NET-HUNTER ]\nGOD-MODE V2.1', font_size='32sp', color=(1, 0, 0, 1), bold=True, halign='center'))
        self.console = TextInput(text='> SYSTEM: ONLINE\n> STATUS: READY', readonly=True, background_color=(0, 0.05, 0, 1), foreground_color=(0, 1, 0, 1), font_size='16sp', size_hint_y=0.7)
        self.add_widget(self.console)
        btns = BoxLayout(size_hint_y=0.2, spacing=10)
        self.scan_btn = Button(text='SCAN IP', background_color=(0.7, 0, 0, 1), color=(1, 1, 1, 1), bold=True)
        self.scan_btn.bind(on_press=self.get_net_data)
        self.clear_btn = Button(text='CLEAR', background_color=(0.2, 0.2, 0.2, 1), color=(1, 1, 1, 1), bold=True)
        self.clear_btn.bind(on_press=self.clear_scr)
        btns.add_widget(self.scan_btn)
        btns.add_widget(self.clear_btn)
        self.add_widget(btns)

    def clear_scr(self, instance): self.console.text = "> LOGS CLEARED\n> STATUS: READY"

    def get_net_data(self, instance):
        self.console.text += "\n> INITIALIZING OSINT..."
        try:
            r = requests.get('https://ipify.org', timeout=10).json()
            self.console.text += f"\n> TARGET IP: {r.get('ip')}\n> STATUS: SUCCESSFUL"
        except: self.console.text += "\n> ERROR: CONNECTION FAILED"

class NetHunterApp(App):
    def build(self): return NetHunterUI()

if __name__ == '__main__': NetHunterApp().run()
