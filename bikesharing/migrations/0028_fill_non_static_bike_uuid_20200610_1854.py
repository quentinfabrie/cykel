# Generated by Django 2.2.10 on 2020-06-10 16:54

from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    Bike = apps.get_model('bikesharing', 'Bike')
    for row in Bike.objects.all():
        row.non_static_bike_uuid = uuid.uuid4()
        row.save(update_fields=['non_static_bike_uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('bikesharing', '0027_bike_non_static_bike_uuid'),
    ]

    operations = [
    	migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
