from django import template

register = template.Library()

MONTHS_UZ = [
    "yanvar",
    "fevral",
    "mart",
    "aprel",
    "may",
    "iyun",
    "iyul",
    "avgust",
    "sentabr",
    "oktabr",
    "noyabr",
    "dekabr",
]


@register.filter
def uz_date(value):
    """Format date with Uzbek month names: '21 noyabr 2025'."""
    if not value:
        return ""
    try:
        month_name = MONTHS_UZ[value.month - 1]
        return f"{value.day} {month_name} {value.year}"
    except Exception:
        return value
