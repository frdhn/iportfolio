from django.urls import path

from five_app import views

urlpatterns = [
    path('oldtemplates',views.old,name='old'),
    path('newtemplatesadding', views.new, name='new'),
    path('portfoliosite', views.portfolio, name='portfolio')

]


