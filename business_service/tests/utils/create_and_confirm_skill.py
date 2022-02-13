from accounts.models.admin_data_confirm import AdminDataConfirm

from business_service.models.valid_skill import ValidSkill
from business_service.models.business_skill import BusinessSkill



def create_and_confirm_skill(business_prof_obj):

    valid_skill = ValidSkill.objects.create(title='web',
                                            description='...')
    AdminDataConfirm.objects.create(target=valid_skill,
                                    is_confirmed=True)

    skill = BusinessSkill.objects.create(business_profile=business_prof_obj,
                                         valid_skill=valid_skill)
    return skill
