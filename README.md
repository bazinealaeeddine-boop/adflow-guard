\# AdFlow Guard (Working Name)



\*\*Reliable server-side event proxy for ad platforms – clean, validated, unified.\*\*



\---



\## The Problem



Marketers and agencies lose 20–40% of ad budget due to untrustworthy tracking data. Broken attribution, missing server-side events, tool sprawl, and garbage data make it impossible to trust ROAS numbers. Decisions are based on dirty data.



\## The Solution



AdFlow Guard sits between your website and ad platforms (Facebook CAPI, Google Ads, TikTok Events). It acts as a \*\*smart event proxy\*\* that:



\- ✅ \*\*Validates\*\* every incoming event against a strict schema.

\- ✅ \*\*Deduplicates\*\* events (idempotency) so you never double-count.

\- ✅ \*\*Enriches\*\* and normalizes data across platforms.

\- ✅ \*\*Fans-out\*\* events to multiple platforms in parallel.

\- ✅ \*\*Monitors\*\* and retries failures, giving you a single source of truth dashboard.



You send events once to a single endpoint – we handle the rest.



\---



\## Features (current MVP)



\- `POST /api/v1/events` – ingest events with schema validation (Marshmallow)

\- Async event processing with Celery and Redis

\- Idempotency-ready architecture (event\_id dedup)

\- PostgreSQL for persistent event logs (coming: analytics)

\- Fully containerized with Docker and Docker Compose



\---



\## Tech Stack



\- \*\*Backend:\*\* Python, Flask

\- \*\*Task Queue:\*\* Celery with Redis as broker

\- \*\*Database:\*\* PostgreSQL

\- \*\*Containerization:\*\* Docker, Docker Compose

\- \*\*Deployment:\*\* AWS EC2 (planned), GitHub Actions



\---



\## Quick Start (Local)



Prerequisites: Docker and Docker Compose installed.



```bash

git clone https://github.com/bazinealaeeddine-boop/adflow-guard.git

cd adflow-guard

docker-compose up --build

