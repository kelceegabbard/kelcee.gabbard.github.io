from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

'''def headshot(request):
    return render(request, 'headshot.html', {})
    '''