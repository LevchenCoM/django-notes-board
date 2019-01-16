# Generated by Django 2.1.5 on 2019-01-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.CharField(choices=[('0', 'To do'), ('1', 'In progress'), ('2', 'Done')], default='0', max_length=1),
        ),
    ]
