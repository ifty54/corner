
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.views import home  # type: ignore # Import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add this line for the home page
    path('tweet/', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
