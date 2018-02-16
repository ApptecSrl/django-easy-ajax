from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<strategy_name>[-\w]+)/(?P<pk>\d+)/$', views.AjaxBaseSerializedView.as_view(),
        name='django-easy-ajax-selector'),
]
