from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('new', views.new_event, name='new_event'),
	path('event<int:pk>', views.event, name='event'),
    path('edit_event/<int:pk>', views.edit, name='edit'),
    path('delete<int:pk>', views.delete, name='delete'), 
    path('delete_comment<int:pk>', views.delete_comment, name='delete_comment'), 
    path('comment_selection/<int:pk>', views.comment_selection, name='comment_selection'),
    path('delete_comment_selection/<int:pk>', views.delete_comment_selection, name='delete_comment_selection'), 
    path('edit_comment/<int:pk>', views.edit_comment, name='edit_comment'),
    path('upload/<int:pk>', views.image_upload_view,name='upload'),
    path('chat', views.chat, name='chat'), 
    path('weather/<int:pk>', views.weather, name='weather'),
    path('login_page', views.login_page, name='login_page'),
    path('register_page', views.register_page, name='register_page'), 
    path('logout_view', views.logout_view, name='logout_view'), 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


