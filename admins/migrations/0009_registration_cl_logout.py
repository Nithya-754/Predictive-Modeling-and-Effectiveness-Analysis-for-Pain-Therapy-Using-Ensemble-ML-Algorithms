# Generated by Django 4.0.9 on 2024-10-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_pain_relief_rh_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='cl_logout',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
