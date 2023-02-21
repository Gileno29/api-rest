
from rest_framework.routers import DefaultRouter
from .views import EstoqueViewSet
from .models import Estoque
app_name='estoque'

router = DefaultRouter(trailing_slash=False)
router.register(r'api', EstoqueViewSet)

app_name = 'estoque'

router = DefaultRouter(trailing_slash=False)
router.register(r'estoque', EstoqueViewSet)

urlpatterns = router.urls
