from django.contrib import admin
from django.urls import path, include

# for swagger setting
from .swagger import swagger_urlpatterns

# end swagger setting
''

# for media setting
from django.conf.urls.static import static

from . import settings

# end media setting
''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('question.urls')),
]


# add media urls to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# add to main urlpatterns swagger_urls
urlpatterns += swagger_urlpatterns
# end adding
