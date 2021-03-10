from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from .models import Question, Choice, UserProfile, User, Answer
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

    # Пытаюсь вставить отбор по дате и по юзеру, но получаю огромное количество ошибок....
    # def latest_question_list():
    #
    #     context = {}
    #     # Get user profile
    #     get_user = get_object_or_404(UserProfile, user=request.user)
    #     # get all answers of user
    #     user_answers = Answer.objects.all().filter(user=get_user)
    #     # filter questions of pub date
    #     questions = Question.objects.filter(pub_date__lte=timezone.now())
    #     latest_question_list = []
    #     for user in user_answers:
    #         for question in questions:
    #             if not user.id in questions:
    #                 latest_question_list.append(question)
    #     context['index'] = latest_question_list
    #
    #     return render(request, 'index.html', context)


class DetailView(generic.DetailView):

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class StatisticView(generic.ListView):
    """Statistic of all questions"""

    def get_queryset(self):
        return Question.objects.all()


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Alweys return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button
    return HttpResponseRedirect(reverse('polls:results',
                                        args=(question.id,)))
