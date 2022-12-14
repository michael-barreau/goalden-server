# Generated by Django 4.1 on 2022-09-06 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_frequency', models.CharField(max_length=55)),
                ('is_complete', models.BooleanField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goaldenapi.goal')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goaldenapi.member')),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goaldenapi.member'),
        ),
        migrations.AddField(
            model_name='goal',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goaldenapi.goaltype'),
        ),
    ]
