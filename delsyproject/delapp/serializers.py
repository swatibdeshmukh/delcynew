from rest_framework import serializers
from delapp.models import *

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
   class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    experience = ExperienceSerializer( many=True)
    addressDetails = AddressDetailsSerializer()
    qualification = QualificationSerializer( many=True)
    project = ProjectSerializer( many=True)
    class Meta:
        model = Employee
        fields = '__all__'

   
    # def create(self, validated_data):
        
    #     e=Employee.objects.latest()
    #     if e:
    #         regid="EMP001"
    #     else:
    #         regid=e.id+1
    #         regid="EMP"+"00"+str("regid"
    #         )



    