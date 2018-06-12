from django.conf.urls import url
from apps.HomePrincipal.views import inde,producc,similar
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$',inde, name="HomePrincipal"),
    url(r'^cientifica$',producc, name="produccion"),
    url(r'^similares$',similar, name="similar"),

]