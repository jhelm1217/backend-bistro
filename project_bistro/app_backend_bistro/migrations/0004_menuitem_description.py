# Generated by Django 5.0.6 on 2024-05-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend_bistro', '0003_alter_menuitem_category_alter_menuitem_cuisine'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(default='coming soon'),
            preserve_default=False,
        ),
    ]
