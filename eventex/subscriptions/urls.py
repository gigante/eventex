from django.conf.urls import url
from eventex.subscriptions.views import new, detail


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', detail, name='detail'),
]
