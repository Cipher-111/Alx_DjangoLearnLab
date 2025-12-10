from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser


class Notification(models.Model):
    recipient = models.ForeignKey(
        CustomUser,
        related_name="notifications",
        on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        CustomUser,
        related_name="actor_notifications",
        on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)

    # Generic relation to Post, Comment, etc.
    target_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    target_object_id = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    target = GenericForeignKey('target_content_type', 'target_object_id')

    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.actor} {self.verb}"
