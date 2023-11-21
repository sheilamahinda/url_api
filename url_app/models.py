# set_url_data/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class SetUrlData(models.Model):
    audio_link = models.URLField()
    gif_link = models.URLField()
    alert_duration = models.IntegerField(default=5, choices=[(i, i) for i in range(11)])
    sound_volume = models.FloatField(default=0.5, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    min_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, validators=[MinValueValidator(0.0)])
    message_template = models.TextField(default='{sender_name} donated {amount}!')

    def __str__(self):
        return f'Set URL Data #{self.pk}'
from django.db import models

# Create your models here.
