import inspect
import justpy as jp


from webapp.about import About # noqa
from webapp.dictionary import Dictionary # noqa
from webapp.home import Home # noqa
from webapp.page import Page

# get global objects and vars in the scope of this module
imports = list(globals().values())

# define routes automatically

for obj in imports:
    if inspect.isclass(obj) and issubclass(obj, Page) and obj is not Page:
        jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)