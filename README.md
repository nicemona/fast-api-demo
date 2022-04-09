# FastAPI demo 🤖

A demo repository for FastAPI

## Prerequisites

- PostgreSQL 13.x
- Python 3.8.x

---


### Run using cmd
```
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Run using docker
```
   docker-compose up -d
```

### By default project will be available on
   - API: [0.0.0.0:8000](http://0.0.0.0:8000)
   - Doc: [0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)


### If you would like to change DB user/password, just edit .env file
```
   DB_USER=xxx
   DB_PASSWORD=xxx
```