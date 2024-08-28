### Wimhome



## Installation

### Option 1 : Installation locale

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/princeGedeon/wimhome.git
    cd wimhome
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations et démarrez le serveur de développement :
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. Accédez à l'application via votre navigateur web à l'adresse `http://127.0.0.1:8000/`.

### Option 2 : Installation avec Docker

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/princeGedeon/wimhome.git
    cd wimhome
    ```

2. Construisez et démarrez les conteneurs Docker :
    ```bash
    docker-compose up --build
    ```

3. Appliquez les migrations :
    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Accédez à l'application via votre navigateur à l'adresse `http://localhost:8000/`.

## Arrêter les conteneurs Docker

Pour arrêter les conteneurs en cours d'exécution :
```bash
docker-compose down
```
