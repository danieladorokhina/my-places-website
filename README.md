# My Places Website

This project is a Django web application for a university lab assignment. It serves as a personal website to manage and display reviews of various places.

## Features

* **Homepage:** A feature that suggests a random place from the database.
* **Place List:** A page that displays all the places with their reviews.
* **Admin Panel:** An administrative interface to easily add, edit, and delete places.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or a newer version installed on your system.

### Installation

Follow these steps to get a copy of the project up and running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/my_places_website.git](https://github.com/your-username/my_places_website.git)
    cd my_places_website
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000/).
