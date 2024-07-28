from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """This app dynamically creates box layouts for labels within the self.names list"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.labels = ["Albert", "James", "Requilme", "Is the Author", "Of this Program"]

    def build(self):
        """This builds the widget and displays every label using a for loop"""
        self.root = Builder.load_file('dynamic_labels.kv')
        for label in self.labels:
            self.root.ids.names_layout.add_widget(Label(text=label))
        return self.root


DynamicLabelsApp().run()
