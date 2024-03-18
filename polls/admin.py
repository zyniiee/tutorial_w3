
# Register your models here.
from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Name", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    fields= ["question", "choice_text", "votes"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)