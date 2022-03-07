from business_skill.models.skill_tag import SkillTag
from business_skill.models.valid_skill import ValidSkill

from accounts.models.system_data_confirm import SystemDataConfirm

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


def searchSkillByTag(query):

    skill_tags = SkillTag.objects.filter(title__icontains=query)

    skill_tag_ids = skill_tags.values('id')

    found_valid_skills = ValidSkill.objects.filter(Q(title__icontains=query) |
                                                   Q(description__icontains=query))

    valid_skill_cnt = ContentType.objects.get(app_label='business_skill',
                                              model='validskill')

    valid_skill_confs = SystemDataConfirm.objects.filter(target_ct=valid_skill_cnt,
                                                         is_latest=True,
                                                         is_confirmed=True)

    valid_skills = ValidSkill.objects.filter(Q(tag__id__in=skill_tag_ids) |
                                             Q(id__in=found_valid_skills.values('id')),
                                             id__in=valid_skill_confs.values('target_id'))

    return valid_skills
