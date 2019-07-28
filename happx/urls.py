from django.conf.urls import url

from happx import views

urlpatterns = [
    url(r'^base/$',views.base,name='base'),
    url(r'^register/$',views.register,name='register'),
    url(r'^auth_login/$',views.auth_login,name='auth_login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^pro/$',views.pro, name='pro'),
    url(r'^smart/$', views.smart, name='smart'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^submit/$', views.submit, name='submit'),
]