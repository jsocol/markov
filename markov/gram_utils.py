import random
from collections import defaultdict

from .text import END_OF_TEXT


def ngram_next(ngrams, n=3):
    options = defaultdict(lambda: defaultdict(int))
    for gram, count in ngrams.items():
        stem, ending = gram[0:n], gram[n:n + 1]
        if not ending:
            ending = END_OF_TEXT
        options[stem][ending] += count
    return dict((k, dict(v)) for k, v in options.items())


def normalize_counts(ngrams):
    for gram in ngrams:
        total = sum(ngrams[gram].values())
        for e in ngrams[gram]:
            ngrams[gram][e] /= total
    return ngrams


def weighted_choice(weights):
    """Given a dictionary of values and non-normalized (int) weights, pick
    a random value."""
    total = sum(weights.values())
    r = random.uniform(0, total)
    upto = 0
    for c, w in weights.items():
        if upto + w > r:
            return c
        upto += w


def generate_from_grams(ngrams, n):
    counts = dict((gram, sum(e.values())) for gram, e in ngrams.items())
    new_text = weighted_choice(counts)
    i = 0
    _last = new_text[i:i + n]
    _next = weighted_choice(ngrams[_last])
    while _next != END_OF_TEXT:
        new_text += _next
        i += 1
        _last = _last[1:] + _next
        _next = weighted_choice(ngrams[_last])
    return new_text


def merge_grams(old, new):
    for gram, endings in new.items():
        old.setdefault(gram, {})
        for e in endings:
            old[gram].setdefault(e, 0)
            old[gram][e] += 1
    return old
