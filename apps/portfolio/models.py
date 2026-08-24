from django.db import models


class Skill(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        unique=True,
        help_text="Enter the name of the skill. Example: Python, Django, Docker.",
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Experience(models.Model):
    role = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Enter your job role. Example: Senior Backend Developer.",
    )
    company = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Enter the company name. Example: Google.",
    )
    period = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Enter the employment period. Examples: 2022 - Present, 2020 - 2022.",
    )
    description = models.TextField(
        help_text="Describe your responsibilities, achievements, and work. Example: Developed and maintained web applications.",
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.role} - {self.company}"
