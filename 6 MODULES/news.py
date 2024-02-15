"""
A small Python module for retrieving the latest news.
"""
import http.client
import xml.etree.ElementTree


def get_news_from_cnn() -> list[str]:
    """
    Get the latest news from CNN.
    :return: Trending headlines from CNN.
    """
    host = "rss.cnn.com"
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/rss/cnn_latest.rss")
    response = conn.getresponse().read()
    root = xml.etree.ElementTree.fromstring(response)
    items = root.find('channel').findall('item')
    return [item.find('title').text for item in items]


# Just for demonstration purposes
print("Python module 'news' loaded!")

# Print the news if the module is executed directly
if __name__ == "__main__":
    print("\n".join(get_news_from_cnn()))
