from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

    #return HttpResponse("Rango says hey there partner! <br/> <a href = '/rango/about/'>Link to the about page</a>")

def about(request):
    return render(request, 'rango/about.html')
    #return HttpResponse("Rango says here is the about page. <br/> <a href = 'http://127.0.0.1:8000'>Link to the main page</a>")
