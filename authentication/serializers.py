
from rest_framework import serializers

from .models import CustomerUser


class CustomerSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomerUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'telephone']
        extra_kwargs = {'password': {'write_only': True}}