from django.db import models


# Create your models here.
class Tasks(models.Model):
    ONGOING = 'Ongoing'
    COMPLETED = 'Completed'
    HELD = 'Held'
    STATUS_CHOICES = (
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed'),
        (HELD, 'Held'),
    )
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=100, null=False, blank=False, default='Description',
                                   verbose_name='Description')
    author = models.CharField(max_length=40, null=False, blank=False, default='Author', verbose_name='Author')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ONGOING)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Crated at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def get_status_color(self):
        status_colors = {
            'Ongoing': 'orange',
            'Completed': 'green',
            'Held': 'red'
        }
        return status_colors.get(self.status, 'gray')

    def __str__(self):
        return f"{self.pk}. {self.title}"
