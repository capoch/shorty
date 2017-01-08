from django.conf import settings
from django_hosts import patterns, host

#this is the old url pattern from django versions previos 1.10
#django-hosts might adapt this and use the same url pattern as django itself

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='default_h'),
    host(r'(?!www).*', 'shorty.hostsconf.urls', name='wildcard'),
)
