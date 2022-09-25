# Task Queue Django

Django qpplication to demonstrate running async background tasks from Django Views, using DB based queue and cron.

 ## Docker Services
 - **APIs**: Service providing interface to user for creating and getting statuses of task. For API documentations kindly refer to swagger.yaml.
 - **DB**: Postgres database service.
 - **Executer**: Service for running cron using Django management command (**python manage.py execute**), looks for new tasks on database after and interval and executes them asynchronously.
 - **Nginx**: Used as reverse proxy for the API service.

 ## Environment Variables
- **DB_NAME**: Database name
-  **DB_USER**: Database username
- **DB_PASSWORD**: Database password
- **DB_HOST**: Database host
- **DB_PORT**: Database port
- **MAX_TIMEOUT_SEC**: Maximum time for that a async task can be executed (timeout)
- **ALLOWED_HOSTS**: Django configuration to control allowed hosts
- **CSRF_TRUSTED_ORIGINS**: Django CSRF trusted origins.
- **DEBUG**: Flag to control execution mode (runs in release mode if set to false)


 ## Running
 Docker compose file has been defined for hooking up application services, use  `docker compose up` command to run.

Before running the application above mentioned environment variables are required to be defined in `.env` file.

 ## Testing
 In order to run test cases use  `docker compose -f docker-compose-test.yml up --exit-code-from test-service` command.