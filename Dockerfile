# Utilise une image Python officielle
FROM python:3.12-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie les dépendances
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application
COPY app/ ./app/

# Expose le port 8000
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]