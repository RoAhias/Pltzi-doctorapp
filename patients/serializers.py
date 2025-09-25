from rest_framework import serializers


from .models import Patient, Insurance, MedicalRecord


class PatientSerializer(serializers.ModelSerializer):
    class meta:
        model = Patient
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class meta:
        model = Insurance
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class meta:
        model = MedicalRecord
        fields = '__all__'