#fuction of the view is to read and write to the database
from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html') #usually a lot but we are being simple, which would involve us evaluating post and gets

def topics(request):
    topics = Topic.objects.all().order_by('date_added')

    context = {'topics': topics} #the key is what we use in the template, the value is what youre getting from the view.

    return render(request, 'MainApp/topics.html', context) #passing the dictionary to the template
    

def topic(request,topic_id):
    topic = Topic.objects.get(id= topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'MainApp/topic.html', context)
