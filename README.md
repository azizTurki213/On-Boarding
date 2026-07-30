# ID/Passport Onboarding Platform

Scans Tunisian CIN and passport documents during onboarding and extracts data via
an AI/OCR microservice. See the project roadmap for the full phase-by-phase plan.

## Layout

```
backend/       Spring Boot API (auth, onboarding sessions, persistence)
ai-service/    Python FastAPI microservice (OCR/extraction - currently stubbed)
frontend/      Angular app (capture UI, review screen, admin dashboard)
docker-compose.yml
```

## Current status (end of Phase 1)

- Backend: entities (`User`, `OnboardingSession`, `ExtractedDocument`), JWT auth
  (`/api/auth/register`, `/api/auth/login`), session lifecycle endpoints
  (`/api/onboarding/sessions`) with consent tracking. Document upload/extraction
  wiring is NOT yet implemented (Phase 2/3).
- AI service: FastAPI skeleton with `/health`, `/extract/passport`, `/extract/cin`.
  Both extraction endpoints currently return **stub data** - real OpenCV/OCR/MRZ
  logic is the Phase 2 (passport) and Phase 3 (CIN) work.
- Frontend: Angular 18 app scaffolded, `AuthService` + JWT interceptor wired up
  against the backend. No screens built yet - that starts around Phase 5/6.

## Running everything locally

### Option A: Docker Compose (backend + ai-service + db)
```bash
docker compose up --build
```
- Backend: http://localhost:8080 (Swagger UI at `/swagger-ui.html`)
- AI service: http://localhost:8000 (interactive docs at `/docs`)
- Postgres: localhost:5432 (db `onboarding` / user `onboarding` / pass `onboarding`)

### Option B: Run services individually (better for active development)

**Backend** (needs your own Maven/JDK 21 setup - this sandbox couldn't reach Maven
Central to verify the build, so do a first `mvn clean install` locally to confirm):
```bash
cd backend
mvn spring-boot:run
```

**AI service:**
```bash
cd ai-service
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install   # already done once in this scaffold, re-run if you re-clone
npm start     # serves on http://localhost:4200
```

## Before you write any real code

1. Set a real `JWT_SECRET` (don't commit it - use an env var or `.env` file).
2. Decide your document-image retention policy (see `rawImagePath` note in
   `ExtractedDocument.java`) before you start persisting real captured images.
3. Only use your own ID / consenting family members' documents for test data -
   never scrape or reuse other people's real ID photos.

## Next steps (Phase 2 of the roadmap)

Build the real passport MRZ pipeline in `ai-service/app/routers/passport.py`:
OpenCV crop of the MRZ region -> Tesseract/PassportEye OCR -> `mrz` library for
field parsing + check-digit validation.
