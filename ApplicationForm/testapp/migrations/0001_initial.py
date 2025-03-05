# Generated by Django 5.1.2 on 2025-02-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=123)),
                ('FatherName', models.CharField(max_length=123)),
                ('Nationality', models.CharField(max_length=123)),
                ('SocialSecurityNumber', models.IntegerField()),
                ('Sex', models.CharField(max_length=123)),
                ('MaritalStatus', models.CharField(max_length=123)),
                ('PanCardNumber', models.CharField(max_length=123)),
                ('DateOfBirth', models.IntegerField()),
                ('PlaceOfBirth', models.CharField(max_length=123)),
                ('PresentHouseNumber', models.IntegerField()),
                ('PermanentHouseNumber', models.IntegerField()),
                ('PresentCity', models.CharField(max_length=123)),
                ('PermanentCity', models.CharField(max_length=123)),
                ('PresentState', models.CharField(max_length=123)),
                ('PermanentState', models.CharField(max_length=123)),
                ('PresentPinCode', models.IntegerField()),
                ('PermanentPinCode', models.IntegerField()),
                ('PresentPeriodOfStay', models.CharField(max_length=123)),
                ('PermanentPeriodOfStay', models.CharField(max_length=123)),
                ('PresentTelephoneNumber', models.IntegerField()),
                ('PermanentTelephoneNumber', models.IntegerField()),
                ('PresentMobileNumber', models.IntegerField()),
                ('PermanentMobileNumber', models.IntegerField()),
                ('PresentEmailId', models.EmailField(max_length=123)),
                ('PermanentEmailId', models.EmailField(max_length=123)),
                ('PresentInstantMsgSystemId', models.CharField(max_length=123)),
                ('PermanentInstantMsgSystemId', models.CharField(max_length=123)),
                ('PassportNumber', models.CharField(max_length=123)),
                ('DateOfIssue', models.DateField(max_length=123)),
                ('DateOfExpiry', models.DateField(max_length=123)),
                ('PlaceOfIssue', models.CharField(max_length=123)),
            ],
        ),
    ]
