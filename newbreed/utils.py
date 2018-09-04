# Necessary libraries called...
import random
import string

from django.utils.text import slugify


def random_string_gen(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_gen(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{rand_str}".format(

            slug=slug,
            rand_str=random_string_gen(size=4))

        return unique_slug_gen(instance, new_slug=new_slug)

    return slug
