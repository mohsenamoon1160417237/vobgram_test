from django.db import models


class SkillTag(models.Model):

    title = models.CharField(max_length=150,
                             unique=True)
