from django.http import HttpResponse

from django.shortcuts import render

from polls.models import Question


# Create your views here.
def index(request):
    question = Question.objects.all()
    return render(request,
                  template_name="index.html",
                  context={"all_questions": question})
def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    return render(request,
                  template_name="detail.html",
                  context={"question": q})


def results(request, question_id):
    return HttpResponse("You're looking at question %d." % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting %d." % question_id)
