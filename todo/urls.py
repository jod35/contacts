from django.urls import path
from . import views

app_name='todo'

urlpatterns=[
    path('',views.HomePageView.as_view(),name='home'),
    path('delete/<int:id>/',views.DeleteView.as_view(),name='delete_task'),
    path('update/<int:id>/',views.UpdateView.as_view(),name='update_task'),
    
]