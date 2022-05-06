from django.contrib import admin
from .models import Question, Theme, Choice

admin.site.register(Theme)
admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.
