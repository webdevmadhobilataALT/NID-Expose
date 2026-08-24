

import uuid

from django.db import models


class NIDCheck(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    nid_number = models.CharField(
        max_length=20,
    )

    visitor_ip = models.GenericIPAddressField()

    is_exposed = models.BooleanField(
        default=False,
    )


    match_count = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.nid_number