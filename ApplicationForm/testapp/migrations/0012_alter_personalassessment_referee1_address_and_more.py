# Generated by Django 5.1.2 on 2025-02-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_personalassessment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee1_Address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee1_Company',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee1_Contact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee1_Name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee1_YearsAcquaintance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee2_Address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee2_Company',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee2_Contact',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee2_Name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Referee2_YearsAcquaintance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='SportHobby_Why',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Strength1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Strength2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Strength3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Strength4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Strength5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Weakness1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Weakness2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Weakness3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Weakness4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalassessment',
            name='Weakness5',
            field=models.TextField(blank=True, null=True),
        ),
    ]
