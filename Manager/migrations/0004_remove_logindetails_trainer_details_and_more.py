# Generated by Django 5.1.2 on 2024-12-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_logindetails_trainer_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logindetails',
            name='trainer_details',
        ),
        migrations.RemoveField(
            model_name='logindetails',
            name='user_details',
        ),
        migrations.AddField(
            model_name='logindetails',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]