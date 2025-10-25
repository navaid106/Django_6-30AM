from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from testapp.models import Employee


class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=40)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=40)


    def validate(self,data):
        ename = data.get('ename')
        esal = data.get('esal')

        if ename.lower() == 'salman khan':
            if esal < 90000:
                raise serializers.ValidationError('Salman khan Salary should be minimum 90k')
        return data
            




    def validate_esal(self,value):
        if value < 4000:
            raise serializers.ValidationError('Employee salary should be minimum 4000')
        return value 









    # def create(self,validated_data):
    #     return Employee.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.eno = validated_data.get('eno',instance.eno)
        instance.ename = validated_data.get('ename',instance.ename)
        instance.esal = validated_data.get('esal',instance.esal)
        instance.eaddr = validated_data.get('eaddr',instance.eaddr)

        instance.save()
        return instance

