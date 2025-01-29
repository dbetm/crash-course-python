import justpy as jp

from webapp.layout import DefaultLayout
from webapp.page import Page


class Home(Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = DefaultLayout(a=wp, view="hHh lpR fFf")

        container = jp.QPageContainer(a=layout)
        content = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")

        jp.Div(a=content, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(
            a=content,
            text="""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ornare ut velit nec 
                tristique. Cras vel accumsan lorem. Vestibulum efficitur varius volutpat. Maecenas 
                mattis eros justo, at fermentum est hendrerit in. Quisque pharetra rutrum condimentum.
                Pellentesque suscipit orci venenatis magna dapibus eleifend. Donec dignissim metus id
                semper pretium. Donec ut quam a ipsum dignissim accumsan a vestibulum dui. Pellentesque
                laoreet odio quis dapibus dictum. Aliquam eu elit pulvinar, molestie sapien vel, facilisis
                lacus. Sed vehicula pretium nisi rutrum lobortis. Vivamus consectetur odio non enim pharetra
                interdum. Ut tincidunt sapien ac metus dignissim, vel feugiat quam consequat. Donec in tortor
                ante. Quisque gravida dolor sapien, sed imperdiet elit tempor id. Praesent dignissim pulvinar
                ipsum, eget semper leo feugiat sed.
            """,
            classes="text-lg"
        )

        return wp
