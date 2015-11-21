from django.db import models


def published(self):
    return self.filter(active=True)

models.QuerySet.published = published

models.Manager.published = published

