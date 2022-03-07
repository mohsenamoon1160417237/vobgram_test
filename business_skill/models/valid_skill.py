from django.db import models

from .skill_tag import SkillTag


class ValidSkill(models.Model):

    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    selected_number = models.PositiveIntegerField(default=0)
    tag = models.ManyToManyField(SkillTag,
                                 related_name='valid_skills')
