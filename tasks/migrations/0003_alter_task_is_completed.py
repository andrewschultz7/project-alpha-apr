# Generated by Django 4.1.2 on 2022-10-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_task_assignee_alter_task_is_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]
