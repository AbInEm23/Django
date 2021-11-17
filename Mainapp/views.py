from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html') #usually a lot but we are being simple, which would involve us evaluating post and gets
    