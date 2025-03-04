# Generated by Django 5.1.1 on 2024-12-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Specialist', '0005_message_delete_chatmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist_details',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='specialist_details',
            name='status',
        ),
        migrations.AlterField(
            model_name='specialist_details',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specialist_details',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialist_details',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
