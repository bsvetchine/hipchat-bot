# coding: utf-8
import requests

from will.plugin import WillPlugin
from will.decorators import respond_to

from .. import app_settings


class SearchPlugin(WillPlugin):

    @respond_to("cherche (?P<search_query>.*)$")
    def search(self, message, search_query):
        """Use Google Places API to search stuff."""
        data = {
            "query": search_query,
            "key": app_settings.GOOGLE_MAPS_API_KEY
        }
        r = requests.get(
            "https://maps.googleapis.com/maps/api/place/textsearch/json",
            params=data)
        try:
            results = r.json()["results"]
        except TypeError:
            results = []
        # construct search text response
        help_text = ""
        for result in results[0:10]:
            help_text += "<b>{name}</b>: {address}</br>".format(
                name=result["name"],
                address=result["formatted_address"])
        self.say(help_text, message=message, html=True)
