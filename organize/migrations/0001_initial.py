# Generated by Django 2.2 on 2019-05-12 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetID', models.CharField(max_length=250)),
                ('asset_name', models.CharField(max_length=250)),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskID', models.CharField(max_length=250)),
                ('task_name', models.CharField(max_length=250)),
                ('frequency', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerID', models.CharField(max_length=250)),
                ('worker_name', models.CharField(max_length=250)),
                ('worker_tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organize.Task')),
            ],
        ),
    ]
