from django.urls import path
from M4_Web import views
from django.contrib.auth.views import login,logout
from django.conf.urls.static import static
from M4_Plan import settings
urlpatterns=[
    path('home/',views.home),
    path('aboutus/', views.about,name='about'),
    path('careers/', views.careers,name='careers'),
    path('contactus/', views.contact,name='contactus'),
    path('Education/', views.education),
    path('Fashion/', views.fashion),
    path('food/', views.food),
    path('healthcare/', views.healthcare),
    path('published_articles/', views.published,name='published'),
    path('retail/', views.retail),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)