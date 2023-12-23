from django.forms import ModelForm, DateInput
from cal.models import Event
from cal.models import CommentModel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'
    exclude=["post_like"]

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class CommentForm(ModelForm):
  class Meta:
    model = CommentModel
    fields = ('name' ,'event','description','image','video')