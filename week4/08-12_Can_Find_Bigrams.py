def can_find(bigrams, words):
    return all(any(bigram in word for word in words) for bigram in bigrams)

print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))