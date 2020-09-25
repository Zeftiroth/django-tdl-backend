from django.urls import path
from .views import  TaskAPIView, TaskDetails, GenericAPIView
# task_list, task_detail,
urlpatterns = [
    
    # path('task/',task_list),
    path('task/', TaskAPIView.as_view()),
    # path('task/<int:id>',task_detail),
    path('detail/<int:id>/', TaskDetails.as_view()),
    path('generic/task/<int:id>/', GenericAPIView.as_view()),
]

