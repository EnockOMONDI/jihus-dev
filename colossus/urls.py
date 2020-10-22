from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from colossus.apps.core import views as core_views
from colossus.apps.clientapp import views as client_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard1/', core_views.dashboard, name='dashboard'),
    path('send/testsms/', core_views.dashboard, name='test_sms'),
    path('send/bulksms/', client_views.send_bulk_sms, name='send_bulk'),
    path('', include('colossus.apps.subscribers.urls', namespace='subscribers')),
    path('', core_views.dashboard, name='dashboard'),
    path('dashboard/', core_views.dashboardnew, name='dashboardnew'),
    path('idmanagement/', core_views.SenderIdMmanagement, name='idmanagement'),
    path('sendquicksms/', core_views.sendquicksms, name='sendquicksms'),
    path('setup/', core_views.setup, name='setup'),
    path('setup/account/', core_views.setup_account, name='setup_account'),
    path('settings/', core_views.SiteUpdateView.as_view(), name='settings'),
    path('accounts/', include('colossus.apps.accounts.urls')),
    path('lists/', include('colossus.apps.lists.urls', namespace='lists')),
    path('notifications/', include('colossus.apps.notifications.urls', namespace='notifications')),
    path('templates/', include('colossus.apps.templates.urls', namespace='templates')),
    path('campaigns/', include('colossus.apps.campaigns.urls', namespace='campaigns')),
    path('<slug:mailing_list_slug>/', core_views.subscribe_shortcut, name='subscribe_shortcut'),
    path('<slug:mailing_list_slug>/unsubscribe/', core_views.unsubscribe_shortcut, name='unsubscribe_shortcut'),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
