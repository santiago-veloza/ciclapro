from rest_framework import routers
from .views import VentaViewSet,  FacturaViewSet

router = routers.DefaultRouter()
router.register(r'ventas', VentaViewSet)

router.register(r'facturas', FacturaViewSet)

urlpatterns = router.urls
