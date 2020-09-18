from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    word_dictionary = {}
    word_list = fulltext.upper().split()
    for word in word_list:
        if word in word_dictionary:
            # Increase count of word
            word_dictionary[word] += 1
        else:
            # Add word to dictionary
            word_dictionary[word] = 1
        sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
        
    return render(request, 'count.html', {'fulltext' : fulltext, 'count_total' : len(word_list), 'word_dictionary' : sorted_words})