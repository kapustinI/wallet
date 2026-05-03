# Practice Wallet API

Simple training backend built with FastAPI and PostgreSQL.

Features:
- create wallet
- get wallet balance
- add income
- add expense
- get total balance across all wallets

## Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL (Docker)
- Pydantic

## Project Structure

```text
app/
  api/v1/            # API routes
  service/           # business logic
  repository/        # DB access layer
  models.py          # ORM models
  schemas.py         # pydantic schemas
  db.py              # database connection
main.py              # app entrypoint
docker-compose.yml   # Postgres container
requirements.txt
```

## Quick Start

### 1) Clone repository

```bash
git clone <your-repo-url>
cd "practice wallet fastapi"
```

### 2) Create `.env` in project root

```env
POSTGRES_DB=wallet_db
POSTGRES_USER=wallet_user
POSTGRES_PASSWORD=wallet_pass
DATABASE_URL=postgresql+psycopg://wallet_user:wallet_pass@127.0.0.1:5432/wallet_db
```

### 3) Start PostgreSQL in Docker

```bash
docker compose up -d db
```

Check:

```bash
docker ps
```

### 4) Install Python dependencies

```bash
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 5) Run API

```bash
uvicorn main:app --reload
```

Swagger UI:

`http://127.0.0.1:8000/docs`

## API

Base prefix: `/api/v1`

### Create wallet

`POST /wallets`

```json
{
  "name": "main",
  "initial_balance": 1000
}
```

### Get balance

`GET /balance?wallet_name=main` - single wallet balance  
`GET /balance` - total balance

### Add income

`POST /operations/income`

```json
{
  "wallet_name": "main",
  "amount": 500,
  "description": "salary"
}
```

### Add expense

`POST /operations/expense`

```json
{
  "wallet_name": "main",
  "amount": 200,
  "description": "coffee"
}
```

## Useful Commands

Enter PostgreSQL in container:

```bash
docker exec -it wallet_postgres psql -U wallet_user -d wallet_db
```

Stop DB container:

```bash
docker compose stop db
```

Recreate local DB (deletes all local data):

```bash
docker compose down
docker volume rm postgress_data
docker compose up -d db
```

## Common Issues

### `DATABASE_URL is not set in .env file`

Add `DATABASE_URL` to root `.env` and restart app.

### `password authentication failed`

Most common reason: `.env` credentials changed after first DB init.
Recreate Docker volume or update DB user password manually.

### Port `5432` conflict

If local Windows PostgreSQL service is running, it may conflict with Docker Postgres.

Options:
- stop/remove local PostgreSQL service
- or change Docker mapping to `5433:5432` and update `DATABASE_URL`

## Next Improvements

- Alembic migrations
- tests
- operation history
- authentication
