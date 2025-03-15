from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Order, Organization, Sushiproducts, AppVersion
from .serializers import ProductSerializer, OrderSerializer, OrganizationSerializer, SushiproductsSerializer, AppVersionSerializer

class LatestAppVersionView(APIView):
    def get(self, request):
        try:
            latest_version = AppVersion.objects.latest('release_date')
            serializer = AppVersionSerializer(latest_version)
            return Response(serializer.data)
        except AppVersion.DoesNotExist:
            return Response(
                {'error': 'No app versions available.'},
                status=status.HTTP_404_NOT_FOUND
            )

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SushiproductsViewSet(viewsets.ModelViewSet):
    queryset = Sushiproducts.objects.all()
    serializer_class = SushiproductsSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer