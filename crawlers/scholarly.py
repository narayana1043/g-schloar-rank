from fp.fp import FreeProxy
from scholarly import scholarly


class Scholarly:

    def __init__(self):
        proxy = FreeProxy(rand=True, timeout=1, country_id=['US', 'CA']).get()
        scholarly.use_proxy(http=proxy, https=proxy)

    def get_author_details(self, name):
        """

        :return:
        """
        author = next(scholarly.search_author(name))
        return author

    def get_author_publications(self, id):
        pass