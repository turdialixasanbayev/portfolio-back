# Portfolio Backend

A Django and Django REST Framework backend for a personal portfolio website. The
application stores portfolio content in a database, exposes public read-only API
endpoints for the frontend, and provides Django Admin for content management.

## Features

- Public versioned REST API under `/api/v1/`
- Portfolio skills and professional experience
- Projects with uploaded images and external links
- Blog posts with HTML content, cover images, publication dates, and calculated
	reading time
- Automatic hiding of unpublished and future-dated posts
- Django Admin interface for managing all dynamic content
- OpenAPI schema with Swagger UI and ReDoc
- Development serving for static and uploaded media files
- CORS configuration for a separately hosted frontend

The public API is intentionally read-only. The frontend does not create or
modify content through the API; administrators manage content through the
admin panel.

## Technology Stack

- Python 3.14.4
- Django 6.1
- Django REST Framework 3.18
- SQLite by default in the local environment, or any database supported by
	`django-environ` and the configured `DATABASE_URL`
- Pillow for image uploads
- `django-cors-headers` for cross-origin requests
- `drf-spectacular` and `drf-spectacular-sidecar` for API documentation
- `django-cleanup` for removing replaced or deleted media files

All pinned Python dependencies are listed in [requirements.txt](requirements.txt).

## Project Structure

```text
portfolio-back/
├── apps/
│   ├── common/                 Shared application configuration
│   ├── portfolio/              Skills and experience
│   │   ├── api/                List serializers and views
│   │   ├── migrations/
│   │   ├── models.py
│   │   └── urls.py
│   └── post/                   Projects and blog posts
│       ├── api/                Project and post API views/serializers
│       ├── migrations/
│       ├── models.py
│       └── urls.py
├── config/                     Django project settings and root URLs
├── media/                      User-uploaded project and post images
├── static/                     Source static assets, if present
├── staticfiles/                Collected static assets
├── manage.py
├── .env.example
└── requirements.txt
```

## Requirements

- Python 3.14 or a compatible Python version supported by the installed Django
	release
- `pip`
- A database configured through `DATABASE_URL`
- The frontend origin(s) listed in the CORS and CSRF environment variables

## Local Setup

1. Clone the repository and enter the project directory:

	 ```bash
	 git clone https://github.com/turdialixasanbayev/portfolio-back.git
	 cd portfolio-back
	 ```

2. Create and activate a virtual environment:

	 ```bash
	 python3 -m venv .venv
	 source .venv/bin/activate
	 ```

3. Install the dependencies:

	 ```bash
	 python -m pip install --upgrade pip
	 pip install -r requirements.txt
	 ```

4. Create the environment file:

	 ```bash
	 cp .env.example .env
	 ```

	 Replace the placeholder values in `.env`. A development configuration can
	 look like this:

	 ```dotenv
	 SECRET_KEY=replace-with-a-long-random-secret
	 DEBUG=True
	 ALLOWED_HOSTS=127.0.0.1,localhost
	 CORS_ALLOWED_ORIGINS=http://127.0.0.1:5500,http://localhost:5500
	 CSRF_TRUSTED_ORIGINS=http://127.0.0.1:5500,http://localhost:5500
	 DATABASE_URL=sqlite:///db.sqlite3
	 ```

	 Comma-separated values are expected for `ALLOWED_HOSTS`,
	 `CORS_ALLOWED_ORIGINS`, and `CSRF_TRUSTED_ORIGINS`. Do not commit real
	 secrets or production credentials.

5. Apply migrations:

	 ```bash
	 python manage.py migrate
	 ```

6. Create an administrator account:

	 ```bash
	 python manage.py createsuperuser
	 ```

7. Start the development server:

	 ```bash
	 python manage.py runserver
	 ```

The API is then available at `http://127.0.0.1:8000/api/v1/` and the admin
panel at `http://127.0.0.1:8000/portfolio-admin-panel/`.

## API

### General rules

- All public endpoints accept `GET` requests.
- Authentication is not required; the default permission is `AllowAny`.
- List endpoints return JSON.
- Skills, experiences, and projects are returned newest first by descending
	database ID.
- Uploaded image fields are serialized using the request context and normally
	appear as absolute media URLs.
- Posts are paginated with a page size of 5. Use the `page` query parameter to
	request another page.
- A missing post returns `404 Not Found` with the detail message `Not found.`.

### Endpoint reference

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/skills/` | List all skills |
| `GET` | `/api/v1/experiences/` | List all experience records |
| `GET` | `/api/v1/projects/` | List all projects |
| `GET` | `/api/v1/posts/` | List public blog posts |
| `GET` | `/api/v1/posts/<slug>/` | Retrieve one public post |
| `GET` | `/api/v1/schema/` | Download the OpenAPI schema |
| `GET` | `/api/v1/schema/swagger-ui/` | Browse the API with Swagger UI |
| `GET` | `/api/v1/schema/redoc/` | Browse the API with ReDoc |

Example request:

```bash
curl http://127.0.0.1:8000/api/v1/posts/
curl http://127.0.0.1:8000/api/v1/posts/docker-basics-for-developers/
```

### Response shapes

Skills:

```json
[
	{
		"id": 1,
		"title": "Django"
	}
]
```

Experience:

```json
[
	{
		"id": 1,
		"role": "Backend Developer",
		"company": "Example Company",
		"period": "2022 - Present",
		"description": "Developed and maintained web applications."
	}
]
```

Project:

```json
[
	{
		"id": 1,
		"title": "Portfolio Website",
		"description": "A personal portfolio website.",
		"image": "http://127.0.0.1:8000/media/projects/portfolio.jpg",
		"external_url": "https://example.com"
	}
]
```

Post detail:

```json
{
	"title": "Docker Basics for Developers",
	"slug": "docker-basics-for-developers",
	"description": "An introduction to containerized development.",
	"image": "http://127.0.0.1:8000/media/posts/docker.jpg",
	"published_date": "2026-01-15",
	"read_time_minutes": 1,
	"content_html": "<h2>Introduction</h2><p>Post content...</p>"
}
```

Post list responses use DRF page-number pagination:

```json
{
	"count": 1,
	"next": null,
	"previous": null,
	"results": []
}
```

### Post publishing rules

A post is included in the public list and detail endpoints only when:

- `is_published` is `true`
- `published_date` is today or earlier in the configured `Asia/Tashkent`
	timezone

If `slug` is left empty in Admin, it is generated from the post title when the
object is saved. The calculated `read_time_minutes` value is based on the
description length and is never lower than one minute:

```text
max(1, ceil(description_length / 200))
```

## Managing Content in Django Admin

1. Open `/portfolio-admin-panel/`.
2. Sign in with a superuser account.
3. Add or edit Skills, Experiences, Projects, and Posts.
4. Upload images to the appropriate model. Project images are stored under
	 `media/projects/`; post images are stored under `media/posts/`.
5. For posts, set the publication date and enable `is_published` when the post
	 should become public.

The admin provides search and filtering for the main content fields. Post
publication can also be changed directly from the post list view.

## Static Files and Media

During development, Django serves `/static/` and `/media/` when `DEBUG=True`.
For production, run:

```bash
python manage.py collectstatic --noinput
```

Configure the production web server to serve `STATIC_ROOT` and `MEDIA_ROOT`,
and use a production-grade WSGI or ASGI process instead of `runserver`.

## Useful Commands

```bash
# Check the Django project configuration
python manage.py check

# Create migrations after model changes
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Collect static assets for deployment
python manage.py collectstatic --noinput

# Open a Django shell
python manage.py shell
```

## Production Checklist

- Set `DEBUG=False`.
- Use a strong, private `SECRET_KEY`.
- Set `ALLOWED_HOSTS` to the real backend hostnames.
- Set `CORS_ALLOWED_ORIGINS` to only the trusted frontend origins.
- Set `CSRF_TRUSTED_ORIGINS` to the trusted origins that require CSRF support.
- Configure a production database through `DATABASE_URL`.
- Run migrations and `collectstatic` during deployment.
- Serve uploaded media from protected, intentional storage.
- Run Django’s deployment checks:

	```bash
	python manage.py check --deploy
	```

- Serve the application through HTTPS and a production WSGI/ASGI server.

## License

See [LICENSE](LICENSE) for the project license.
