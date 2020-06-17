from django.contrib import admin
from django.urls import path, include
from main.views import MainView, UserViewSet
from rest_framework_nested import routers
from organizations.backends import invitation_backend
import notifications.urls

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', LoginView.as_view({'post': 'create'})),
    path("", MainView.as_view(), name='main'),
    path(r'^accounts/', include('organizations.urls')),
    path(r'^invitations/', include(invitation_backend().get_urls())),
    path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
