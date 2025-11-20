from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        labels = {
            "name": "Ism",
            "email": "Email",
            "message": "Xabar",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ismingiz"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email manzilingiz"}),
            "message": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Xabaringiz", "rows": 4}
            ),
        }
