from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
    CategoryView, ProductView
)

router = DR()

router.register('category', CategoryView)
router.register('products', ProductView)

urlpatterns = []

urlpatterns += router.urls