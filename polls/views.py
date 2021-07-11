from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from .models import Question, Choice, UserProfile, Answer
from django.views import generic
from django.utils import timezone


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
#
#         return questions


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


def view(request):
    context = {}
    current_user = request.user
    user_id = current_user.id
    #get all user's answers
    answers = Answer.objects.all().filter(user=user_id)
    # лист пройденных опросов
    finish_questions_list = []
    for i in answers:
        if i.question.id not in finish_questions_list:
            finish_questions_list.append(i.question.id)
    # получаем доступные опросы
    questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


    # формируем лист ожидания опросов
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
        selected_choice.votes += 1
        selected_choice.save()
        print('user_id', user_id)
        print('question', question)
        print('selected_choice', selected_choice)
        print('created', created)
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))







# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     choice = request.POST.get('choice')
#     user = request.user
#     user_id = user.id
#     if not choice:
#         return render(request, 'polls/question_detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice"
#         })
#     # selected_choice = question.choice_set.filter(pk=choice)
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     print(selected_choice, 'выбранный выбор')
#     if not selected_choice:
#         return render(request, 'polls/question_detail.html', {
#             'question': question,
#             'error_message': "Incorrect choice"
#         }),
#
#     created = Answer.objects.get_or_create(user=user_id, question=question, choice=selected_choice)
#     if created:
#         selected_choice.votes += 1
#         selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice"
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Alweys return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button
    # return HttpResponseRedirect(reverse('polls:results',
    #                                     args=(question.id,)))