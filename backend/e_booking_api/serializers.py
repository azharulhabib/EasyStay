from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import (
    Admin,
    Customer,
    Owner,
    RentalListing,
    RentalImage,
    UtilityBillImage,
    CustomerBookingHistory,
    OwnerBookingHistory,
    Booking,
    Payment
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name', 'phone_number', 'slug', 'is_active', 'is_staff', 'is_superuser')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        
    def validate_password(self, value):
        from django.core.exceptions import ValidationError as DjangoValidationError
        try:
            get_user_model()._pass_valid(None, value)
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.messages if hasattr(e, 'messages') else str(e))
        return value

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        
        return user
    
class AdminSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Admin
        
    def create(self, validated_data):
        return Admin.objects.create_user(**validated_data)
        
class CustomerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Customer
       
    def create(self, validated_data):
        return Customer.objects.create_user(**validated_data)
       
class OwnerSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Owner
    
    def create(self, validated_data):
        return Owner.objects.create_user(**validated_data)
        
class RentalListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalListing
        fields = '__all__'
        read_only_fields = ('id',)
        
class RentalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalImage
        fields = '__all__'
        read_only_fields = ('id',)
        
class UtilityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilityBillImage
        fields = '__all__'
        read_only_fields = ('id',)
        
class CustomerBookingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBookingHistory
        fields = '__all__'
        read_only_fields = ('id',)
        
class OwnerBookingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerBookingHistory
        fields = '__all__'
        read_only_fields = ('id',)
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('id',)
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('id',)