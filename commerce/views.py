from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsProductOwner
from rest_framework.exceptions import PermissionDenied

# Write Views here
class ProductListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView, IsProductOwner):
    permission_classes = [IsProductOwner]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.user_type == 'Seller':
            serializer.save(seller=self.request.user)
        else:
            raise PermissionDenied('Only sellers can sell products!')

