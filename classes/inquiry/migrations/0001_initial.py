# Generated by Django 3.1.3 on 2020-11-18 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inquiry_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('st_name', models.CharField(max_length=40)),
                ('area', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=20)),
                ('mob', models.CharField(max_length=10)),
                ('landline', models.CharField(max_length=8)),
                ('collage', models.CharField(max_length=40)),
                ('ref_name', models.CharField(max_length=20)),
                ('remarks', models.TextField()),
                ('inquiry_by', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=20)),
                ('demolec_date', models.DateField()),
                ('demolec_time', models.CharField(max_length=20)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_students', to='course.course_table')),
            ],
        ),
    ]