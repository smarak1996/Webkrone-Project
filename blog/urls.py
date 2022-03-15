from . import views
from django.urls import path


urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('<str:tag_slug>', views.post_list, name='post_list_by_tag'),
    #path('<int:year>/<int:month>/<int:day>/<str:post>/',views.post_detail,name='post_detail'),
    path('<int:post_id>',views.post_share,name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<str:post>',views.post_detail,name='post_detail'),

]