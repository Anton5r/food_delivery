from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, OrganizationViewSet, SushiproductsViewSet, LatestAppVersionView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'sushiproducts', SushiproductsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'organization', OrganizationViewSet)
# router.register(r'update', LatestAppVersionView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/update/', LatestAppVersionView.as_view(), name='latest-app-version'),
]