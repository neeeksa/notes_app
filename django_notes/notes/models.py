from django.db import models


class Notes(models.Model):
    title = models.CharField('Name', max_length=50)
    full_text = models.TextField('Note')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/notes/{self.id}'

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
