# Generated by Django 2.1 on 2018-08-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commandName', models.CharField(max_length=100)),
                ('param', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('familyName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parrotServer.Log'),
        ),
    ]
