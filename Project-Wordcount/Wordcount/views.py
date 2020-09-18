from django.http import HttpResponse
from django.shortcuts import render
import operator
import string

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    
    # clean up text so it only has words
    fulltext_clean = ''.join([char for char in fulltext if char not in string.punctuation])

    word_dictionary = {}
    word_list = fulltext_clean.upper().split()

    # count each occurence of each word in from the fulltext (word_list)
    for word in word_list:
        if word in word_dictionary:
            # Increase count of word
            word_dictionary[word] += 1
        else:
            # Add word to dictionary
            word_dictionary[word] = 1
        sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
        
    return render(request, 'count.html', {'fulltext' : fulltext, 'count_total' : len(word_list), 'word_dictionary' : sorted_words})

def about(request):
    return render(request, 'about.html')