import os

# Configurações Django
os.environ['SECRET_KEY'] = 'a1c87dacccecc1589a0ed6b5415972fb830f50b6e2a192e17d31a423fa4069a9'
os.environ['ALLOWED_HOSTS'] = '127.0.0.1,localhost'
os.environ['DEBUG'] = 'True'

# Configurações MySQL
os.environ['MYSQL_ROOT_PASSWORD'] = '123456789'
os.environ['MYSQL_ROOT_HOST'] = '%'
os.environ['MYSQL_DATABASE'] = 'biblioteca'
os.environ['MYSQL_USER'] = 'jeff'
os.environ['MYSQL_PASSWORD'] = '123'
os.environ['MYSQL_HOST'] = 'db'
os.environ['MYSQL_PORT'] = '3306'

# Banco de Dados Django
os.environ['DB_ENGINE'] = 'django.db.backends.mysql'

# Verificação (opcional) - mostra as variáveis criadas
print("Variáveis de ambiente configuradas:")
for var in ['SECRET_KEY', 'ALLOWED_HOSTS', 'DEBUG', 'MYSQL_DATABASE', 'MYSQL_HOST']:
    print(f"{var}: {os.environ.get(var)}")

while True:
  pass