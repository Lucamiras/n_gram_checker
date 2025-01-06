from nltk.corpus import stopwords
import string
from collections import Counter
from nltk import ngrams
from nltk.tokenize import word_tokenize
import re


def generate_ngrams(text, n):
    """Generates n-grams from a given text."""
    stop = stopwords.words("english")
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    tokens_without_stopwords = [t for t in tokens if t not in stop]
    cleaned_tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens_without_stopwords if re.sub(r'[^\w\s]', '', token)]
    n_grams = ngrams(cleaned_tokens, n)
    return Counter(n_grams).most_common(10)  # Limit to top 10 ngrams