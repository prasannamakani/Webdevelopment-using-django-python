# Generated by Django 5.1.2 on 2025-02-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_alter_previousemployersdetails_emailidofalternativereportingmanager3'),
    ]

    operations = [
        migrations.CreateModel(
            name='GapsInEducationAndKeyResponsibilitiesCurrentAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GapsFrom1', models.IntegerField()),
                ('GapsTo1', models.IntegerField()),
                ('GapsReason1', models.TextField()),
                ('GapsCompleteAddressAndLocation1', models.TextField()),
                ('GapsFrom2', models.IntegerField()),
                ('GapsTo2', models.IntegerField()),
                ('GapsReason2', models.TextField()),
                ('GapsCompleteAddressAndLocation2', models.TextField()),
                ('OrganizationChartCurrentPosition', models.TextField()),
                ('KeyResponsibilitiesCurrentAssignment1', models.TextField()),
                ('KeyResponsibilitiesCurrentAssignment2', models.TextField()),
                ('KeyResponsibilitiesCurrentAssignment3', models.TextField()),
                ('KeyResponsibilitiesCurrentAssignment4', models.TextField()),
            ],
        ),
    ]
