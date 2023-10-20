# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import About

# create a serializer class
class AboutSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = About
		fields = ('id', 'description')
