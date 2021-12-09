#fuction of the view is to read and write to the database
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import EntryForm, TopicForm
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

    return render(request, 'Mainapp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('Mainapp:topics')

    context = {'form':form} #allows us to put it on the html skeleton 
    return render(request, 'Mainapp/new_topic.html', context)

def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Mainapp:topic', topic_id=topic_id)

    context = {'form':form, 'topic':topic}
    return render(request, 'Mainapp/new_entry.html', context)
