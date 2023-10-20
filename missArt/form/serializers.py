from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('ID', 'NAME', 'DATE', 'DUE', 'FEE', 'CONTACT_NO', 'EMAIL', 'STATUS')
