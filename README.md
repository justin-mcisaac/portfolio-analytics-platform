# Portfolio Analytics Platform

A full-stack web application for recording stock and ETF transactions, tracking portfolio value, and analyzing investment performance.

## Project Goals

This project demonstrates full-stack software development through:

- A React and TypeScript frontend
- A Python and FastAPI REST API
- PostgreSQL data persistence
- Historical market-data integration
- Quantitative portfolio analytics
- Automated testing and continuous integration

## Planned Features

- Create and manage investment portfolios
- Record stock and ETF transactions
- Derive current holdings from transaction history
- Retrieve and cache historical market prices
- Track portfolio value over time
- Calculate return, volatility, Sharpe ratio, and maximum drawdown
- Visualize asset allocation and historical performance
- Compare portfolio performance against a benchmark

## Technology Stack

### Frontend

- React
- TypeScript
- Vite

### Backend

- Python
- FastAPI

### Database

- PostgreSQL

### Planned Analytics and Testing

- Pandas and NumPy
- pytest
- Vitest and React Testing Library

## Current Status

The backend foundation currently includes:

- React and TypeScript frontend
- FastAPI REST API
- PostgreSQL development database
- SQLAlchemy database connection
- Alembic database migrations
- Initial portfolio model
- Database-aware health endpoint
- Automated backend integration test

## Local Development

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at `http://localhost:5173`.

### Backend

```bash
cd backend
source .venv/bin/activate
python3 -m pip install -r requirements.txt
fastapi dev app/main.py
```

The backend runs at `http://127.0.0.1:8000`.

API documentation is available at `http://127.0.0.1:8000/docs`.
### Database

Start PostgreSQL from the project root:

```bash
docker compose up -d
```

Check its status:

```bash
docker compose ps
```

Stop PostgreSQL without deleting its data:

```bash
docker compose down
```

### Database Migrations

Run migration commands from the `backend` directory with the Python virtual environment active.

Apply all migrations:

```bash
alembic upgrade head
```

Check the current revision:

```bash
alembic current
```

Generate a migration after changing the database models:

```bash
alembic revision --autogenerate -m "describe the schema change"
```

### Backend Tests

With PostgreSQL running:

```bash
cd backend
source .venv/bin/activate
pytest -v
```
## Project Structure

```text
portfolio-analytics-platform/
├── backend/      # FastAPI application
├── frontend/     # React and TypeScript application
└── docs/         # Architecture notes and screenshots
```

## Roadmap

The first release will focus on portfolio management, transactions, holdings, historical prices, performance analytics, data visualization, testing, and deployment.