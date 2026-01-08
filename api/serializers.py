from rest_framework import serializers
from base.models import Schedule, BookedSchedule, Slot, UserInformation, Department, Email, Project, ContactInquiry
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by']

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['pk','start_time', 'end_time']


class ScheduleSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, read_only=True)
    class Meta:
        model = Schedule
        fields = ['date', 'slots']
    


class BookScheduleSerializer(serializers.ModelSerializer):
    slot = serializers.PrimaryKeyRelatedField(many=False, queryset=Slot.objects.all(), write_only=True)
    user_info = UserSerializer(write_only=True)
    class Meta:
        model = Schedule
        fields = [ 'date', 'slot', 'user_info']

    
    def validate(self, attrs):
        if attrs['date'] < timezone.now().date():
            raise serializers.ValidationError("Date cannot be in the past")
        return attrs

    def create(self, validated_data):
        date = validated_data['date']
        slot = validated_data['slot']


        with transaction.atomic():
            try:
                schedule = Schedule.objects.get(date=date)
            except Schedule.DoesNotExist:
                raise serializers.ValidationError("No schedule found for this date")
            if slot in schedule.slots.all():
                raise serializers.ValidationError("Slot already booked")
            schedule.slots.add(slot)
            user = UserInformation.objects.create(**validated_data['user_info'])
            booking = BookedSchedule.objects.create(user=user, schedule_date=date, schedule_slot=slot)
        return schedule


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    schedule_slot = SlotSerializer(read_only=True)
    class Meta:
        model = BookedSchedule
        fields = ['user', 'schedule_date','schedule_slot','created_at']


class AvailableSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
    

class ScheduleSerializer(serializers.ModelSerializer):
    available_slots = serializers.SerializerMethodField( read_only=True)
    
    class Meta:
        model = Schedule
        fields = [ 'date', 'available_slots']

    
    def get_available_slots(self, obj):
        return SlotSerializer(Slot.objects.all().exclude(uuid__in=obj.slots.values_list('uuid', flat=True)), many=True).data

class ManageScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['deleted_at', 'deleted_by', 'created_at', 'updated_at']


class BookingSlotSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(read_only=True)
    class Meta:
        model = BookedSchedule
        fields = [ 'user', 'schedule']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['pk','name']


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by']


from base.models import Hero, Service, TeamMember

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by']


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = '__all__'

        read_only_fields = ['created_at', 'updated_at', 'deleted_at', 'deleted_by', 'is_resolved']






    