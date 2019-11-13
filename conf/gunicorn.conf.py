from multiprocessing import cpu_count

# Server Socket
bind = "0.0.0.0:8000"  # Este tipo de sockets es más rápido que
# utilizando la interfaz local. Por lo que si el Nginx y el Gunicorn están en
# el mismo servidor es el que les recomiendo.
backlog = 2048

# Worker Processes
workers = cpu_count() * 2 + 1  # Valor recomendado por la doc oficial.
worker_class = 'gevent'  # Le decimos que utilice gevent para un mejor rendimiento.
worker_connections = 1000
max_requests = 0
keepalive = 5
timeout = 30

# Security
limit_request_line = 4096
limit_request_fields = 8190

# Server Mechanics
# pidfile = '/var/run/main_app.pid'
# user = 'nginx'
# group = 'nginx'

# Logging
loglevel = 'error'
accesslog = 'gunicorn_main_app.access.log'
errorlog = 'gunicorn_main_app.error.log'

# Process Naming
proc_name = 'main_app'
