from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Question, Choice


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

def vote(request):
    choice_id= request.POST["choice"]
    choice = Choice.objects.get(id=choice_id)
    choice.votes= choice.votes + 1
    choice.save()
    return HttpResponseRedirect(reverse("detail", args=(choice.question.id,)))

def choice_detail(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    return render(request,
                  template_name="choice_detail.html",
                  context={"choice": choice})