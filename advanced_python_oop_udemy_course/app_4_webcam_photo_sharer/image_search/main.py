from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests


Builder.load_file("frontent.kv")


class FirstScreen(Screen):
    def __get_image_link(self, query: str) -> str:
        print("query", query)
        page = wikipedia.page(query)

        return page.images[0]

    def __download_image(self, image_link: str) -> str:
        image_path = "files/image.jpg"

        req = requests.get(
            image_link,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
            }
        )

        with open(image_path, "wb") as file:
            file.write(req.content)

        return image_path

    def search_image(self):
        image_link = self.__get_image_link(
            self.manager.current_screen.ids.user_query.text
        )

        self.manager.current_screen.ids.img.source = self.__download_image(image_link)


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()