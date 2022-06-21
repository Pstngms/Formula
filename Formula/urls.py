from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import register, user_login, user_logout, profile, profile_update
from events.views import events_page, ViewEvents, AddReg, RemoveReg
from home.views import home_page
from news.views import get_category, news_page

urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),
    path('', home_page, name='home_page'),
    path('news/', news_page, name='news'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('news/category/<int:category_id>/', get_category, name='category'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('events/', events_page, name='events'),
    path('events/<int:pk>/', ViewEvents.as_view(), name='view_events'),
    path('registration/add', AddReg.as_view(), name='add'),
    path('registration/remove', RemoveReg.as_view(), name='remove'),
    path('profile', profile, name='profile'),
    path('profile/update/<int:id>/', profile_update, name='profile_update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
