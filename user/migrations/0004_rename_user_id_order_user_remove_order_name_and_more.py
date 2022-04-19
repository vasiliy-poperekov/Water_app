# Generated by Django 4.0.4 on 2022-04-18 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_orders_user_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='count_of_products', to='user.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='count_of_products',
            field=models.IntegerField(),
        ),
    ]
