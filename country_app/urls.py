from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import web_views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # Web interface URLs
    path('', web_views.country_list, name='country_list'),
    path('countries/<str:country_id>/', web_views.country_detail, name='country_detail'),
]

