# My Places Website

This is a simple Django website to keep track of places I've visited.

---

### How to Run

1.  **Clone the code:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Set up the environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Set up the database:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

4.  **Start the server:**
    ```bash
    python manage.py runserver
    ```