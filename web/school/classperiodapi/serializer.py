from rest_framework import serializers
from classperiod.models import ClassPeriod
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"