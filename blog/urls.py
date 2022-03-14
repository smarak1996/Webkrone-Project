from . import views
from django.urls import path

app_name='blog'
urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    path('post_list', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>/',views.post_detail,name='post_detail'),
    path('<int:post_id>',views.post_share,name='post_share'),
    path('postcomment/<int:year>/<int:month>/<int:day>/<str:post>',views.post_detail_comment,name='post_detail_comment'),

]