from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from achievements import views as achievement_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", achievement_views.home_view, name="home"),
    path("achievements/", include("achievements.urls")),
    path("timeline/", achievement_views.timeline_view, name="timeline"),
    path("skills/", achievement_views.skills_view, name="skills"),
    path("contact/", achievement_views.contact_view, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
