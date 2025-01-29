import justpy as jp

from definition import definer
from webapp.layout import DefaultLayout
from webapp.page import Page


class Dictionary(Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)

        layout = DefaultLayout(a=wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=layout)
        content = jp.Div(a=container, classes="bg-gray-200 h-screen")

        jp.Div(a=content, text="Instant English dictionary!", classes="text-4xl m-2")
        jp.Div(
            a=content,
            text="Get the definition of any English word instantly as you type.",
            classes="text-lg"
        )
        input_row = jp.Div(a=content, classes="grid grid-cols-1")
        result_div = jp.Div(a=content, classes="m-2 p-2 text-lg border-2 border-green-400 h-40")
        
        input_box = jp.Input(
            a=input_row,
            placeholder="Type in a word here...",
            classes=(
                "m-2 py-2 px-4 bg-gray-100 border-2 border-gray-200 rounded w-64"
                " focus:outline-none focus:border-purple-500 focus:bg-white"
            ),
            result_div=result_div
        )

        input_box.on("input", cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        definition_:tuple = definer.get(widget.value)
        widget.result_div.text = "\n".join(definition_)
        # widget.input_box.value = ""
