from django.db import models


class Budget(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
