from django.db import models

class DateAndTime(models.Model):
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.date_time)