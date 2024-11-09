from django.urls import path
from .views import actor_list, actor_detail, actor_create_or_edit, actor_delete

urlpatterns = [
    path('actors/', actor_list, name='actor_list'),
    path('actors/<int:pk>/', actor_detail, name='actor_detail'),
    path('actors/create/', actor_create_or_edit, name='actor_create'),
    path('actors/edit/<int:pk>/', actor_create_or_edit, name='actor_edit'),
    path('actors/delete/<int:pk>/', actor_delete, name='actor_delete'),  # Шлях для підтвердження видалення

]
