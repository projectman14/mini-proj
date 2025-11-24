# src/query_builder.py
import re, nltk
from nltk.corpus import stopwords
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
STOP = set(stopwords.words('english'))

def build_query(text: str, max_words: int = 20) -> str:
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [re.sub(r'\W+', '', t) for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t and t not in STOP]
    return " ".join(tokens[:max_words])
