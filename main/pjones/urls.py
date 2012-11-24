from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
import registration

urlpatterns = patterns('',
    # Examples:
    #    url(r'^$', 'test1.views.home', name='home'),
    # url(r'^test1/', include('test1.foo.urls')),
    url(r'^$','cms.views.index',{},name = "index"),
    url(r'^about$','cms.views.about',{},name = "about"),
    url(r'^manager$','cms.views.manager',{},name = "manager"),
    url(r'^careers$','cms.views.careers',{},name = "careers"),
    url(r'^services$','cms.views.services',{},name = "services"),
    url(r'^director$','cms.views.director',{},name = "director"),
    url(r'^company$','cms.views.company',{},name = "company"),
    url(r'^projects$','cms.views.projects',{},name = "projects"),
    url(r'^help$','cms.views.help',{},name = "help"),
    url(r'^contact$','cms.views.contact',{},name = "contact"),
#    url(r'^user/',include('user_profiles.urls'),{},name = "user"),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/password_reset/$', 'django.contrib.auth.views.password_reset',{'template_name': 'accounts/password_reset_form.html'}, name='password_reset',),
    (r'^password_reset/done/$','django.contrib.auth.views.password_reset_done',{'template_name': 'accounts/password_reset_done.html'}),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm',{'template_name': 'accounts/password_reset_confirm.html'}),
    (r'^reset/done/$','django.contrib.auth.views.password_reset_complete',{'template_name': 'accounts/password_reset_complete.html'}),

)
#
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        url(r'^site_static/(?P<path>.*)$', 'django.views.static.serve', {
#            'document_root': settings.STATIC_ROOT,
#            'show_indexes': True,
#            }),
#    )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
