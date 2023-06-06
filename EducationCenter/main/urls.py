from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news_detail/<int:pk>/', views.news_detail, name='main-news-detail'),
    path('blog/', views.post, name='main-posts'),
    path('contact/', views.contact, name='main-contact'),
    path('admission/', views.admission, name='main-admission'),
    path('susses/', views.admission_susses, name='main-susses-message'),
    path('<str:id>', views.get_courses_by_id, name='into'),
    path('details/<str:id>', views.event_details, name='event_details'),
    path('courses/', views.allcourses, name='courses'),
    path('events/', views.get_events, name='main-events'),
]
