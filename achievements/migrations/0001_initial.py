from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("level", models.PositiveIntegerField()),
                ("category", models.CharField(max_length=120)),
                ("is_highlighted", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"ordering": ["order", "-level"]},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=120, unique=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Technology",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, unique=True)),
                ("slug", models.SlugField(max_length=170, unique=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Achievement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                ("category", models.CharField(
                    choices=[
                        ("EDUCATION", "Ta'lim"),
                        ("CERTIFICATE", "Sertifikat"),
                        ("PROJECT", "Loyiha"),
                        ("COMPETITION", "Tanlov"),
                        ("PUBLICATION", "Nashr"),
                        ("AWARD", "Mukofot"),
                        ("RESEARCH", "Tadqiqot"),
                        ("OTHER", "Boshqa"),
                    ],
                    max_length=20,
                )),
                ("short_description", models.CharField(max_length=280)),
                ("description", models.TextField()),
                ("date", models.DateField()),
                ("location", models.CharField(blank=True, default="", max_length=255)),
                ("organization", models.CharField(blank=True, default="", max_length=255)),
                ("image", models.ImageField(blank=True, null=True, upload_to="images/")),
                ("file", models.FileField(blank=True, null=True, upload_to="files/")),
                ("external_link", models.URLField(blank=True)),
                ("is_featured", models.BooleanField(default=False)),
                ("is_public", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "tags",
                    models.ManyToManyField(blank=True, related_name="achievements", to="achievements.tag"),
                ),
                (
                    "technologies",
                    models.ManyToManyField(blank=True, related_name="achievements", to="achievements.technology"),
                ),
            ],
            options={"ordering": ["-date", "-created_at"]},
        ),
    ]
