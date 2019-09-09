# Generated by Django 2.2.4 on 2019-09-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesharing', '0008_bikesharepreferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikesharepreferences',
            name='gbfs_hide_bikes_after_location_report_hours',
            field=models.IntegerField(default=1, help_text="Time period after the vehicles will hidden from GBFS, if there was no location report. Needs 'Gbfs Hide Bikes After Location Report Silence' activated."),
        ),
        migrations.AddField(
            model_name='bikesharepreferences',
            name='gbfs_hide_bikes_after_location_report_silence',
            field=models.BooleanField(default=False, help_text='If activated, vehicles will disappear from GBFS, if there was no location report in the configured time period.'),
        ),
    ]
