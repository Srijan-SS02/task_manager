# Generated by Django 4.1.4 on 2022-12-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mytask', '0002_delete_newtask'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
            ],
        ),
    ]
