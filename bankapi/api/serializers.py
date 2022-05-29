# -*- coding: utf-8 -*-


from rest_framework import serializers

from api.models import branches

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = branches
        fields = ('ifsc','bank_id','branch','address','city','district','state')