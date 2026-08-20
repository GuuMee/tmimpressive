from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ваше имя",
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "+993 __ __-__-__",
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "email@example.com (необязательно)",
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition",
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Ваше сообщение...",
                "rows": 4,
                "class": "w-full px-4 py-3 rounded-xl border border-gray-300 focus:border-teal focus:ring-2 focus:ring-teal/30 outline-none transition resize-none",
            }),
        }