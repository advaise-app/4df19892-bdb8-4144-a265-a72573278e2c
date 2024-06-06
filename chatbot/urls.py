from django.urls import path
from . import views

urlpatterns = [
    path('answer/', views.answer_query, name='answer_query'),
]