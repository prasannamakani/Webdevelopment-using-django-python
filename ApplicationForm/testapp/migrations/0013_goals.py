# Generated by Django 5.1.2 on 2025-02-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_alter_personalassessment_referee1_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShortTermGoals', models.TextField()),
                ('LongTermGoals', models.TextField()),
                ('EverAttendMnjSoftwareInterview', models.TextField()),
            ],
        ),
    ]
