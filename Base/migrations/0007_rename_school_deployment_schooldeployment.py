# Generated by Django 4.0 on 2024-11-03 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_remove_school_deployment_catagory_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='School_Deployment',
            new_name='SchoolDeployment',
        ),
    ]
