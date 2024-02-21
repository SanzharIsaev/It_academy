"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls
from participants.views import ApplicationsForParticipantsAPIView
from customers.views import ApplicationsForCustomersAPIView
from news.views import NewsAPIView
from comments.views import CommentsAPIView
from gallery.views import GalleryAPIViews
from aboutus.views import AboutUsAPIView
from projects.views import ProjectsAPIViews
from team.views import TeamAPIViews



router = routers.DefaultRouter()
router.register(r'api/v1/participants', ApplicationsForParticipantsAPIView)
router.register(r'api/v1/customers', ApplicationsForCustomersAPIView)
router.register(r'api/v1/news', NewsAPIView)
router.register(r'api/v1/comments', CommentsAPIView)
router.register(r'api/v1/gallery', GalleryAPIViews)
router.register(r'api/v1/aboutus', AboutUsAPIView)
router.register(r'api/v1/projects', ProjectsAPIViews)
router.register(r'api/v1/team', TeamAPIViews)







urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls)),
]



urlpatterns += doc_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)