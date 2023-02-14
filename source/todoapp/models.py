from django.db import models


# Create your models here.
class Tasks(models.Model):
    ONGOING = 'Ongoing'
    COMPLETED = 'Completed'
    HELD = 'Held'
    STATUS_CHOICES = (
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed'),
        (HELD, 'HELD'),
    )
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Article')
    text = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Text')
    author = models.CharField(max_length=40, null=False, blank=False, default='Author', verbose_name='Author')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ONGOING)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Crated at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

