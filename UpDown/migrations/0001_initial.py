# Generated by Django 3.0.5 on 2020-04-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_num', models.CharField(max_length=50, verbose_name='客户端号')),
                ('score', models.IntegerField(verbose_name='分数')),
            ],
        ),
    ]