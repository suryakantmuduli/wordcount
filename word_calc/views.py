from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'word_calc/home.html')


def about(request):
    return render(request, 'word_calc/about.html')


def count(request):
    #for get the text in the page
    textbox = request.GET['textbox']
    #for split the lines
    lines = textbox.split()

    #for count the every word how many times.
    worddictionary = {}
    for word in lines:
        if word in worddictionary:
            #if the word is already in the dict then increase the word no.
            worddictionary[word] +=1
        else:
            #add in the dict.
            worddictionary[word] = 1

    return render(request, 'word_calc/count.html', {'textbox':textbox, 'lines':len(lines), 'worddictionary':worddictionary.items()})