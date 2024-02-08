from rest_framework import serializers
from webapp.models import logindb

class loginserializer(serializers.ModelSerializer):

    class Meta:
        model=logindb
        fields=('username','e_mail','password')