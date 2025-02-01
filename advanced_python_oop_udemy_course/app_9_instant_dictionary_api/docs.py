import justpy as jp



class Doc():
    path = "/docs"

    @classmethod
    def serve(cls):
        wp = jp.WebPage()
        content = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=content, text="Instant dictionary API", classes="text-4xl m-2")
        jp.Div(a=content, text="Get definitions of words:", classes="text-lg")
        jp.Hr(a=content)
        jp.Div(a=content, text="www.example.com?w=sun")
        jp.Hr(a=content)

        jp.Div(
            a=content,
            text="""
                {
                    "word": "sun",
                    "definition": [
                        "Any star, especially when seen as the centre of any single solar system.",
                        "The particular star at the centre of our solar system, from which the Earth gets light and heat."
                    ]
                }
            """,
        )

        return wp