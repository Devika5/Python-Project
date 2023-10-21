from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('listv/',views.Todolistview.as_view(), name='listv'),
    path('detailv/<int:pk>/',views.Tododetailview.as_view(), name='detailv'),
    path('upd/<int:pk>/',views.Updateview.as_view(),name='upd'),
    path('dlt/<int:pk>/',views.deleteview.as_view(),name='dlt'),

]




