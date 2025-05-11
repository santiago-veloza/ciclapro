from rest_framework import routers
from .views import InventarioViewSet

router = routers.DefaultRouter()
router.register(r'inventario', InventarioViewSet)

urlpatterns = router.urls