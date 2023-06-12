# Generated by Django 3.2.19 on 2023-06-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("iq_eq_app", "0002_auto_20230612_2033"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="testuser",
            options={},
        ),
        migrations.RemoveField(
            model_name="testuser",
            name="created",
        ),
        migrations.AddField(
            model_name="testuser",
            name="eq_test_time",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="testuser",
            name="iq_test_time",
            field=models.DateTimeField(null=True),
        ),
    ]
