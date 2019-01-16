from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):

    TO_DO = '0'
    IN_PROGRESS = '1'
    DONE = '2'
    STATUS_CHOICES = (
        (TO_DO, 'To do'),
        (IN_PROGRESS, 'In progress'),
        (DONE, 'Done')
    )
    status =  models.CharField(max_length=1,
                                      choices=STATUS_CHOICES,
                                      default=TO_DO)
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/notes/{}/{}/".format(self.author.username, self.id)

    def get_edit_url(self):
        return "/notes/{}/{}/edit/".format(self.author.username, self.id)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
