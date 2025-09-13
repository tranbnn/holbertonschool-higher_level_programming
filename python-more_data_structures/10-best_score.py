#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None

    for scores in a_dictionary:
        if scores == max(a_dictionary, key=a_dictionary.get):
            return scores
