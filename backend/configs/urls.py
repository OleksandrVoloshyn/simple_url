from django.urls import path
from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from main.views import MainView, GetTopURLSView, RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title="Simplify urls API",
        default_version='v1',
        description="Make url shorter",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('create_short', MainView.as_view(), name='main_create'),
    path('rates', GetTopURLSView.as_view(), name='main_list_top'),
    path('redirect/<str:data>', RedirectView.as_view(), name='main_redirect'),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0)),
]
