# Generated by Django 3.2.6 on 2021-09-29 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customertransaction_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customertransaction',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction', to='api.customer'),
        ),
    ]