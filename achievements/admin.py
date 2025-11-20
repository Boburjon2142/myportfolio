from django.contrib import admin

from .models import Achievement, ContactMessage, Skill, Tag, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "is_featured", "is_public")
    list_filter = ("category", "is_featured", "is_public", "date", "technologies", "tags")
    search_fields = ("title", "short_description", "organization", "location")
    autocomplete_fields = ("technologies", "tags")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-date",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level", "is_highlighted", "order")
    list_filter = ("category", "is_highlighted")
    search_fields = ("name", "category")
    ordering = ("order", "-level")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)
