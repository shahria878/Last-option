# Generated by Django 5.2 on 2025-04-26 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_courseregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregister',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='credits',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='section_name_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='semester',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='AdmitCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(blank=True, max_length=100, null=True)),
                ('exam', models.CharField(choices=[('Mid', 'Mid'), ('Final', 'Final')], max_length=20)),
                ('bill', models.CharField(choices=[('Paid', 'Paid'), ('Prepaid', 'Prepaid'), ('Unpaid', 'Unpaid'), ('Halfpaid', 'Halfpaid')], max_length=20)),
                ('cou_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_course_code', to='app1.courseregister')),
                ('cre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_credits', to='app1.courseregister')),
                ('prog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_program', to='app1.studentinfo')),
                ('seme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_semester', to='app1.courseregister')),
                ('sess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_session', to='app1.studentinfo')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_student', to='app1.student')),
                ('tit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admitcard_title', to='app1.courseregister')),
            ],
        ),
    ]
