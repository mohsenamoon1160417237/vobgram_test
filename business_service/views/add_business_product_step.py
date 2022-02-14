from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.model_serializers.business_product_step import BusinessProductStepSerializer
from business_service.model_serializers.view.business_product_step import BusinessProductStepViewSerializer

from business_service.models.business_product_step import BusinessProductStep


class AddBusinessProductStep(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request, prod_step_id):

        product_step = get_object_or_404(BusinessProductStep, id=prod_step_id)
        serializer = BusinessProductStepViewSerializer(product_step)
        return Response({'status': 'get a product step object',
                         'product_step': serializer.data})

    def post(self, request, prod_id):

        serializer_data = {'business_product_id': prod_id,
                           'note': request.data['note'],
                           'step_url': request.data['step_url'],
                           'from_date': request.data['from_date'],
                           'to_date': request.data['to_date']}

        serializer = BusinessProductStepSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'created business product step',
                         'product step': serializer.data})

    def put(self, request, prod_step_id):

        product_step = get_object_or_404(BusinessProductStep,
                                         id=prod_step_id)

        product_id = product_step.business_product.id

        serializer_data = {'business_product_id': product_id,
                           'note': request.data['note'],
                           'step_url': request.data['step_url'],
                           'from_date': request.data['from_date'],
                           'to_date': request.data['to_date']}

        serializer = BusinessProductStepSerializer(product_step, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        return Response({'status': 'updated business product step',
                         'product step': serializer.data})

    def delete(self, request, prod_step_id):

        product_step = get_object_or_404(BusinessProductStep, id=prod_step_id)

        product = product_step.business_product

        step_number = product_step.step_number

        product_step.delete()

        product_steps = BusinessProductStep.objects.filter(business_product=product,
                                                           step_number__gt=step_number)
        for p_step in product_steps:

            p_step.step_number -= 1
            p_step.save()

        product.max_step_number -= 1
        product.save()

        return Response({'status': 'deleted product step'})
