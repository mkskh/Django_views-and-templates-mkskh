from django.urls import path

from home_page.views import HomePage

app_name = "todo"
urlpatterns = [
    path('', HomePage.as_view(), name="home_page"),
]