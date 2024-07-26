from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """This app creates a simple type name and greet program"""

    def build(self):
        """Loads the .kv file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """This handles the greet button"""
        print("Greet")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_app(self):
        """This handles the clear button"""
        if self.root.ids.clear_self.on_press:
            self.root.ids.input_name.text = ''
            self.root.ids.output_label.text = "Enter your name "


BoxLayoutDemo().run()
