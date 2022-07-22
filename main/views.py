from django.shortcuts import render


# from django.http import HttpResponse
#
# # Create your views here.
#
#
# def index(request):
#     return HttpResponse('<h4>Check</h4>')
#
#
# def about(request):
#     return HttpResponse('<h4>About us</h4>')


# Create your views here.


def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'random', 'text']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
