# coding: utf-8
import random
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to


class ImagesPlugin(WillPlugin):

    @respond_to("image (?P<search_query>.*)$")
    def image_search(self, message, search_query):
        """Search image on google images and post a random one."""
        data = {
            "q": search_query,
            "v": "1.0",
            "safe": "active",
            "rsz": "8"
        }
        r = requests.get(
            "http://ajax.googleapis.com/ajax/services/search/images",
            params=data)
        try:
            results = r.json()["responseData"]["results"]
        except TypeError:
            results = []
        if len(results) > 0:
            url = random.choice(results)["unescapedUrl"]
            self.say("%s" % url, message=message)
        else:
            self.say(u"Je n'ai rien trouvé!", message=message)
