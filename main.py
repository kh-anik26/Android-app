from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
import time

class MainApp(App):
    def build(self):
        self.title = "My Kivy Android App"
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title
        title = Label(
            text='Welcome to My Android App!',
            font_size='24sp',
            size_hint_y=None,
            height='60dp',
            color=(0.2, 0.6, 1, 1)
        )
        
        # Input section
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp')
        self.text_input = TextInput(
            hint_text='Enter your message here...',
            multiline=False,
            size_hint_x=0.7
        )
        
        submit_btn = Button(
            text='Submit',
            size_hint_x=0.3,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        submit_btn.bind(on_press=self.on_submit)
        
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(submit_btn)
        
        # Display area
        self.display_label = Label(
            text='Your messages will appear here...',
            text_size=(None, None),
            halign='center',
            valign='middle',
            font_size='16sp'
        )
        
        # Buttons section
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', spacing=10)
        
        time_btn = Button(
            text='Show Time',
            background_color=(0.8, 0.4, 0.8, 1)
        )
        time_btn.bind(on_press=self.show_time)
        
        clear_btn = Button(
            text='Clear',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        clear_btn.bind(on_press=self.clear_display)
        
        info_btn = Button(
            text='App Info',
            background_color=(0.2, 0.6, 0.8, 1)
        )
        info_btn.bind(on_press=self.show_info)
        
        button_layout.add_widget(time_btn)
        button_layout.add_widget(clear_btn)
        button_layout.add_widget(info_btn)
        
        # Add all widgets to main layout
        main_layout.add_widget(title)
        main_layout.add_widget(input_layout)
        main_layout.add_widget(self.display_label)
        main_layout.add_widget(button_layout)
        
        return main_layout
    
    def on_submit(self, instance):
        user_text = self.text_input.text.strip()
        if user_text:
            current_time = time.strftime("%H:%M:%S")
            self.display_label.text = f"[{current_time}] You said: {user_text}"
            self.text_input.text = ""
        else:
            self.show_popup("Warning", "Please enter some text!")
    
    def show_time(self, instance):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.display_label.text = f"Current time: {current_time}"
    
    def clear_display(self, instance):
        self.display_label.text = "Display cleared!"
        self.text_input.text = ""
    
    def show_info(self, instance):
        info_text = """
        My Kivy Android App
        Version: 1.0
        
        Features:
        • Text input and display
        • Time display
        • Simple UI interactions
        
        Built with Kivy Python
        """
        self.show_popup("App Information", info_text)
    
    def show_popup(self, title, content):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        popup_label = Label(
            text=content,
            text_size=(300, None),
            halign='center',
            valign='middle'
        )
        
        close_btn = Button(
            text='Close',
            size_hint_y=None,
            height='40dp',
            background_color=(0.6, 0.6, 0.6, 1)
        )
        
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_btn)
        
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.8, 0.6),
            auto_dismiss=False
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    MainApp().run()