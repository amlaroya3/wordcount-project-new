from django.http  import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html', {'name': 'Amlan'})

def count(request):

    mtxt = request.GET['fulltext']
    mwords = mtxt.split()
    wrdcnt ={}
    for word in mwords :
        if wrdcnt.get(word) is not None :
                wrdcnt[word] += 1
        else :
             wrdcnt[word] = 1
    srtd = sorted(wrdcnt.items(), key = operator.itemgetter(1), reverse = True)
 #  print(srtd)
    return render(request, 'count.html', {'kount' : len(mwords), 'fulltext' : mtxt, 'sorted' : srtd})

def testpage(request):
    return HttpResponse('<h1>Testing Django</h1>')

def about(request):
    return render(request, 'about.html' )