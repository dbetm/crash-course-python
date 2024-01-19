import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from filesharer import FileSharer

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.btn_start_camera.text = "Pause camera"
        self.ids.camera.texture = (
            self.ids.camera._camera.texture
        )
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.btn_start_camera.text = "Resume camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        filename = current_time + ".png"
        self.filepath = f"captures/{filename}"
        self.ids.camera.export_to_png(self.filepath)

        self.manager.current = "image_screen"
        # set the capture in the current screen
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    default_link_message = "Create a link first"

    def create_link(self):
        """Access the photo filepath, upload it to the web and display the generated url."""
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath, api_key="")
        self.url = filesharer.share()
        self.ids.img_link.text = self.url

    def copy_link(self):
        """Copy link to the clipboard."""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.img_link.text = self.default_link_message
    
    def open_link(self):
        """Open link with the default web browser."""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.img_link.text = self.default_link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()