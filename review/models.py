from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models

from PIL import Image


class Ticket(models.Model):

    IMAGE_MAX_SIZE = (800, 800)

    title = models.CharField(max_length=128, verbose_name='Titre', null=False, blank=False)
    description = models.TextField(max_length=2048, null=False, blank=False, verbose_name='Description')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image')
    time_created = models.DateTimeField(auto_now=True)
    review_created = models.BooleanField(default=False)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):

    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)],
        verbose_name='Note', null=False, blank=False
        )
    headline = models.CharField(max_length=128, verbose_name='Titre', null=False, blank=True)
    body = models.CharField(max_length=8192, verbose_name='Commentaire', null=False, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
        )

    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        unique_together = ('user', 'followed_user')
