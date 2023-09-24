from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SurveyQuestion, SurveyChoice

def index(request):
    survey_question_list = SurveyQuestion.objects.order_by()
    context = {"survey_question_list_list": survey_question_list}
    return render(request, "survey/index.html", context)

def detail(request, survey_question_id):
    survey_question = get_object_or_404(SurveyQuestion, pk = survey_question_id)
    return render(request, "survey/detail.html", {"survey_question": survey_question})

def results(request, survey_question_id):
    response = f"Results from question id {survey_question_id}"
    return HttpResponse(response, survey_question_id)

def choose_answer(request, survey_question_id):
    return f"Answering question {survey_question_id}"
