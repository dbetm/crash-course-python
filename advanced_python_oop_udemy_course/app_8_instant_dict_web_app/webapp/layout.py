import justpy as jp


class DefaultLayout(jp.QLayout):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # code for layout was inspired in HTML code generated at: https://quasar.dev/layout-builder/
        # layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=self, elevated=True, classes="bg-primary text-white")
        toolbar = jp.QBtn(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", side="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller, classes="p-2")
        menu_item_classes = "p-2 m-2 text-lg text-blue-600 hover:text-blue-400"

        jp.A(a=qlist, text="Home", href="/", classes=menu_item_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=menu_item_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=menu_item_classes)
        jp.Br(a=qlist)

        jp.QButton(
            a=toolbar,
            dense=True,
            flat=True,
            round=True,
            icon="menu",
            click=self.toggle_drawer,
            drawer=drawer,
        )
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def toggle_drawer(widget, msg):
        widget.drawer.value = False if widget.drawer.value else True