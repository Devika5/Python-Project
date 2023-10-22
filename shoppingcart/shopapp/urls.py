from . import views
from django.urls import path

app_name='shopapp'

urlpatterns =[
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:cslug>/',views.allprodcat,name='prodbycat'),
    path('<slug:cslug>/<slug:productslug>/',views.prodetail,name='procatdetail')
]