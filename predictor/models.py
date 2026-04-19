from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('normal', 'Normal User'),
    )
    
    # Existing fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='normal')
    
    # New profile fields
    # Personal Information
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    
    # Professional Information
    worker_id = models.CharField(max_length=50, blank=True, null=True)
    hospital_name = models.CharField(max_length=200, blank=True, null=True)
    clinic_name = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    
    # Contact Information
    address = models.TextField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Professional Links
    linkedin_url = models.URLField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username
    
    @property
    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return '/static/default-avatar.png'

class Activity(models.Model):
    ACTION_TYPES = (
        ('upload', 'File Upload'),
        ('predict', 'Prediction Made'),
        ('download', 'Downloaded Results'),
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('view_dashboard', 'Viewed Dashboard'),
        ('filter_data', 'Filtered Data'),
        ('profile_update', 'Profile Updated'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, choices=ACTION_TYPES)
    details = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"