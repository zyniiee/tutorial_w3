from django.urls import path

from polls.views import index, vote, detail, results, choice_detail

urlpatterns = [
    path('', index, name="home"),
    path("<int:question_id>/detail", detail, name="detail"),
    path("<int:question_id>/results", results, name="results"),
    path("vote", vote, name="vote"),
    path("choice/<int:choice_id>/detail", choice_detail, name="choice detail")

]