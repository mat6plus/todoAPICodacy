from django.urls import path
from .views import TodoList,TodoDetails,TodoCreate,TodoUpdate,TodoDelete




urlpatterns = [
    path('', TodoList.as_view()),
    path('create', TodoCreate.as_view()),
    path('<int:pk>/details', TodoDetails.as_view()),
    path('<int:pk>/update', TodoUpdate.as_view()),
    path('<int:pk>/delete', TodoDelete.as_view()),
]