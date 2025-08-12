from django.urls import path
from . import views

urlpatterns = [
    path('', views.bulk_upload, name='upload'),
    path('results/', views.results_view, name='results'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('clear/', views.clear_resumes, name='clear_resumes'),
    path('extract/', views.extract_keywords_view, name='extract_keywords'),
    path('save-profile/', views.save_role_profile, name='save_profile'),
    path('load-keywords/<str:role_name>/', views.load_role_keywords, name='load_keywords'),
]