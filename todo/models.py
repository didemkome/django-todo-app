# pylint: disable=no-member
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profiles'
        

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, verbose_name='Title', blank=True)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('project-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('project-delete', args=[self.pk])

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Title')
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('issue-detail', args=[self.pk])

    def get_update_url(self):
        return reverse('issue-update', args=[self.pk])

    def get_delete_url(self):
        return reverse('issue-delete', args=[self.pk])

