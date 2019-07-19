import re

import matplotlib.pyplot as plt
import twitter
from wordcloud import WordCloud, STOPWORDS


def get_text(statuses: [twitter]) -> [str]:
    return [status.text for status in statuses]


def generate_wordcloud(data: str) -> None:
    """
    Generates a Word Cloud from the data
    :param data: String
    :return: Word Cloud
    """
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=800, background_color='white',
                          stopwords=stopwords, min_font_size=10).generate(data)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)

    plt.savefig("wordcloud.png")


def list_to_str(statuses: [str]):
    """
    From a list of strings, return a
    combined string of
    all items in list
    :param statuses: list of strings
    :return: string
    """
    words = " ".join(statuses)
    # Remove user mentions
    words = re.sub("@\w+", "", words)
    # Remove URLs
    words = re.sub(r"(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b", "", words)
    return words
