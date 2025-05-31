
```markdown
# 📝 Django ToDo App

A simple task management (ToDo) application built using Django and Bootstrap.
This app allows users to **create**, **view**, **update**, and **delete** tasks through a clean, responsive interface.

Visit my Todo App at https://django-projects-ed78.onrender.com

## 🚀 Features

- ✅ Add new tasks with title and description
- 🗂️ View all tasks
- ✏️ Edit/update existing tasks
- ❌ Delete tasks
- 🧾 CSRF-protected forms
- 💅 Styled with Bootstrap 5

````

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ManneUdayKiran/todo-app.git
   cd todo-app
````

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Visit the app in your browser:**

   ```
   http://127.0.0.1:8000/
   ```

## 🔐 Deployment Notes

If deploying to platforms like **Render**, make sure to:

* Set `ALLOWED_HOSTS` properly in `settings.py`
* Add your Render domain to `CSRF_TRUSTED_ORIGINS`
* Serve static files using `whitenoise` or similar method
* Ensure correct `STATICFILES_DIRS` and `STATIC_ROOT`

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy Coding! 🛠️

```

