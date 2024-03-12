from django.urls import path
from . import views

urlpatterns = [
    path('cv1/', views.cv1, name='cv1'),
    path('cv2/', views.cv2, name='cv2'),
    path('cv/<str:username>/', views.view_cv, name='view_cv'),
    path('cv_2/<str:username>/', views.cv_2, name='cv_2'),
    path('generate_fake_data/', views.generate_fake_data, name='generate_fake_data'),
    path('',views.home, name='home'),
]
