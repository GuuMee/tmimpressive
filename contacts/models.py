from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=30)
    email = models.EmailField("Email", blank=True)
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка с сайта"
        verbose_name_plural = "Заявки с сайта"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.phone}"