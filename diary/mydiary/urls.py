from django.urls import path
from . import views

app_name='mydiary'
urlpatterns = [
    path('show/', views.show, name='show'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
    path('<int:todo_id>/update', views.update, name='update'),
    path('add/', views.add, name='add')
]