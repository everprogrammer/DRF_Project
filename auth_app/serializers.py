from rest_framework import serializers
from auth_app.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = CustomUser
        fields = '__all__'

        
# Register serializer
class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'},
                                      write_only=True,
                                      required=True)
    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'user_type', 'password', 'password2', )
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def save(self):
        custom_user = CustomUser(
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            user_type = self.validated_data['user_type'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords did not match!'})

        custom_user.set_password(password)
        custom_user.save()

        return custom_user