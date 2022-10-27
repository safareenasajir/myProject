
from django.urls import path
from . import views

urlpatterns = [

    path('',views.add,name='add'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('lstvw/',views.Tasklistview.as_view(),name='lstvw'),
    path('dtvw/<int:pk>/',views.Taskdetailview.as_view(),name='dtvw'),
    path('uptvw/<int:pk>/', views.Taskupdateview.as_view(), name='uptvw'),
    path('dltvw/<int:pk>/', views.Taskdeleteview.as_view(), name='dltvw'),

]
