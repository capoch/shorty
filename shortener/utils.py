import random, string
#to use variables from setting
from django.conf import settings

# instead of setting SHORTCODE_MIN = settings.SHORTCODE_MIN
# like this we ensure functioning of the App when reused in another project without
# a specific SHORTCODE_MIN entry in settings
SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN, chars = string.ascii_lowercase + string.digits):
    return  ''.join(random.choice(chars) for _ in range(size))
    # this line does the same like these 4 lines:
    #new_choice = ''
    #for i in range(size):
    #    new_choice += random.choice(chars)
    #return new_choice

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    #here we want to check that this new_code doesn't exist already
    #but since we import code_generator to models we cannot import from models to utils
    #this is solved with this workaround:
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code
