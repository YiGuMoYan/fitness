"""
URL configuration for fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from fitness import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fit/", include("fit.urls")),
    path("account/", include("account.urls")),
    path("training_log/", include("training_log.urls")),
    path("diet/", include("diet.urls")),
    path("body/", include("body.urls")),
    path("share/", include("share_log.urls")),
    path("comment/", include("comment.urls")),
    path("gym/", include("gym_location.urls")),
    path("food/", include("food.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
