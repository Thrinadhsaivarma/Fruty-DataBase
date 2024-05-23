from django.urls import path

from market import views
urlpatterns = [
    path('<int:pk>/',views.fruty_detail,name='fruty_detail')
]
