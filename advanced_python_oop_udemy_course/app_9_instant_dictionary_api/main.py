import justpy as jp


from api import API
from docs import Doc



jp.Route("/", API.serve)
jp.Route(Doc.path, Doc.serve)

jp.justpy()