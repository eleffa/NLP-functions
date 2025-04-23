from nlplogic.corenlp import get_phrases #,search_wikipedia, summarize_wikipedia, get_textblob


def test_get_phrase():
    assert "golden state" in get_phrases("Golden State Warriors")
