from django.shortcuts import render
from base.models import Schedule, BookedSchedule, Slot, Department, Project
# Create your views here.

from rest_framework.permissions import IsAuthenticated, IsAdminUser


from rest_framework import generics
from api.serializers import (
    ScheduleSerializer,
    BookingSerializer,
    BookingSlotSerializer,
    BookScheduleSerializer,
    ManageScheduleSerializer,
    DepartmentSerializer,
    SlotSerializer,
    EmailSerializer,
    ProjectSerializer
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from api.pagination import GlobalPagination

from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status   


class BookScheduleView(generics.CreateAPIView):

    queryset = Schedule.objects.all()
    serializer_class = BookScheduleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = serializer.save()

        return Response(
            {
                "message": "Slot booked successfully",
            },
            status=status.HTTP_201_CREATED
        )


class AllScheduleList(generics.ListAPIView):
    serializer_class = BookingSerializer
    pagination_class = GlobalPagination
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return BookedSchedule.objects.all()




class AvailableSlotView(generics.GenericAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'date'

    def get(self, request, *args, **kwargs):
        date = kwargs.get('date')


        schedule = Schedule.objects.filter(
            date=date
        ).first()

        if not schedule:
            return Response(
                {
                    "date": date,
                    "available_slots": []
                },
            )

        serializer = self.get_serializer(schedule)
        return Response(serializer.data)
    





from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta

class WeeklyScheduleView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date') 
        if not start_date_str:
            return Response(
                {
                    "message": "Start date is required",
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        
        week_days = [start_date + timedelta(days=i) for i in range(7)] 
        
        data = []
        for day in week_days:
            day_schedule = Schedule.objects.filter(date=day).prefetch_related('slots')
            slots_data = []
            for schedule in day_schedule:
                for slot in Slot.objects.all():
                    booked = BookedSchedule.objects.filter(schedule_date=day, schedule_slot=slot).exists()
                    status = "Available" if not booked else "Booked"
            
                    slots_data.append({
                        "start_time": slot.start_time.strftime('%H:%M'),
                        "end_time": slot.end_time.strftime('%H:%M'),
                        "status": status

                    })
            data.append({
                "date": day,
                "slots": slots_data
            })
        return Response(data)


class ManageScheduleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManageScheduleSerializer
    permission_classes = [IsAdminUser]
    queryset = Schedule.objects.all()
    lookup_field = 'date'

class CreateScheduleView(generics.CreateAPIView):
    serializer_class = ManageScheduleSerializer
    permission_classes = [IsAdminUser]



class DepartmentCreateView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DepartmentManageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class SlotCreateView(generics.CreateAPIView):
    serializer_class = SlotSerializer
    permission_classes = [IsAdminUser]


class SlotManageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SlotSerializer
    queryset = Slot.objects.all()


class SendEmailAPIView(generics.CreateAPIView):
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print('validated_data',serializer.validated_data)

        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']


        complete_message = f"""
        Sender Name: {serializer.validated_data['first_name'] + ' ' + serializer.validated_data['last_name']}
        Sender Email: {serializer.validated_data['email']}
        Motive: {serializer.validated_data['motive']}

        Message: {serializer.validated_data['message']}
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER

        try:
            send_mail(
                subject,
                complete_message,
                from_email,
                recipient_list,
                fail_silently=False,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Failed to send email",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(
            {
                "message": "Email sent successfully",
            },
            status=status.HTTP_201_CREATED
        )

from base.models import Email
class EmailList(generics.ListAPIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()

    pagination_class = GlobalPagination


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    pagination_class = GlobalPagination


class ProjectManageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAdminUser]


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAdminUser]


from base.models import Hero, Service, TeamMember
from api.serializers import HeroSerializer, ServiceSerializer, TeamMemberSerializer

class HeroList(generics.ListAPIView):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()

class HeroManageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
    permission_classes = [IsAdminUser]

class HeroCreateView(generics.CreateAPIView):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
    permission_classes = [IsAdminUser]

class ServiceList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceManageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [IsAdminUser]

class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [IsAdminUser]

class TeamMemberList(generics.ListAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()

class TeamMemberManageView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()
    permission_classes = [IsAdminUser]

class TeamMemberCreateView(generics.CreateAPIView):
    serializer_class = TeamMemberSerializer
    queryset = TeamMember.objects.all()
    permission_classes = [IsAdminUser]

class AllSlotsList(generics.ListAPIView):
    serializer_class = SlotSerializer
    queryset = Slot.objects.all()

    

from .serializers import ContactInquirySerializer
from base.models import ContactInquiry

class CreateContactInquiryView(generics.CreateAPIView):
    serializer_class = ContactInquirySerializer
    queryset = ContactInquiry.objects.all()

