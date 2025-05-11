# 🔗 URL Shortener API with Analytics

A simple backend API built using **FastAPI** that shortens long URLs and tracks click analytics.  
Inspired by services like Bitly.

## 📌 Features

- Generate short URLs for long links
- Track the number of clicks per short link
- Clean API with Swagger docs (`/docs`)
- Containerized with Docker
- (Optional) CI/CD with GitHub Actions

## 🚀 Endpoints

| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| POST   | `/shorten`           | Submit long URL → get short code  |
| GET    | `/{short_code}`      | Return original URL for redirection |
| GET    | `/analytics/{code}`  | View number of visits on short URL |

## 🧪 Example Request

```bash
curl -X POST http://127.0.0.1:8000/shorten \
 -H "Content-Type: application/json" \
 -d '{"original_url": "https://www.google.com"}'
