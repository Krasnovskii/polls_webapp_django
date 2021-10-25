from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Answer
from django.views import generic
from django.utils import timezone



class DetailView(generic.DetailView):

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class StatisticView(generic.ListView):
    """Statistic of all questions"""
    context_object_name = 'questions'
    template_name = 'polls/statistic.html'

    def get_queryset(self):
        return Question.objects.all()


def view(request):
    context = {}
    current_user = request.user
    user_id = current_user.id

    #get all user's answers
    answers = Answer.objects.all().filter(user=user_id)

    # list of the answered questions
    finish_questions_list = []
    for i in answers:
        if i.question.id not in finish_questions_list:
            finish_questions_list.append(i.question.id)

    # get all accessible questions
    questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

    # create a list of the non answered questions
    start_questions_list = []
    for j in questions:
        if j.id not in finish_questions_list:
            start_questions_list.append(j)
    context['start_question_list'] = start_questions_list
    return render(request, 'polls/index.html', context)



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    current_user = request.user
    user_id = current_user.id
    choice = request.POST.get('choice')
    if not choice:
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    selected_choice = question.choice_set.get(pk=choice)
    if not selected_choice:
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "Incorrect choice"
        })
    created = Answer.objects.get_or_create(user=user_id, question=question, choice=selected_choice)
    if created:
        # save answer in global statistic
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
