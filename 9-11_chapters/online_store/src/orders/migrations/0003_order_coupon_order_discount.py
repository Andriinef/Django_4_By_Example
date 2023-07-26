# Generated by Django 4.1.10 on 2023-07-19 14:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coupons", "0001_initial"),
        ("orders", "0002_order_stripe_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="coupons.coupon",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
