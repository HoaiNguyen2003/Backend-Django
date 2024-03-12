from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class CV(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    github_url = models.URLField()
    city = models.CharField(max_length=255)
    birth_date = models.DateField()
    university = models.CharField(max_length=255)
    introduction = models.TextField()
    skillset = models.TextField()
    rewards = models.TextField()
    projects = models.TextField()
    results = models.TextField()
    # Bạn có thể thêm các trường khác theo mẫu CV của mình

    def __str__(self):
        return self.full_name