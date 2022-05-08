import japanize_kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '200')

class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)

        self.fw = 0
        self.ml = 0
        self.mol = 0
        self.text = ''

    def calculate(self):
        try:
            self.fw = float(self.ids.fw.text)
            self.ml = float(self.ids.ml.text)
            self.mol = float(self.ids.mol.text)
            self.text = str(self.fw * self.mol * self.ml / 1000)
            self.ids.alert.text = '数値を入力してください。'
        except ValueError:
            self.ids.alert.text = '全て半角数字を入力してください！'
    
class MolApp(App):
    def __init__(self, **kwargs):
        super(MolApp, self).__init__(**kwargs)
        self.title = 'Mol Calculator'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    MolApp().run()