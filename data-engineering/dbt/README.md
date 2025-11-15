# dbt Docker Setup

## Complete Setup Guide

### 1. Start the services
```bash
docker-compose up -d
```

### 2. Create dbt project
```bash
docker-compose exec dbt dbt init my_project
```

**During setup, configure:**
- Database: Select `1` for postgres
- Host: Enter `postgres` (not localhost)
- Port: Press Enter for default `5432`
- User: Enter `dbt_user`
- Password: Enter `dbt_password`
- Database name: Enter `analytics`
- Schema: Enter `public`
- Threads: Enter `2`

### 3. Test connection
```bash
docker-compose exec dbt bash -c "cd my_project && dbt debug"
```

### 4. Run dbt models
```bash
docker-compose exec dbt bash -c "cd my_project && dbt run"
```

### 5. Start dbt documentation UI
```bash
docker-compose exec dbt bash -c "cd my_project && dbt docs generate && dbt docs serve --host 0.0.0.0 --port 8080"
```

**Access the UI:** http://localhost:8080

### Additional Commands

**Test models:**
```bash
docker-compose exec dbt bash -c "cd my_project && dbt test"
```

**Access PostgreSQL directly:**
```bash
docker-compose exec postgres psql -U dbt_user -d analytics
```

**Stop services:**
```bash
docker-compose down
```

## Services

- **PostgreSQL**: Database running on port 5432
  - Database: `analytics`
  - User: `dbt_user`
  - Password: `dbt_password`

- **dbt**: Container with dbt-postgres adapter
  - Profiles configured to connect to PostgreSQL service

## Files

- `docker-compose.yml`: Service definitions
- `profiles.yml`: dbt database connection configuration
- `container-installation.md`: Comprehensive installation guide