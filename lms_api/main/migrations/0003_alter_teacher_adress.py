# Generated by Django 5.0.3 on 2024-03-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='adress',
            field=models.CharField(max_length=255),
        ),
    ]
