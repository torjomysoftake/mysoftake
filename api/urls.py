from django.urls import path, include
from api.views import (
    CreateScheduleView,
    BookScheduleView,
    AvailableSlotView,
    AllScheduleList,
    WeeklyScheduleView,
    ManageScheduleView,
    DepartmentCreateView,
    DepartmentManageView,
    SlotCreateView,
    SlotManageView,
    SendEmailAPIView,
    EmailList,
    ProjectList,
    ProjectCreateView,
    ProjectManageView,
    HeroList,
    HeroManageView,
    HeroCreateView,
    ServiceList,
    ServiceManageView,
    ServiceCreateView,
    TeamMemberList,
    TeamMemberManageView,
    TeamMemberCreateView,
    AllSlotsList,
    CreateContactInquiryView
)
urlpatterns = [
    path('book-schedule/', BookScheduleView.as_view(), name='book-schedule'),
    path('all-schedule/', AllScheduleList.as_view(), name='all-schedule'),
    path('available-slot/<date>/', AvailableSlotView.as_view(), name='available-slot'),
    path('weekly-schedule/', WeeklyScheduleView.as_view(), name='weekly-schedule'),
    path('manage-schedule/<date>/', ManageScheduleView.as_view(), name='manage-schedule'),
    path('create-schedule/', CreateScheduleView.as_view(), name='create-schedule'),

    path('departments/', DepartmentCreateView.as_view(), name='department-list-create'),
    path('department/<str:pk>/', DepartmentManageView.as_view(), name='department-retrieve-update-destroy'),
    path('slot/', SlotCreateView.as_view(), name='slot-list-create'),
    path('slot/<str:pk>/', SlotManageView.as_view(), name='slot-retrieve-update-destroy'),
    path('send-email/', SendEmailAPIView.as_view(), name='send-email'),
    path('emails/', EmailList.as_view(), name='emails'),
    path('projects/', ProjectList.as_view(), name='projects'),
    path('create-project/', ProjectCreateView.as_view(), name='project-list-create'),
    path('project/<str:pk>/', ProjectManageView.as_view(), name='project-retrieve-update-destroy'),
    path('hero/', HeroList.as_view(), name='hero-list-create'),
    path('hero/<str:pk>/', HeroManageView.as_view(), name='hero-retrieve-update-destroy'),
    path('create-hero/', HeroCreateView.as_view(), name='hero-list-create'),

    path('service/', ServiceList.as_view(), name='service-list-create'),
    path('service/<str:pk>/', ServiceManageView.as_view(), name='service-retrieve-update-destroy'),
    path('create-service/', ServiceCreateView.as_view(), name='service-list-create'),

    path('team-member/', TeamMemberList.as_view(), name='team-member-list-create'),
    path('team-member/<str:pk>/', TeamMemberManageView.as_view(), name='team-member-retrieve-update-destroy'),

    path('all-slots/', AllSlotsList.as_view(), name='all-slots'),

    path('create-contact-inquiry/', CreateContactInquiryView.as_view(), name='create-contact-inquiry'),

]