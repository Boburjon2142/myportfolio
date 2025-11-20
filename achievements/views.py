from collections import defaultdict

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Achievement, Skill, Technology


def home_view(request):
    featured = Achievement.objects.filter(is_public=True, is_featured=True)[:3]
    stats = {
        "total": Achievement.objects.filter(is_public=True).count(),
        "projects": Achievement.objects.filter(is_public=True, category="PROJECT").count(),
        "certificates": Achievement.objects.filter(is_public=True, category="CERTIFICATE").count(),
    }
    context = {
        "featured": featured,
        "stats": stats,
    }
    return render(request, "home.html", context)


def achievement_list_view(request):
    queryset = Achievement.objects.filter(is_public=True)
    search = request.GET.get("search")
    category = request.GET.get("category")
    year = request.GET.get("year")
    technology_slug = request.GET.get("technology")

    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) | Q(short_description__icontains=search) | Q(description__icontains=search)
        )
    if category:
        queryset = queryset.filter(category=category)
    if year:
        queryset = queryset.filter(date__year=year)
    if technology_slug:
        queryset = queryset.filter(technologies__slug=technology_slug)

    queryset = queryset.distinct()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    filters = {
        "search": search or "",
        "category": category or "",
        "year": year or "",
        "technology": technology_slug or "",
    }

    context = {
        "page_obj": page_obj,
        "filters": filters,
        "categories": Achievement.CATEGORY_CHOICES,
        "technologies": Technology.objects.all(),
        "years": Achievement.objects.filter(is_public=True)
        .dates("date", "year")
        .values_list("date__year", flat=True)
        .distinct()
        .order_by("-date__year"),
    }
    return render(request, "achievements/list.html", context)


def achievement_detail_view(request, slug):
    achievement = get_object_or_404(Achievement, slug=slug, is_public=True)
    related = (
        Achievement.objects.filter(is_public=True, technologies__in=achievement.technologies.all())
        .exclude(id=achievement.id)
        .distinct()[:3]
    )
    context = {
        "achievement": achievement,
        "related": related,
    }
    return render(request, "achievements/detail.html", context)


def timeline_view(request):
    achievements = Achievement.objects.filter(is_public=True).order_by("-date")
    grouped = defaultdict(list)
    for achievement in achievements:
        grouped[achievement.date.year].append(achievement)
    timeline = sorted(grouped.items(), key=lambda item: item[0], reverse=True)
    return render(request, "timeline.html", {"timeline": timeline})


def skills_view(request):
    skills = Skill.objects.all().order_by("order", "-level")
    grouped = defaultdict(list)
    for skill in skills:
        grouped[skill.category].append(skill)
    return render(
        request,
        "skills.html",
        {"skills_by_category": dict(grouped), "highlighted": skills.filter(is_highlighted=True)[:6]},
    )


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
