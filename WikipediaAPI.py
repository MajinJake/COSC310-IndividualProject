import wikipedia as wikipedia


class wikipediaAPI:
    def wikiPage(topic):
        wikiPage = wikipedia.page(topic)

        output = wikiPage.title + "\n" + wikiPage.url + "\n" + "\n" + wikiPage.summary
        return output