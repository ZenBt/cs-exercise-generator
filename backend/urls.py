from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("api/", include("apps.cs_gen.urls")),
    # path("auth/", include('djoser.urls')),
    # OpenAPI 3 documentation with Swagger UI
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(template_name="swagger-ui.html",
                                                        url_name="schema"), name="swagger-ui",),
    path('docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
