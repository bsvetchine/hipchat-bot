# coding: utf-8
import random
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to


class GifPlugin(WillPlugin):

    @respond_to("gif (?P<search_query>.*)$")
    def gif_search(self, message, search_query):
        """Search GIF images using Giphy and post a random one."""
        data = {
            "q": search_query,
            "api_key": "dc6zaTOxFJmzC"
        }
        r = requests.get(
            "http://api.giphy.com/v1/gifs/search",
            params=data)

        try:
            results = r.json()["data"]
        except TypeError:
            results = []
        if len(results) > 0:
            url = random.choice(results)["images"]["fixed_height"]["url"]
            self.say("%s" % url, message=message)
        else:
            self.say(u"Je n'ai rien trouvé!", message=message)
