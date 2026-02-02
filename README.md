🚀 Django Scraper: Buscador de Empleo Automatizado

Este proyecto es una herramienta de Web Scraping integrada en el framework Django. Comencé creando un scraper básico para extraer títulos de una web personal y lo evolucioné hacia un sistema capaz de capturar ofertas de empleo reales de portales como Startup Jobs.
🎯 Objetivo del Proyecto

Aprender a integrar herramientas de automatización de navegación (Selenium) con un sistema de gestión de base de datos robusto (Django) para recolectar, procesar y almacenar información de la web de forma automática.
🛠️ Tecnologías Utilizadas

    Python 3.12 / 3.13: Lenguaje principal.

    Django 6.0: Framework para la estructura del proyecto y gestión de base de datos.

    Selenium: Biblioteca para la automatización del navegador y extracción de datos.

    Webdriver-manager: Para la gestión automática de los drivers de Chrome.

    SQLite: Base de datos ligera incluida en Django.

📂 Estructura del Proyecto (Puntos Clave)

    scraper/models.py: Define la estructura de la base de datos (nuestra tabla de empleos).

    scraper/services/scrape.py: El "corazón" del scraper. Aquí reside la lógica de navegación de Selenium.

    scraper/management/commands/scraper.py: El "interruptor". Permite ejecutar el scraper desde la consola mediante comandos de Django.

🚀 Instalación y Acceso

Sigue estos pasos para levantar el proyecto en tu entorno local (Linux):

    Clonar/Acceder a la carpeta:
    code Bash

cd webscraper

Activar el entorno virtual:
code Bash

source venv/bin/activate

Instalar dependencias:
code Bash

pip install -r requirements.txt

Preparar la base de datos:
code Bash

    cd webscraper_project
    python manage.py migrate

🤖 Cómo ejecutar el Scraper

Para activar el robot y que empiece a buscar empleos, ejecuta el siguiente comando personalizado en la terminal:
code Bash

python manage.py scraper

🖥️ Cómo ver los datos (Panel de Administración)

He configurado el Django Admin para poder visualizar los resultados de forma cómoda y visual:

    Crear un usuario de acceso:
    code Bash

python manage.py createsuperuser

(Sigue las instrucciones en consola para crear tu usuario).

Lanzar el servidor:
code Bash

python manage.py runserver

Acceder al panel:
Abre tu navegador en http://127.0.0.1:8000/admin e inicia sesión. En la sección "Jobs" verás todas las ofertas que el robot ha capturado.

📈 Evolución del Proyecto 
El cambio de rumbo

Originalmente, el proyecto estaba diseñado para extraer etiquetas <h1> genéricas de una web estática. Decidí llevarlo al siguiente nivel enfocándolo en un portal de empleo real (Startup Jobs).

¿Cómo lo hice?

    Rediseño de Modelos: Cambié el modelo inicial ScrapedData por uno llamado Job, añadiendo campos específicos como company (empresa) y url única para evitar ofertas duplicadas.

    Ingeniería de Selectores: Utilicé las herramientas de desarrollador de Chrome para identificar las clases CSS exactas de las tarjetas de empleo (div.job-card, h3, etc.).
