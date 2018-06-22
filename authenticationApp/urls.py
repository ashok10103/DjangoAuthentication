from django.conf.urls import include,url
from .views import HomePageView


urlpatterns = [
    url('^$',HomePageView.as_view(),name="home")
]
