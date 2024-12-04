from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include
from django.contrib import admin

import app.urls
import users.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app.urls)),
    path('users/', include(users.urls))
]
