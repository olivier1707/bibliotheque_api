from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_appli import views

urlpatterns = [
    path('genres/', views.genre_list, name='genres'),
    path('genres/<int:pk>/', views.genre_detail),
    path('livres/',views.LivreList.as_view()),
    path('livres/<int:pk>/', views.LivreDetail.as_view()),
    path('lecteurs/', views.LecteurList.as_view(), name='lecteur-list'),
    path('lecteurs/<int:pk>/', views.LecteurDetail.as_view(), name='lecteur-detail'),
    path('bibliothecaires/', views.BibliothecaireList.as_view(), name='bibliothecaire-list'),
    path('bibliothecaires/<int:pk>/', views.BibliothecaireDetail.as_view(), name='bibliothecaire-detail'),
]


# urlpatterns = format_suffix_patterns(urlpatterns)