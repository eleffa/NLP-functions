#!/usr/bin/env python3
import fire
from nlplogic.corenlp import get_phrases


if __name__ == "__main__":
    fire.Fire(get_phrases)
