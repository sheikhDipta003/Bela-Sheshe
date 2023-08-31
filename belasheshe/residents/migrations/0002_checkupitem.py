# Generated by Django 4.2.4 on 2023-08-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckupItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bloodpressure', models.CharField(max_length=20)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('heartrate', models.IntegerField()),
            ],
        ),
    ]