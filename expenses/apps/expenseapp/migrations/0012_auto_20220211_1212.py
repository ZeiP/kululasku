# Generated by Django 3.2.12 on 2022-02-11 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0011_auto_20220210_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name_plural': ' Kululaskut'},
        ),
        migrations.AlterModelOptions(
            name='infomessage',
            options={'verbose_name_plural': ' Kululaskut'},
        ),
        migrations.AddField(
            model_name='infomessage',
            name='description_en',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='infomessage',
            name='description_fi',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Selite'),
        ),
        migrations.AddField(
            model_name='infomessage',
            name='description_se',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='InfoMessageTranslation',
        ),
    ]
