from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from flowers.views import FlowersView
from categories.views import CategoriesView

router = SimpleRouter()

router.register('flowers', FlowersView)
router.register('categories', CategoriesView)

urlpatterns = [
  path('admin/', admin.site.urls),
  path("api/", include(router.urls))
] 

# urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)