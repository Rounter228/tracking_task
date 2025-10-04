from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('task_create', TaskCreateView.as_view(), name="task_create"),
]

app_name = "tracker_app"