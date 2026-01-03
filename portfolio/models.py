from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    technologies = models.CharField(max_length=200, help_text="e.g. Python, TensorFlow, SQL")
    date_created = models.DateField()

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    published_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title