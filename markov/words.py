import re
from collections import defaultdict

from . import gram_utils
from .text import normalize_text, END_OF_TEXT


def count_ngrams(text, n=3):
    n = n + 1
    ngrams = defaultdict(int)
    text = normalize_text(text)
    boundaries = re.compile(r'[\b\s]+')
    words = boundaries.split(text)

    for i in range(0, len(words) - (n - 1)):
        gram = tuple(words[i:i+n])
        ngrams[gram] += 1
    last_gram = tuple(words[-(n - 1):] + [END_OF_TEXT])
    ngrams[last_gram] += 1
    return dict(ngrams)


def generate(text, n=3):
    ngrams = count_ngrams(text, n)
    ngrams = gram_utils.ngram_next(ngrams, n)
    return ' '.join(gram_utils.generate_from_grams(ngrams, n))


def generate_from_samples(samples, n=3):
    ngrams = {}
    for sample in samples:
        sample_grams = count_ngrams(sample, n)
        sample_grams = gram_utils.ngram_next(sample_grams, n)
        ngrams = gram_utils.merge_grams(ngrams, sample_grams)

    return ' '.join(gram_utils.generate_from_grams(ngrams, n))
