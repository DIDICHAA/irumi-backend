# Generated by Django 4.2.5 on 2023-09-19 17:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lantern",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "nickname",
                    models.CharField(
                        help_text="공백없이 닉네임을 입력해주세요.",
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[^\\s]{1,10}$", "공백없이 닉네임을 입력해주세요."
                            )
                        ],
                    ),
                ),
                ("content", models.TextField(max_length=100)),
                (
                    "password",
                    models.CharField(
                        help_text="네 자리 숫자를 입력해주세요.",
                        max_length=4,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\d{4}$", "네 자리 숫자를 입력해주세요."
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LanternReaction",
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
                    "reaction",
                    models.CharField(
                        choices=[("like", "Like"), ("dislike", "Dislike")],
                        max_length=10,
                    ),
                ),
                ("user_id", models.CharField(max_length=36)),
                (
                    "lantern",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reactions",
                        to="lantern.lantern",
                    ),
                ),
            ],
        ),
    ]
