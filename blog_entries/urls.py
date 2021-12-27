from django.urls import path
from blog_entries import views


urlpatterns = [

    path('<int:post_id>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),

]
