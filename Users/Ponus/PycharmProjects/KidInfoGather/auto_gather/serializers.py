from django.core import serializers
from django.contrib.auth.models import User
from auto_gather.models import Subdomain, Domain


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class SubdomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdomain
        fields = ('id', 'ip', 'url', 'url_valid')


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id', 'ip', 'url', 'url_valid')