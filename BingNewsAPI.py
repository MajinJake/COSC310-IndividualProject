import http.client
import json


class BingNews:
    def headlines(self):
        conn = http.client.HTTPSConnection("bing-news-search1.p.rapidapi.com")

        headers = {
            'X-BingApis-SDK': "true",
            'X-RapidAPI-Host': "bing-news-search1.p.rapidapi.com",
            'X-RapidAPI-Key': "f65b10b085msh0b516a8321d2283p1861aajsn172581f3392f"
        }

        conn.request("GET", "/news/trendingtopics?safeSearch=Off&textFormat=Raw", headers=headers)

        res = conn.getresponse()
        data = res.read()

        rawOutput = data.decode("utf-8")
        json_obj = json.loads(rawOutput)

        # get top 5 headlines
        finalOutput = []

        for i in range(0, 5):
            headLine = json_obj['value'][i]
            finalOutput.append("Headline: " + headLine['query']['text'] + ", Link: " + headLine['newsSearchUrl'])

        return finalOutput
