from django.urls import path
from .views import index, question

urlpatterns = [
    path('', index, name="quizz-index"),
    path('question/', question, name="quizz-question")
]
