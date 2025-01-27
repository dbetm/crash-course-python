import justpy as jp


# strings for classes are form the Tailwind framework

@jp.SetRoute("/")
def home():
    wp = jp.WebPage()
    content = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=content, classes="grid grid-cols-3 gap-4 py-4 px-2")
    n1 = jp.Input(a=div1, placeholder="input first value", classes="form-input")
    n2 = jp.Input(a=div1, placeholder="input second value", classes="form-input")
    result_div = jp.Div(a=div1, text="Results will be here...", classes="text-gray-60")
    jp.Div(a=div1, text="Just another div...", classes="text-gray-60")
    jp.Div(a=div1, text="Yet another div...", classes="text-gray-60")

    div2 = jp.Div(a=content, classes="grid grid-cols-2 gap-4")
    jp.Button(
        a=div2,
        text="Calculate",
        click=sum_up,
        classes=(
            "border border-blue-500 m-3 py-1 px-4 rounded text-blue-600"
            " hover:bg-red-500 hover:text-white"
        ),
        number_1=n1,
        number_2=n2,
        result=result_div,
    )
    jp.Div(
        a=div2,
        text="I'm a cool interactive div!",
        mouseenter=mouse_enter,
        mouseleave=mouse_leave,
        classes="hover:bg-red-400"
    )
    
    return wp


@jp.SetRoute("/2")
def home2():
    # Quasar can use Tailwind too, but it adds some additional components that we can use
    wp = jp.QuasarPage(tailwind=True)
    content = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=content, classes="grid grid-cols-3 gap-4 py-4 px-2")
    n1 = jp.Input(a=div1, placeholder="input first value", classes="form-input")
    n2 = jp.Input(a=div1, placeholder="input second value", classes="form-input")
    result_div = jp.Div(a=div1, text="Results will be here...", classes="text-gray-60")
    jp.Div(a=div1, text="Just another div...", classes="text-gray-60")
    jp.Div(a=div1, text="Yet another div...", classes="text-gray-60")

    div2 = jp.Div(a=content, classes="grid grid-cols-2 gap-4")
    jp.QBtn(
        a=div2,
        color="secondary",
        label="Calculate",
        click=sum_up,
        number_1=n1,
        number_2=n2,
        result=result_div,
    )
    jp.Div(
        a=div2,
        text="I'm a cool interactive div!",
        mouseenter=mouse_enter,
        mouseleave=mouse_leave,
        classes="hover:bg-red-400"
    )
    
    return wp


def sum_up(widget, msg):
    result = float(widget.number_1.value) + float(widget.number_2.value)

    widget.result.text = str(result)


def mouse_enter(widget, msg):
    widget.text = "A mouse 🐭 entered the house!!"


def mouse_leave(widget, msg):
    widget.text = "The mouse left the house"

#jp.Route("/", home) # instead use decorator jp.SetRoute

jp.justpy()