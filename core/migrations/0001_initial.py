# Generated by Django 4.2.5 on 2023-10-24 09:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Days",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="FoodItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="food_images/"),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_available", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ShoppingCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "shopping_cart_id",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("ip", models.GenericIPAddressField(blank=True, null=True)),
                (
                    "ip_location",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Ip Location",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=17, null=True
                    ),
                ),
                ("number_of_items", models.PositiveIntegerField(default=0)),
                ("is_current", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="TodaysSpecial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="core.days"
                    ),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.fooditem"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.shoppingcart",
                    ),
                ),
                (
                    "food_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.fooditem"
                    ),
                ),
            ],
        ),
    ]