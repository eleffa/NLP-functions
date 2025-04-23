from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search wikipedia"""
    print(f"searching for name : {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize wikipedia"""
    print(f"Finding wikipedia summary for : {name}")
    return wikipedia.summary(name)


def get_textblob(text):
    """Gets text blob objet and returns"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    "finds wikipedia name and returns back phrases"

    text = summarize_wikipedia(name)
    blob = get_textblob(text)
    phrases = blob.noun_phrases
    # print(phrases)
    return phrases


# golden_state_warriors = wikipedia.summary("Golden State Warriors")
# blob.noun_phrases
