from django.db import models
import random, string
# Create your models here.
def code_generator(size=6, chars = string.ascii_lowercase + string.digits):
    return  ''.join(random.choice(chars) for _ in range(size))
    # this line does the same like these 4 lines:
    #new_choice = ''
    #for i in range(size):
    #    new_choice += random.choice(chars)
    #return new_choice

class ShortyURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("saved")
        self.shortcode = code_generator()
        super(ShortyURL,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
