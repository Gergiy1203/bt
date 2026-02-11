import django
import sys, os
import fastapi
from django.conf.global_settings import INSTALLED_APPS
from django.http import HttpResponse
from fastapi.middleware.cors import CORSMiddleware
from django.db import models





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather.urls')),
]




def index(request):
    return render(request, 'wether/index.html')




class City(models.Model):
    name = models.CharField(max_length=25)


def __str__(self):
        return self.name




class Meta:
    verbose_name_plural = 'cities'





def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)





def vote(request, questioon_id):
    return HttpResponse("You're looking at question %s." % questioon_id)







urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.questioon_text for q in latest_question_list])
    return HttpResponse(output)



















class Question(models.Model):
    question_text = models.CharFild(max_length=200)
    pub_data = models.DateTimeField("date pulished")


class Choice(models.Model):
    questioon = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




# INSTALLED_APPS = [
  #  'django.contrib.admin',
   # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
    #'polls.apps.PollsConfig',
    #'users.apps.UsersConfig',
    #'quizzes.apps.QuizzesConfig',
    #'blog.appsBlogConfig',
#]
