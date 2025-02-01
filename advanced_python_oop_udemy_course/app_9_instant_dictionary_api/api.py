import json

import justpy as jp

from definition import Definition


definer = Definition("data.csv")


class API:
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get("w")

        response = {
            "word": word,
            "definition": definer.get(word)
        }

        wp.html = json.dumps(response)

        return wp
