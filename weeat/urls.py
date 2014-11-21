from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.routers import DefaultRouter
from api import views
router = DefaultRouter()
router.register(r'categories', views.CategorieViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'orders', views.OrderViewSet)
#router.register(r'foodscat/foods', views.FoodsCategorieViewSet,'foods')

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'server.views.index', name='index'),
    url(r'^chef/$', 'server.views.chef', name='chef'),
    url(r'^chef/update_order/', 'server.views.update_order', name='update_order'),
    url(r'^users/login/$', 'server.views.login_user', name='login_user'),
    url(r'^users/logout/$', 'server.views.logout_user', name='logout_user'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
