# Generated by Django 4.0.4 on 2022-04-18 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('well_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone_number', models.TextField()),
                ('orders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='user.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('volume', models.FloatField()),
                ('consist', models.TextField()),
                ('consumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='user.consumer')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='count_of_products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='count_of_products', to='user.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='user.user'),
        ),
        migrations.CreateModel(
            name='DeliveryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('workers_list', models.ManyToManyField(blank=True, related_name='workers_list', to='user.deliveryman')),
            ],
        ),
        migrations.AddField(
            model_name='deliveryman',
            name='orders_list',
            field=models.ManyToManyField(blank=True, related_name='orders_list', to='user.order'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='user.product'),
        ),
    ]
