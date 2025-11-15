# dbt UI Setup Guide

## Steps to Access dbt Documentation UI

### 1. Initialize a dbt project (if not already done)
```bash
docker-compose exec dbt dbt init my_project
# Follow prompts to create the project
```

### 2. Navigate to your project directory
```bash
docker-compose exec dbt bash
cd my_project
```

### 3. Generate documentation
```bash
docker-compose exec dbt dbt docs generate
```

### 4. Serve the documentation UI
```bash
docker-compose exec dbt dbt docs serve --host 0.0.0.0 --port 8080
```

### 5. Access the UI
Open your browser to: http://localhost:8080

## Alternative: One-liner to serve docs
```bash
docker-compose exec dbt bash -c "cd my_project && dbt docs generate && dbt docs serve --host 0.0.0.0 --port 8080"
```

## What you'll see in the UI:
- **Lineage Graph**: Visual representation of your data models
- **Documentation**: Model descriptions, column details, and tests
- **Data Catalog**: Browse all your tables and views
- **Source Code**: View the SQL and YAML files

## Notes:
- The docs server runs in the foreground, so keep the terminal open
- Press Ctrl+C to stop the docs server
- Port 8080 is exposed in docker-compose.yml