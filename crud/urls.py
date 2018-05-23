from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/delete', views.delete, name='delete_user'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update_user'),
    path('<int:id>/edit', views.edit, name='edit_user'),

]