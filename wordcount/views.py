from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['text']

    wordlist = fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word]=1

    sortedlist=sorted(worddictionary.items(), key=operator.itemgetter(1))

    return render(request, 'count.html', {'text':fulltext,'count':len(wordlist), 'sortedlist':sortedlist})
