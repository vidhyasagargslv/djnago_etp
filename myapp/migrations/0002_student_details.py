# Generated by Django 5.0.1 on 2024-03-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fav_language', models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('c++', 'C++'), ('c#', 'C#'), ('javascript', 'javascript')], max_length=30)),
            ],
        ),
    ]
