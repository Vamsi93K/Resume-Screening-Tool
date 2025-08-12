from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/',null=True,blank=True)
    score = models.FloatField(default=0.0)
    matched_keywords = models.JSONField(default=list)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class JobDescription(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    extracted_keywords = models.JSONField(default=list)

class RoleKeywordProfile(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    keywords = models.JSONField(default=list)

class ResumeSource(models.Model):
    SOURCE_CHOICES = [('EMAIL', 'Email'), ('ATS', 'ATS')]
    source_type = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    source_details = models.TextField()
    last_fetched = models.DateTimeField(null=True)
