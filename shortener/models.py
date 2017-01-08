from django.db import models
from .utils import code_generator, create_shortcode
#to use variables from settings.py
from django.conf import settings
from .validators import validate_url, validate_dot_com

# instead of setting SHORTCODE_MAX = settings.SHORTCODE_MAX
# like this we ensure functioning of the App when used in another project without
# a specific SHORTCODE_MAX entry in settings
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class ShortyURLManager(models.Manager):
    #objects.all() will show only active entries
    def all(self, *args, **kwargs):
        qs = super(ShortyURLManager, self).all(*args, **kwargs).filter(active=True)
        return qs

    def refresh_shortcodes(self):
        new_codes = 0
        qs = ShortyURL.objects.filter(pk__gte = 1)
        for q in qs:
            q.shortcode = create_shortcode(q)
            print (q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)
# Create your models here.


class ShortyURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortyURLManager()

    def save(self, *args, **kwargs):
        print("saved")
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(ShortyURL,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
