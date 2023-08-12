from django.urls import path
from Codeleap_api import views


urlpatterns = [
    path('/careers/', views.PostList.as_view()),
    path('/careers/<int:pk>/', views.PostDetail.as_view()),
]