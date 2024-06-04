# news_automator.py

Overview

The News Article Fetcher is a Python script that uses the NewsAPI to retrieve top news headlines based on specified categories or search queries. The script allows users to specify a news category as a command-line argument to fetch relevant articles. It can also fetch articles based on a specific query and retrieve news sources by category.

Features

Fetch Articles by Category: Retrieves top news headlines for a specified category.
Fetch Articles by Query: Retrieves top news headlines based on a specific search query.
Fetch News Sources by Category: Lists news sources for a specified category.

Components

get_articles_by_category(category):
Constructs query parameters using the provided category.
Fetches articles using the NewsAPI and prints the titles and URLs of the articles.

get_articles_by_query(query):
Constructs query parameters using the provided query string.
Fetches articles using the NewsAPI and prints the titles and URLs of the articles.

get_sources_by_category(category):
Constructs query parameters to get news sources for a specific category.
Fetches sources using the NewsAPI and prints the names and URLs of the sources.

_get_articles(params):
A helper function used by get_articles_by_category and get_articles_by_query.
Makes the API request and processes the response to extract and print article titles and URLs.

Command-line Interface:
Allows users to specify the news category directly when running the script.
Provides error handling for cases when no arguments are provided.
