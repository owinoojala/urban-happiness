from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# def current_time(request):
#     now =  datetime.datetime.now()
#     html = "<html><body> It is now %s.</body></html>" % now
#     return HttpResponse(html)
def index(request):
    return render(request, "index.html",{'name':'Pthon Web Dev with Django'})
# def add(request):
#     num1 = int(request.POST["num1"])
#     num2 = int(request.POST["num2"])
#     result = num1 + num2
#     return render(request, 'result.html', {'result':result})

def hours_ahead(request):
    offset = int(request.POST["offset"])
    td = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'result.html', {'hours_ahead':td})
