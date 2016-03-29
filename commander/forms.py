from django import forms
from .models import Shot

class ShotForm(forms.ModelForm):
    class Meta:
        model = Shot
        fields = ('IOT_id',
                  'gps_lat',
                  'gps_long',
                  'gps_elev',
                  'heading_point')