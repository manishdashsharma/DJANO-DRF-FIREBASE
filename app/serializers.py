from rest_framework import serializers

class CreateUserSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False, allow_blank=False)
    location = serializers.CharField(allow_null=False, allow_blank=False)

class UpdateUserSerializer(serializers.Serializer):
    user_id = serializers.CharField(allow_null=False, allow_blank=False)
    update_data = serializers.DictField(
        child=serializers.CharField(),
        help_text="JSON object with optional keys: name, location",
        required=True
    )

    def validate_update_data(self, value):
        """
        Check if the update_data contains only allowed keys.
        """
        allowed_keys = ['name', 'location']
        
        for key in value.keys():
            if key not in allowed_keys:
                raise serializers.ValidationError(
                    f"Invalid key: {key}. Allowed keys are: {', '.join(allowed_keys)}"
                )
        return value