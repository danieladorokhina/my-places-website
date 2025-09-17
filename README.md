# My Places Website

This is a simple website made with Django. It helps me keep track of places I've been and what I thought of them.

## How it works

- **Main page:** Just a button that picks a random place for me.
- **Places list:** Shows all the places I've added.
- **Admin page:** This is where I add new places and reviews.

## How to run it

1.  **Get the code:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Set up your Python environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install what you need:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    ```bash
    python manage.py migrate
    ```

5.  **Create an admin account:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the website:**
    ```bash
    python manage.py runserver
    ```

That's it! Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) to see the website.