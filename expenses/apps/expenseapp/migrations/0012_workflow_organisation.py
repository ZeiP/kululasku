# Generated by Django 2.2.13 on 2021-01-18 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0011_auto_20210118_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='organisation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='expenseapp.Organisation'),
            preserve_default=False,
        ),
    ]
