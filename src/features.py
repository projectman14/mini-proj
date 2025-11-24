# src/features.py
import re, nltk
from rapidfuzz.distance import Levenshtein
from nltk.util import ngrams
from .config import FALSE_PHRASES
nltk.download('punkt', quiet=True)

def clean_tokens(text):
    return [t.lower() for t in nltk.word_tokenize(text) if t.isalpha()]

def word_similarity_ratio(query, text):
    q, t = set(clean_tokens(query)), set(clean_tokens(text))
    return len(q & t) / max(1, len(q))

def levenshtein_ratio(query, text):
    a, b = query.lower(), text.lower()
    dist = Levenshtein.distance(a, b)
    return (len(a) + len(b) - dist) / max(1, len(a) + len(b))

def ngram_false_count(text):
    tokens = clean_tokens(text)
    counts = 0
    for n in (1,2,3):
        for g in ngrams(tokens, n):
            phrase = " ".join(g)
            if phrase in FALSE_PHRASES:
                counts += 1
    return counts
