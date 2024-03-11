from django.urls import path

from polls.views import index, vote, detail,results

urlpatterns = [
    path('', index, name="home"),
    path("<int:question_id>/detail", detail, name="detail"),
    path("<int:question_id>/results", results, name="results"),
    path("<int:question_id>/vote", vote, name="vote"),
]