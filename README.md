🧩 User API Project (Django REST Framework)

A clean, modular, and secure Django REST API for user management, authentication, filtering, and search.
This project was built using Django 5, Django REST Framework, and django-filter.

🚀 Features
✅ User Management

Register new users

Login with token authentication

Update profile

Delete account

🔐 Custom Permissions

Restrict access based on authenticated user

Prevent users from editing others’ data

🔎 Filtering & Search (Day 25)

Search users by username, email

Filter by is_active, date_joined, etc.

Built with django-filter

📦 API Endpoints
Method	Endpoint	Description
POST	/api/register/	Create a new user
POST	/api/login/	Obtain auth token
GET	/api/users/	List all users (with search & filter)
GET	/api/users/<id>/	Retrieve a user
PUT	/api/users/<id>/	Update
DELETE	/api/users/<id>/	Delete
🛠️ Technologies Used

Python 3.13

Django 5.2

Django REST Framework

Django Filter

SQLite3 (default DB)

📁 Project Structure
user_api_project/
│── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   ├── filters.py
│── user_api_project/
│   ├── settings.py
│   ├── urls.py
│── manage.py

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/banumariwan/user_api_project.git
cd user_api_project

2️⃣ Create virtual environment
python -m venv .venv

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Start the server
python manage.py runserver

🧪 Testing the API

You can test endpoints using:

Postman

cURL

Thunder Client

DRF’s browsable API (default)

🔍 Search & Filter Examples
Search by username:
/api/users/?search=banu

Filter by active users:
/api/users/?is_active=True

Combine:
/api/users/?search=mar&is_active=True

📜 License

This project is licensed under the MIT License.
