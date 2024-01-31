# Generated by Django 4.2.7 on 2024-01-31 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Running', 'Running')], default='Pending', max_length=10)),
                ('schedule_types', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=10)),
                ('description', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.availabletime')),
            ],
        ),
    ]
