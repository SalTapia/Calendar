from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, CommentModel
from django.urls import reverse, resolve 
from .views import *
from django.http import HttpRequest
import pytest

class TestingUrls(TestCase):

    @pytest.mark.django_db
    def test00(self):
        CommentModel.objects.create(
            name = "",
            event = None ,  
            description = "", 
            created = "",
            image = None,  
            video = None,
        )
        commentmodel00 = CommentModel.objects.get(id=1)
        self.assertEqual(commentmodel00.name,"")
        self.assertEqual(commentmodel00.event,None)
        self.assertEqual(commentmodel00.description,"")
        self.assertEqual(str(commentmodel00.image),"")
        self.assertEqual(str(commentmodel00.video),"")

    def test01(self):
        CommentModel.objects.create(
            name = "Mike",
            event = None ,  
            description = "Going to the market, sounds great!", 
            created = "",
            image = None,  
            video = None,
        )
        commentmodel00 = CommentModel.objects.get(id=1)
        self.assertEqual(commentmodel00.name,"Mike")
        self.assertEqual(commentmodel00.event,None)
        self.assertEqual(commentmodel00.description,"Going to the market, sounds great!")
        self.assertEqual(str(commentmodel00.image),"")
        self.assertEqual(str(commentmodel00.video),"")    
    def test02(self):
        self.assertEqual(reverse("cal:login_page"),"/login_page")
    def test03(self):
        self.assertEqual(reverse("cal:register_page"),"/register_page")
    def test04(self):
        self.assertEqual(reverse("cal:logout_view"),"/logout_view")
    def test05(self):
