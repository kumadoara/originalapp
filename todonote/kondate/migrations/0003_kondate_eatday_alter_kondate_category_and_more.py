# Generated by Django 4.2.7 on 2023-12-04 01:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kondate', '0002_kondate_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='kondate',
            name='eatday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='食事日'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kondate',
            name='category',
            field=models.CharField(choices=[('Monday', '月曜日'), ('Tuesday', '火曜日'), ('Wednesday', '水曜日'), ('Thursday', '木曜日'), ('Friday', '金曜日'), ('Saturday', '土曜日'), ('Sunday', '日曜日')], max_length=30),
        ),
        migrations.AlterField(
            model_name='kondate',
            name='created',
            field=models.DateTimeField(verbose_name='記録日時'),
        ),
    ]