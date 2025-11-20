from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=170, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ("EDUCATION", "Ta'lim"),
        ("CERTIFICATE", "Sertifikat"),
        ("PROJECT", "Loyiha"),
        ("COMPETITION", "Tanlov"),
        ("PUBLICATION", "Nashr"),
        ("AWARD", "Mukofot"),
        ("RESEARCH", "Tadqiqot"),
        ("OTHER", "Boshqa"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=280)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255, blank=True, default="")
    organization = models.CharField(max_length=255, blank=True, default="")
    technologies = models.ManyToManyField(Technology, related_name="achievements", blank=True)
    tags = models.ManyToManyField(Tag, related_name="achievements", blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    file = models.FileField(upload_to="files/", blank=True, null=True)
    external_link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Achievement.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=120)
    level = models.PositiveIntegerField()
    category = models.CharField(max_length=120)
    is_highlighted = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-level"]

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"
