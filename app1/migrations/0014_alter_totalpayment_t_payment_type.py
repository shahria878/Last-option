# Generated by Django 5.2 on 2025-05-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_delete_studentpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalpayment',
            name='t_payment_type',
            field=models.CharField(choices=[('Tuition(Mid Term)', 'Tuition(Mid Term)'), ('Tuition(Final)', 'Tuition(Final)'), ('Admission', 'Admission'), ('Registration', 'Registration'), ('Late Fee', 'Late Fee'), ('Retake Fee', 'Retake Fee'), ('Other', 'Other')], max_length=50),
        ),
    ]
