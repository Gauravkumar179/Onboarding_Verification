# Generated by Django 4.0.1 on 2022-07-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0004_alter_user_aadhar_number_alter_user_bank_ifsc_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alternative_mobile_number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Divorce', 'Divorce'), ('Widow', 'Widow')], max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.IntegerField(max_length=10),
        ),
    ]