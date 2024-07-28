from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKmApp(App):
    """This app converts miles to kilometers"""

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """This method will calculate miles by 1.6"""
        try:
            result = float(value) * 1.609344
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, increment):
        """handles the up/down buttons, incrementing either by 1 or -1"""
        try:
            result = int(self.root.ids.input_number.text) + increment
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.input_number.text = '0'


ConvertMilesToKmApp().run()
