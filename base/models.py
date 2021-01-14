from django.db import models

# Create your models here.


class Profile(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    link = models.URLField(max_length=300, default='', blank=True)

    def __str__(self):
        return self.heading


class Skills(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill

    class Meta():
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
