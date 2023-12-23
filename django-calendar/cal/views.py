from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout,authenticate,login
from .models import *
from .utils import Calendar
from .forms import EventForm, CommentForm
from .weather import *


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
    
def event(request,pk):
    event_title = Event.objects.get(id=pk)
    post_likes = event_title.post_like.count()
    if request.user.is_authenticated:
        if request.method == "POST":
            if event_title.post_like.filter(id=request.user.id).exists():
                event_title.post_like.remove(request.user)
                event_title.save()
                return HttpResponseRedirect(reverse('cal:event',kwargs={'pk':pk})) 
            else:
                event_title.post_like.add(request.user)
                event_title.save()
                return HttpResponseRedirect(reverse('cal:event',kwargs={'pk':pk}))    
    else:
        return HttpResponseRedirect(reverse('cal:register_page'))
    context={
        'event_title': event_title,
        'id': pk,
        'post_likes':post_likes,  
    }
    return render(request, 'cal/selection.html',context) 

def new_event(request,event_id=None):
    if request.user.is_authenticated:
        instance = Event()
        if event_id:
            instance = get_object_or_404(Event, pk=event_id)
        form = EventForm(request.POST or None, instance=instance)
        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cal:calendar'))

        return render(request, 'cal/new_event.html', {'form': form}) 
    else:
        return HttpResponseRedirect(reverse('cal:register_page'))        

def delete(request,pk):
    Event.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('cal:calendar'))

def delete_comment(request,pk):
    CommentModel.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('cal:calendar'))

def edit(request,pk):
    instance = Event.objects.get(id=pk)
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:event',kwargs={'pk':pk}))
    context={
        'form': form,
        'id': pk,
    }
    return render(request, 'cal/modify_event.html',context)

def delete_comment_selection(request,pk):
    comment_to_delete = CommentModel.objects.get(id=pk)
    context={
        'comment_to_delete':comment_to_delete,
    }
    return render(request,'cal/delete_comment.html',context)

def comment_selection(request,pk):
    comment_instance = CommentModel.objects.get(id=pk)
    context={
         'comment_instance':comment_instance
     }
    return render(request,'cal/comment_selection.html',context)

def edit_comment(request,pk):
    instance = CommentModel.objects.get(id=pk)
    commentform = CommentForm(request.POST or None, instance=instance)
    if request.POST and commentform.is_valid():
        commentform.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    context={
        'commentform': commentform,
    }    
    return render(request,'cal/edit_comment.html',context)

def image_upload_view(request,pk):
    comments = CommentModel.objects.all().filter(event=pk)
    event = Event.objects.get(id=pk)
    commentform = CommentForm(initial={'event':pk})
    if request.method == 'POST':
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            name = commentform.cleaned_data["name"]
            event = commentform.cleaned_data["event"]
            description = commentform.cleaned_data["description"]
            image = commentform.cleaned_data["image"]
            video = commentform.cleaned_data["video"]
            commentform = CommentModel(name=name,event=event,description=description,image=image,video=video)
            commentform.save()
            return HttpResponseRedirect(reverse('cal:upload',kwargs={'pk':pk}))
    context={
        'commentform':commentform,
        'comments':comments,
        'title':event.title,
    }
    return render(request, 'cal/upload.html',context)

def chat(request):
    return render(request, 'cal/chat.html')

def weather(request,pk):
    context={
        'day':day,
        'descreption':descreption,
        'temp':temp
    }
    return render(request,'cal/weather.html',context)

def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request,'cal/login.html',{'form':form})

def register_page(request):
    form = UserCreationForm()
    if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('cal:login_page'))
    return render(request,'cal/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('cal:calendar'))