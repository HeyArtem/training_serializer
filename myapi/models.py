from django.db import models


class Hero(models.Model):
    name = models.CharField(
        verbose_name="Имя", max_length=60, blank=False, null=False, unique=True
    )

    alias = models.CharField(
        verbose_name="Прозвище",
        max_length=60,
        blank=False,
        null=False,
        unique=True,
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
        null=False,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
        null=False,
    )
    content = models.TextField(
        verbose_name="Oписание", blank=False, null=False, unique=True
    )

    class Meta:
        verbose_name = "Герой"
        verbose_name_plural = "Герои"

    # def save(self, *args, **kwargs):
    #     """Переопределяю т.к создание дефолтного alias"""
    #     if not self.alias:
    #         self.alias = default_alias(self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name
