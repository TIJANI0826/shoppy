"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
from products import views
from carts import views
from orders import views
from 




urlpatterns = [
    #Examples
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^s/$', views.search, name='search'),
    url(r'^products/$', views.all', name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', products.views.single, name='single_product'),
    url(r'^cart/(?P<id>\d+)/$', carts.views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', carts.views.add_to_cart, name='add_to_cart'),
    url(r'^cart/$', carts.views.view, name='cart'),
    url(r'^checkout/$', orders.views.checkout, name='checkout'),
    url(r'^orders/(?P<username>[\w-]+)$', orders.views.orders, name='user_orders'),
    url(r'^ajax/dismiss_marketing_message/$', marketing.views.dismiss_marketing_message,
        name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', marketing.views.email_signup, name='ajax_email_signup'),
    url(r'^ajax/add_user_address/$', account.views.add_user_address, name='ajax_add_user_address'),

    # url(r'^blog/', include('blog.urls')),
    # (?P<all_items>.*)
    # (?P<id>\d+)
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/logout/$', account.views.logout_view, name='auth_logout'),
    url(r'^accounts/login/$', account.views.login_view, name='auth_login'),
    url(r'^account/register/$', account.views.registration_view, name='auth_register'),
    url(r'^account/address/add/$', account.views.add_user_address, name='add_user_address'),
    url(r'^account/activate/(?P<activation_key>\w+)/$', account.views.activation_view, name='activation_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

