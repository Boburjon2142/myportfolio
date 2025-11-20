from django.urls import path

from . import views

app_name = "achievements"

urlpatterns = [
    path("", views.achievement_list_view, name="list"),
    path("<slug:slug>/", views.achievement_detail_view, name="detail"),
]
