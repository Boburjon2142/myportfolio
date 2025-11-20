import random
from datetime import date

from django.core.management.base import BaseCommand
from django.db import transaction

from achievements.models import Achievement, Skill, Tag, Technology


class Command(BaseCommand):
    help = "Demo ma'lumotlar bilan bazani to'ldiradi."

    TECHNOLOGIES = [
        "Python",
        "Django",
        "HTML5",
        "CSS3",
        "JavaScript",
        "Bootstrap",
        "SQLite",
        "AI",
        "REST",
        "Docker",
    ]

    TAGS = [
        "backend",
        "sertifikat",
        "tadqiqot",
        "web",
        "ma'lumotlar",
        "sun'iy-intellekt",
        "startap",
        "hackathon",
    ]

    ACHIEVEMENTS = [
        {
            "title": "Sun'iy intellekt asosida tibbiy tashxis platformasi",
            "category": "PROJECT",
            "short_description": "Rentgen tasvirlarini tahlil qiluvchi AI xizmati",
            "description": "Ko'p qatlamli neyron tarmoq yordamida tibbiy tasvirlarni tahlil qilish va shifokorlar uchun tavsiyalar beruvchi platforma ishlab chiqildi.",
            "date": date(2025, 3, 15),
            "location": "Toshkent",
            "organization": "MedTech Lab",
            "technologies": ["Python", "AI", "REST"],
            "tags": ["sun'iy-intellekt", "tadqiqot"],
            "is_featured": True,
            "external_link": "https://example.com/ai-diagnostic",
        },
        {
            "title": "Yevroosiyo bo'yicha eng yaxshi edtech startap mukofoti",
            "category": "AWARD",
            "short_description": "Onlayn ta'lim platformasi uchun xalqaro sovrin",
            "description": "Adaptive Learning algoritmi asosida shaxsiylashtirilgan dars rejalarini quruvchi startap loyihasi g'olib deb topildi.",
            "date": date(2024, 11, 2),
            "location": "Istanbul",
            "organization": "Eurasia Forum",
            "technologies": ["Python", "Django", "AI"],
            "tags": ["startap", "sun'iy-intellekt"],
            "is_featured": True,
            "external_link": "https://example.com/edtech-award",
        },
        {
            "title": "Cloud-native CRM tizimi",
            "category": "PROJECT",
            "short_description": "Savdo guruhlari uchun moslashuvchan platforma",
            "description": "Mikroxizmatlar arxitekturasi asosida qurilgan CRM tizimi biznes jarayonlarni avtomatlashtiradi.",
            "date": date(2024, 6, 21),
            "location": "Toshkent",
            "organization": "InnoSoft",
            "technologies": ["Python", "Django", "Docker", "REST"],
            "tags": ["web", "backend"],
            "is_featured": True,
            "external_link": "https://example.com/crm",
        },
        {
            "title": "Google Professional Cloud Architect sertifikati",
            "category": "CERTIFICATE",
            "short_description": "Bulut me'morchiligi bo'yicha muvaffaqiyatli sinov",
            "description": "Murakkab bulut tizimlari va xavfsizlik konfiguratsiyalarini loyihalash bo'yicha sertifikat olindi.",
            "date": date(2023, 9, 12),
            "organization": "Google",
            "technologies": ["Python", "Docker"],
            "tags": ["sertifikat", "backend"],
            "external_link": "https://example.com/google-cert",
        },
        {
            "title": "Yoshlar innovatsiyasi tanlovi g'olibi",
            "category": "COMPETITION",
            "short_description": "Elektron hukumat uchun avtomatlashtirilgan tizim",
            "description": "Davlat xizmatlari uchun tezkor murojaatlar oqimini tahlil qiluvchi tizim nomdor bo'ldi.",
            "date": date(2023, 5, 30),
            "location": "Toshkent",
            "organization": "Yoshlar agentligi",
            "technologies": ["Python", "SQLite", "Bootstrap"],
            "tags": ["hackathon", "web"],
            "external_link": "https://example.com/egov",
        },
        {
            "title": "Django asosida portfel platformasi",
            "category": "PROJECT",
            "short_description": "Talabalar uchun yutuqlarni boshqarish tizimi",
            "description": "Portfel oynasida yutuqlar, sertifikatlar va feedbacklarni boshqaruvchi responsive sayt.",
            "date": date(2022, 10, 18),
            "location": "Toshkent",
            "technologies": ["Django", "Bootstrap", "SQLite"],
            "tags": ["web", "backend"],
            "external_link": "https://example.com/portfolio",
        },
        {
            "title": "IEEE jurnalida maqola",
            "category": "PUBLICATION",
            "short_description": "Edge AI orqali IoT qurilmalarini himoyalash",
            "description": "Tahliliy maqola IoT xavfsizligi bo'yicha ilg'or metodlarni taklif etadi.",
            "date": date(2022, 3, 5),
            "organization": "IEEE",
            "technologies": ["AI", "Python"],
            "tags": ["tadqiqot", "sun'iy-intellekt"],
            "external_link": "https://example.com/ieee",
        },
        {
            "title": "ML DataOps pipeline",
            "category": "RESEARCH",
            "short_description": "Avtomatlashtirilgan ma'lumotlar ishlov berish jarayoni",
            "description": "Ma'lumotlar sifati nazorati va modellarga doimiy etkazib berishni avtomatlashtiruvchi pipeline.",
            "date": date(2021, 12, 9),
            "technologies": ["Python", "AI"],
            "tags": ["ma'lumotlar", "sun'iy-intellekt"],
            "external_link": "https://example.com/dataops",
        },
        {
            "title": "Frontend ustaxona kursi",
            "category": "EDUCATION",
            "short_description": "Bootstrap va zamonaviy UI texnologiyalari",
            "description": "Yangi boshlovchilar uchun 8 haftalik amaliy kurs o'tkazildi.",
            "date": date(2021, 4, 17),
            "location": "Samarqand",
            "technologies": ["HTML5", "CSS3", "Bootstrap", "JavaScript"],
            "tags": ["web"],
            "external_link": "https://example.com/frontend",
        },
        {
            "title": "Onlayn hackathon chempioni",
            "category": "COMPETITION",
            "short_description": "Pandemiya monitoring platformasi",
            "description": "Ijtimoiy tarmoqlardan to'plangan ma'lumotlar asosida monitoring qiluvchi panel ishlab chiqildi.",
            "date": date(2020, 8, 6),
            "technologies": ["Python", "Django", "JavaScript"],
            "tags": ["hackathon", "ma'lumotlar"],
            "external_link": "https://example.com/hackathon",
        },
        {
            "title": "Open-source jamoaga hissa",
            "category": "OTHER",
            "short_description": "Django uchun uzbekcha lokalizatsiya to'plami",
            "description": "UZ locale fayllarini kengaytirish va testlar bilan ta'minlash tashabbusi.",
            "date": date(2020, 2, 13),
            "technologies": ["Django"],
            "tags": ["backend"],
            "external_link": "https://example.com/oss",
        },
    ]

    SKILLS = [
        ("Backend", "Python"),
        ("Backend", "Django"),
        ("Frontend", "HTML5"),
        ("Frontend", "CSS3"),
        ("Frontend", "Bootstrap"),
        ("Frontend", "JavaScript"),
        ("Ma'lumotlar", "Pandas"),
        ("Ma'lumotlar", "NumPy"),
        ("Ma'lumotlar", "SQL"),
        ("DevOps", "Docker"),
        ("DevOps", "CI/CD"),
        ("Soft skills", "Jamoa boshqaruvi"),
        ("Soft skills", "Prezentatsiya"),
    ]

    def handle(self, *args, **options):
        random.seed(42)
        with transaction.atomic():
            tech_objects = {}
            for name in self.TECHNOLOGIES:
                tech, _ = Technology.objects.get_or_create(name=name, defaults={"slug": name.lower().replace(" ", "-")})
                tech_objects[name] = tech

            tag_objects = {}
            for name in self.TAGS:
                tag, _ = Tag.objects.get_or_create(name=name, defaults={"slug": name.lower().replace(" ", "-")})
                tag_objects[name] = tag

            for payload in self.ACHIEVEMENTS:
                technologies = payload.pop("technologies", [])
                tags = payload.pop("tags", [])
                achievement, _ = Achievement.objects.update_or_create(
                    title=payload["title"],
                    defaults={**payload, "short_description": payload["short_description"][:280]},
                )
                if technologies:
                    achievement.technologies.set([tech_objects[name] for name in technologies if name in tech_objects])
                if tags:
                    achievement.tags.set([tag_objects[name] for name in tags if name in tag_objects])

            for idx, (category, name) in enumerate(self.SKILLS, start=1):
                Skill.objects.update_or_create(
                    name=name,
                    defaults={
                        "category": category,
                        "level": random.randint(70, 100),
                        "is_highlighted": idx <= 6,
                        "order": idx,
                    },
                )

        self.stdout.write(self.style.SUCCESS("Demo ma'lumotlar muvaffaqiyatli yaratildi."))
