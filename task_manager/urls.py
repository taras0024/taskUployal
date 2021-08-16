from django.urls import path

from task_manager.views import homePageView

urlpatterns = [
    path('', homePageView, name='home')

]
