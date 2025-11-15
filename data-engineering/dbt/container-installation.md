# Container-Based dbt Installation Guide

## Overview

This guide provides instructions for setting up and running dbt (data build tool) using Docker containers, offering a consistent and isolated environment for your data transformation workflows.

## Prerequisites

- Docker installed and running
- Docker Compose (optional, for multi-service setups)
- Basic familiarity with dbt concepts

## Quick Start with Official dbt Docker Image

### 1. Pull the dbt Image

```bash
# Pull the latest dbt image with specific adapter
docker pull dbtlabs/dbt-postgres:1.7.latest
```

Available adapters:
- `dbt-postgres` - PostgreSQL
- `dbt-snowflake` - Snowflake
- `dbt-bigquery` - Google BigQuery
- `dbt-redshift` - Amazon Redshift

### 2. Basic Container Setup

```bash
# Create a dbt project directory
mkdir my-dbt-project
cd my-dbt-project

# Initialize dbt project using container
docker run --rm -v $(pwd):/usr/app -w /usr/app dbtlabs/dbt-postgres:1.7.latest dbt init my_project
```

### 3. Run dbt Commands

```bash
# Run dbt models
docker run --rm -v $(pwd):/usr/app -w /usr/app dbtlabs/dbt-postgres:1.7.latest dbt run

# Test models
docker run --rm -v $(pwd):/usr/app -w /usr/app dbtlabs/dbt-postgres:1.7.latest dbt test

# Generate documentation
docker run --rm -v $(pwd):/usr/app -w /usr/app dbtlabs/dbt-postgres:1.7.latest dbt docs generate
```

## Docker Compose Setup

Create a `docker-compose.yml` file for easier management:

```yaml
version: '3.8'

services:
  dbt:
    image: dbtlabs/dbt-postgres:1.7.latest
    volumes:
      - .:/usr/app
      - ~/.dbt:/root/.dbt  # Mount dbt profiles
    working_dir: /usr/app
    environment:
      - DBT_PROFILES_DIR=/root/.dbt
    command: tail -f /dev/null  # Keep container running
    
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: analytics
      POSTGRES_USER: dbt_user
      POSTGRES_PASSWORD: dbt_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Using Docker Compose

```bash
# Start services
docker-compose up -d

# Run dbt commands
docker-compose exec dbt dbt run
docker-compose exec dbt dbt test

# Stop services
docker-compose down
```

## Database Connection Examples

### PostgreSQL Configuration

Create `profiles.yml` in your project or `~/.dbt/` directory:

```yaml
my_project:
  outputs:
    dev:
      type: postgres
      host: postgres  # service name in docker-compose
      user: dbt_user
      password: dbt_password
      port: 5432
      dbname: analytics
      schema: public
      threads: 4
      keepalives_idle: 0
  target: dev
```

### Snowflake Configuration

```yaml
my_project:
  outputs:
    dev:
      type: snowflake
      account: your_account
      user: your_username
      password: your_password
      role: your_role
      database: your_database
      warehouse: your_warehouse
      schema: public
      threads: 4
  target: dev
```

### BigQuery Configuration

```yaml
my_project:
  outputs:
    dev:
      type: bigquery
      method: service-account
      keyfile: /path/to/service-account.json
      project: your_gcp_project
      dataset: your_dataset
      threads: 4
      timeout_seconds: 300
  target: dev
```

## Custom Dockerfile

For additional dependencies or configurations:

```dockerfile
FROM dbtlabs/dbt-postgres:1.7.latest

# Install additional packages
RUN pip install dbt-snowflake dbt-bigquery

# Copy custom profiles
COPY profiles.yml /root/.dbt/

# Set working directory
WORKDIR /usr/app

# Default command
CMD ["dbt", "run"]
```

Build and use:

```bash
docker build -t my-custom-dbt .
docker run --rm -v $(pwd):/usr/app my-custom-dbt
```

## Best Practices

### 1. Volume Mounting
- Mount your dbt project directory to `/usr/app`
- Mount profiles directory to preserve configurations
- Use named volumes for database data persistence

### 2. Environment Variables
```bash
# Pass environment variables for sensitive data
docker run --rm \
  -e DBT_PASSWORD=your_password \
  -e DBT_USER=your_user \
  -v $(pwd):/usr/app \
  dbtlabs/dbt-postgres:1.7.latest dbt run
```

### 3. Network Configuration
```yaml
# Use custom networks for service isolation
networks:
  dbt_network:
    driver: bridge
```

### 4. Resource Limits
```yaml
deploy:
  resources:
    limits:
      cpus: '2'
      memory: 2G
    reservations:
      memory: 1G
```

## Troubleshooting

### Common Issues

**Permission Errors**
```bash
# Fix file permissions
docker run --rm -v $(pwd):/usr/app -w /usr/app --user $(id -u):$(id -g) dbtlabs/dbt-postgres:1.7.latest dbt run
```

**Profile Not Found**
- Ensure `profiles.yml` is in the correct location
- Check `DBT_PROFILES_DIR` environment variable
- Verify profile name matches project name

**Connection Issues**
- Verify database service is running
- Check network connectivity between containers
- Validate connection parameters in profiles.yml

**Memory Issues**
```yaml
# Increase container memory limits
deploy:
  resources:
    limits:
      memory: 4G
```

### Debugging

```bash
# Run container interactively
docker run -it --rm -v $(pwd):/usr/app -w /usr/app dbtlabs/dbt-postgres:1.7.latest /bin/bash

# Check dbt version and installed adapters
dbt --version

# Debug connection
dbt debug

# View logs
docker-compose logs dbt
```

## Security Considerations

1. **Secrets Management**
   - Use environment variables for sensitive data
   - Consider using Docker secrets or external secret management
   - Avoid hardcoding credentials in Dockerfiles

2. **Network Security**
   - Use custom networks to isolate containers
   - Limit exposed ports
   - Implement proper firewall rules

3. **Image Security**
   - Use official dbt images
   - Regularly update base images
   - Scan images for vulnerabilities

## Performance Optimization

1. **Resource Allocation**
   - Set appropriate CPU and memory limits
   - Configure thread counts based on available resources

2. **Caching**
   - Use Docker layer caching for faster builds
   - Implement dbt artifact caching between runs

3. **Parallel Execution**
   - Leverage dbt's native parallelization
   - Scale horizontally with multiple containers if needed

## Monitoring and Logging

```yaml
# Add logging configuration to docker-compose.yml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

## Additional Resources

- [dbt Documentation](https://docs.getdbt.com/)
- [dbt Docker Hub](https://hub.docker.com/u/dbtlabs)
- [dbt Community Forum](https://discourse.getdbt.com/)
- [Docker Documentation](https://docs.docker.com/)