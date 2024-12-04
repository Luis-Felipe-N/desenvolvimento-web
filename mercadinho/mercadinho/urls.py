from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include
from django.contrib import admin

import app.urls
import api.urls
import users.urls

urlpatterns = [
    path('api/', include(api.urls)),
    path('users/', include(users.urls)),
    path('admin/', admin.site.urls),
    path('', include(app.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
