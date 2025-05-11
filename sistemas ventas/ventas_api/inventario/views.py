from rest_framework import viewsets
from .models import Inventario
from .serializers import InventarioSerializer
from drf_yasg.utils import swagger_auto_schema

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    
    @swagger_auto_schema(tags=["Inventario"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=["Inventario"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    @swagger_auto_schema(tags=["Inventario"])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "mensaje": "¡Inventario creado con éxito!",
            "inventario": serializer.data
        }, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(tags=["Inventario"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=["Inventario"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(tags=["Inventario"])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    