from .models import test_db
from rest_framework import serializers


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = test_db
        fields = ['id', 'date', 'latitude', 'longitude', 'equip_id', 'serial',
            'v1', 'v2', 'v3', 'v4', 'v5', 
            'v6', 'v7', 'v8', 'v9', 'v10', 
            'v11', 'v12', 'v13', 'v14', 'v15', 
            'v16', 'v17', 'v18', 'v19', 'v20', ]
