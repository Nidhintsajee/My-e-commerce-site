from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.list_products, name='list_products'),
    url(r'^product/(?P<pk>\d+)/$', views.detail_product, name='detail_product'),
    url(r'^ecommerce/new/$', views.add_product, name='add_product'),
    url(r'^ecommerce/save/$', views.save_product, name='save_product'),
]


