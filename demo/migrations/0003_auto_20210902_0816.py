# Generated by Django 3.2.6 on 2021-09-02 08:16

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0002_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Domain",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name="userprofile",
            name="domain_roles",
            field=jsonfield.fields.JSONField(default="{}"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprofile",
            name="current_domain",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="demo.domain"
            ),
        ),
    ]