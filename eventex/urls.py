from django.conf.urls import url, include
from django.contrib import admin
from eventex.core.views import home, speaker_detail


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', speaker_detail, name='speaker_detail'),
    url(r'^admin/', admin.site.urls),
]
