from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    """Serializers also take care of Validations"""
    name = serializers.CharField(max_length=10)