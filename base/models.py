from django.db import models
from django.utils import timezone
from project.abstract_model import BaseModel


class Slot(BaseModel):
    start_time = models.TimeField(default="09:00:00")
    end_time = models.TimeField(default="10:00:00")

    class Meta:
        unique_together = ("start_time", "end_time")

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Schedule(BaseModel):
    date = models.DateField()
    slots = models.ManyToManyField(Slot, blank=True)

    def __str__(self):
        return str(self.date)


class Department(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserInformation(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255, null=True, blank=True)
    purpose = models.TextField()

    def __str__(self):
        return self.name


class BookedSchedule(BaseModel):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    schedule_date = models.DateField(default=timezone.now)
    schedule_slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.user.name} - {self.schedule_date}"










class Project(BaseModel):
    STATUS = (
       ('Ongoing', 'Ongoing'),
       ('Completed', 'Completed'),
    )
    title = models.CharField(max_length=255)
    project_picture = models.ImageField(upload_to='media/project_pictures', null=True, blank=True)
    short_description = models.TextField()
    project_manager = models.CharField(max_length=255)
    overview = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255, choices=STATUS, default='Ongoing')

    def __str__(self):
        return self.title
    
    class Meta:
        
        ordering = ["-created_at"]
    
    @property
    def duration_in_weeks(self):
        return (self.end_date - self.start_date).days
    


class Email(BaseModel):
    MOTIVES = (
        ('General Enquiry', 'General Enquiry'),
        ('Job Application', 'Job Application'),
        ('Project Enquiry', 'Project Enquiry'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default="")
    email = models.EmailField()
    motive = models.CharField(max_length=255, choices=MOTIVES)
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["-created_at"]
    


class Hero(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/hero_pictures', null=True, blank=True)

class Service(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/service_pictures', null=True, blank=True)

class TeamMember(BaseModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/team_member_pictures', null=True, blank=True)
    short_description = models.TextField()

    @property
    def image_url(self):
        try:
            return self.image.url
        except:
            return ''
    
    

