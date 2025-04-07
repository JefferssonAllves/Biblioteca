import os

print("Variáveis de ambiente configuradas:")
for var in ['SECRET_KEY', 'ALLOWED_HOSTS', 'DEBUG', 'MYSQL_DATABASE', 'MYSQL_HOST']:
    print(f"{var}: {os.environ.get(var)}")