from django.urls import path

from .import views



urlpatterns = [
    path('', views.index_view,name='index'),
    path('kondate/', views.KondateList.as_view(), name='list-kondate'),
    path('kondate/<int:pk>/detail/', views.DetailKondateList.as_view(), name='detail-kondate'),
    path('kondate/create/', views.CreateKondateList.as_view(), name='create-kondate'),
    path('kondate/<int:pk>/update/', views.UpdateKondateList.as_view(), name='update-kondate'),
    path('kondate/<int:pk>/delete/', views.DeleteKondateList.as_view(), name='delete-kondate'),
]