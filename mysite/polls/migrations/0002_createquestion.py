# Generated by Django 3.1.3 on 2021-01-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='createQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('optionVote', models.CharField(max_length=100)),
                ('tagsget', models.CharField(max_length=200)),
            ],
        ),
    ]
