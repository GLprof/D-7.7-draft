from django.urls import path
from .views import PList, PDetail, creat_p, update_p, delete_p

urlpatterns = [path('p/', PList.as_view()),
               path('p/<int:pk>/', PDetail.as_view(), name='p_detail'),
               path('p/create/', creat_p, name='p_create'),
               path('p/update/<int:pk>/', update_p, name='p_update'),
               path('p/delete/<int:pk>/', delete_p, name='p_delete'), ]




