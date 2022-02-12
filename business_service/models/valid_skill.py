from django.db import models
from accounts.models.admin_data_confirm import AdminDataConfirm


class ValidSkill(models.Model):

    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    selected_number = models.PositiveIntegerField(default=0)
    admin_data_confirm = models.OneToOneField(AdminDataConfirm,
                                              on_delete=models.DO_NOTHING,
                                              related_name='valid_skill',
                                              null=True)
