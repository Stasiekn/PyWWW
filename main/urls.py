"""pywww URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from main.views import  hello_word, about, some_test, contact, user_profile
app_name='main'

urlpatterns = [
    path('', hello_word, name='hello'),
    path('testy', some_test, name='some_test'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user/<int:user_id>.profile', user_profile, name="userprofile")
]
