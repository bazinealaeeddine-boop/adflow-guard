# AdFlow Guard

**Reliable server-side event proxy for ad platforms – clean, validated, unified.**

---

## The Problem
Marketers and agencies lose 20–40% of ad budget due to untrustworthy tracking data. Broken attribution, missing server-side events, tool sprawl, and garbage data make it impossible to trust ROAS numbers. Decisions are based on dirty data.

## The Solution
AdFlow Guard sits between your website and ad platforms (Facebook CAPI, Google Ads, TikTok Events). It acts as a **smart event proxy** that:

- ✅ **Validates** every incoming event against a strict schema.
- ✅ **Deduplicates** events (idempotency) so you never double-count.
- ✅ **Enriches** and normalizes data across platforms.
- ✅ **Fans-out** events to multiple platforms in parallel.
- ✅ **Monitors** and retries failures, giving you a single source of truth dashboard.

You send events once to a single endpoint – we handle the rest.

---

## Features (current MVP)

- `POST /api/v1/events` – ingest events with schema validation (Marshmallow)
- Async event processing with Celery and Redis
- Idempotency-ready architecture (event_id dedup)
- PostgreSQL for persistent event logs (coming: analytics)
- Fully containerized with Docker and Docker Compose

---

## Tech Stack

- **Backend:** Python, Flask
- **Task Queue:** Celery with Redis as broker
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Deployment:** AWS EC2 (planned), GitHub Actions

---

## Quick Start (Local)

Prerequisites: Docker and Docker Compose installed.

```bash
git clone https://github.com/bazinealaeeddine-boop/adflow-guard.git
cd adflow-guard
docker-compose up --build
```

Send a test event:

```bash
curl -X POST http://localhost:5000/api/v1/events \
  -H "Content-Type: application/json" \
  -d '{
    "events": [
      {
        "event_id": "test123",
        "event_name": "PageView",
        "user_data": {"ip": "1.1.1.1"},
        "platforms": ["facebook"]
      }
    ]
  }'
```

You should see "received": true and the Celery worker log Processing event....

---

Roadmap

· API Key authentication for clients
· Real integrations: Facebook CAPI, Google Ads API, TikTok Events
· Simple analytics dashboard (Flask + Chart.js)
· Webhook retry & dead-letter queue
· Self-serve onboarding & paid plans
· Deploy to AWS EC2 (free tier)

---

Why I'm Building This

I'm a beginner in DevOps learning by doing. This project is my hands-on journey to master Docker, Flask, Celery, and AWS while solving a real pain in digital marketing. I believe even a simple proxy can save thousands in wasted ad spend.

---

Let's Connect

· I'm sharing progress on LinkedIn;https://www.linkedin.com/in/alae-eddine-bazine-5730a13a6?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bpdw9X3dPR52p%2FFW3AGwx0Q%3D%3D and – follow along!
· Feedback, contributions, or just a chat? Open an issue or DM me.

---

Built with ❤️ in Morocco.

```