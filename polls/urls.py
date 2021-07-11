from django.urls import path

from . import views
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.view, name='view'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('statistic/', views.StatisticView.as_view(), name='statistic'),
]
