from django.db import models

from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(
        max_length=150,
        db_index=True,
        unique=True,
        help_text="Enter the project title. Example: Portfolio Website.",
    )
    description = models.TextField(
        help_text="Write a brief description of the project, including its purpose and key features.",
    )
    image = models.ImageField(
        upload_to="projects",
        help_text="Upload an image representing the project.",
    )
    external_url = models.URLField(
        help_text="Enter the external project URL. Example: https://www.your-site.com.",
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        help_text="Enter the post title. Example: Docker Basics for Developers.",
    )
    slug = models.SlugField(
        max_length=150,
        null=True,
        blank=True,
        db_index=True,
        help_text="Automatically generated from the title. Leave empty to generate it automatically.",
    )
    description = models.TextField(
        help_text="Write a short summary of the post. This text is used as the post preview.",
    )
    image = models.ImageField(
        upload_to="posts",
        help_text="Upload the cover image for the post.",
    )
    content_html = models.TextField(
        help_text=(
            "Enter the final rendered HTML content of the post. "
            "Example: &lt;h2&gt;Introduction&lt;/h2&gt;&lt;p&gt;Your content here...&lt;/p&gt;"
        )
    )
    published_date = models.DateField(
        help_text="Enter the date when the post should be published. Future dates will not be shown publicly.",
    )
    is_published = models.BooleanField(
        default=False,
        help_text="Enable this to make the post publicly available. Unpublished posts are hidden from the public API.",
    )

    class Meta:
        ordering = ["-published_date"]

    @property
    def read_time_minutes(self):
        return max(1, (len(self.description) + 199) // 200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
