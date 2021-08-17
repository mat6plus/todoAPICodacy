from django.urls import path
from .views import TodoList,TodoDetails,TodoCreate,TodoUpdate,TodoDelete




urlpatterns = [
    path('', TodoList.as_view()),
    path('create', TodoCreate.as_view()),
    path('detail/<int:pk>', TodoDetails.as_view()),
    path('update/<int:pk>', TodoUpdate.as_view()),
    path('delete/<int:pk>', TodoDelete.as_view()),
]