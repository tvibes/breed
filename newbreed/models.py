from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

from django.db.models import signals

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

import uuid
from django.db.models.signals import pre_save

from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy

# Python file used for 'unique slug generation' is called here.
from .utils import unique_slug_gen


# Create your models here.
class Artisan(models.Model):
    MECHANIC = 'MCH'
    PAINTING = 'PTG'
    CARPENTRY = 'CTY'
    TILING = 'TLG'

    CAT_CHOICES = (
        (MECHANIC, 'MECHANIC'),
        (PAINTING, 'PAINTING'),
        (CARPENTRY, 'CARPENTRY'),
        (TILING, 'TILING'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    category = models.CharField(choices=CAT_CHOICES, default='MECHANIC', max_length=20, )
    image = models.ImageField(null=False, blank=False, default=1)
    width = models.IntegerField(default=338)
    height = models.IntegerField(default=254)
    slug = models.SlugField(default='page-slug', blank=True, unique=True)
    description = models.CharField(max_length=60, null=False, blank=False, default=5)
    detail = models.TextField(null=False, blank=False, max_length=2500, default=5)
    is_favourite = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": self.slug})

    class META:
        ordering = ['-timestamp']


# Here is the Pre_save receiver function and statement.
def pre_save_receiver_photo_model(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == '':
        instance.slug = unique_slug_gen(instance)


# The Pre_save Connect for photo model
pre_save.connect(pre_save_receiver_photo_model, sender=Artisan)
