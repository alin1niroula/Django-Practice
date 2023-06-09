from django.urls import path, include
from rest_framework import routers
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'items', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('product-filter/',  ProductFilterView.as_view(), name='product-filter/'),
    path('product-crud/<int:pk>',  CRUDViewSet.as_view(), name='product-crud'),
]