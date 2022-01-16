import uuid
from django.contrib.auth.models import User
from django.db import models


def get_user_suffix(user_id):
        result = User.objects.get(pk=user_id)
        return "_".join([result.username, str(result.pk)])
    

def user_img_dir(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4())[:13], ext)
    return '{0}/images/user/{1}'.format(get_user_suffix(instance.user.id), filename)


class Profile(models.Model):
    """Profile model.
    Proxy model that extends the base data with other
    information.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(max_length=200, blank=True)
    photo = models.ImageField(
        upload_to=user_img_dir,
        blank=True,
        null=True
    )
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('user',)

    def __str__(self):
        """Return username"""
        return self.user.username
    
    