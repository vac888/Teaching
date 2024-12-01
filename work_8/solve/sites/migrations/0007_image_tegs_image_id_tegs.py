# Generated by Django 4.2.1 on 2024-11-29 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_delete_temp_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_tegs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sites.image')),
                ('teg_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sites.teg')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='id_tegs',
            field=models.ManyToManyField(through='sites.image_tegs', to='sites.teg'),
        ),
    ]
