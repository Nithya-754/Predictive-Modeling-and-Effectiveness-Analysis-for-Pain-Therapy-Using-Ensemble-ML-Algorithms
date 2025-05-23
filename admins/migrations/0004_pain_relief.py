# Generated by Django 4.0.9 on 2024-10-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_registration_type_of_pain'),
    ]

    operations = [
        migrations.CreateModel(
            name='pain_relief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField(max_length=50, null=True)),
                ('pain', models.IntegerField(max_length=50, null=True)),
                ('swelling', models.IntegerField(max_length=50, null=True)),
                ('stiffness', models.IntegerField(max_length=50, null=True)),
                ('warmth_and_redness', models.IntegerField(max_length=50, null=True)),
                ('weakness_or_instability', models.IntegerField(max_length=50, null=True)),
                ('popping_or_grinding_sensation', models.IntegerField(max_length=50, null=True)),
                ('limites_range_of_motion', models.IntegerField(max_length=50, null=True)),
                ('swelpain_with_certain_movementsling', models.IntegerField(max_length=50, null=True)),
                ('tenderness', models.IntegerField(max_length=50, null=True)),
                ('bearing_weight', models.IntegerField(max_length=50, null=True)),
                ('dull_aching_pain', models.IntegerField(max_length=50, null=True)),
                ('sharp_stabbing_pain', models.IntegerField(max_length=50, null=True)),
                ('muscle_spams', models.IntegerField(max_length=50, null=True)),
                ('radiating_pain', models.IntegerField(max_length=50, null=True)),
                ('numbness_or_tingling', models.IntegerField(max_length=50, null=True)),
                ('weakness', models.IntegerField(max_length=50, null=True)),
                ('b_stiffness', models.IntegerField(max_length=50, null=True)),
                ('pain_with_movement', models.IntegerField(max_length=50, null=True)),
                ('pain_that_worsens_at_night', models.IntegerField(max_length=50, null=True)),
                ('fatigue', models.IntegerField(max_length=50, null=True)),
                ('loss_of_range_of_motion', models.IntegerField(max_length=50, null=True)),
                ('fever_or_chills', models.IntegerField(max_length=50, null=True)),
            ],
        ),
    ]
