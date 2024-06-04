import requests
from sys import argv

API_KEY = 'bce6ae7a0e9f4ded9bbd15f195f49229'

URL = ('https://newsapi.org/v2/top-headlines?')


def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)


def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)


def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(results['title'])
        print(result['url'])
        print('')


def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apikey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])


if __name__ == "__main__":
    print(f"Getting news for {argv[1]}...\n")
    get_artciles_by_category(argv[1])
    print(f"Successfully retrieved top {argv[1]} headlines")
    # get_artciles_by_query("Elon Musk"))
    #print_sources_by_category("technology")
