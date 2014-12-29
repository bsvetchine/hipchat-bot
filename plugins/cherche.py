# coding: utf-8
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to


class SearchPlugin(WillPlugin):

    @respond_to("cherche (?P<search_query>.*)$")
    def search(self, message, search_query):
        """Use Google Places API to search stuff."""
        data = {
            "query": search_query,
            "key": "AIzaSyCB_F2sXqH-kJ9PWkdQ7xVY90zZR4ppceo"
        }
        r = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
            params=data)
        try:
            results = r.json()
        except TypeError:
            results = []
        self.say(u"%s" % results, message=message)
