<div align="center">

# 📰 Django Blog

**A full-featured blog built with Django: authentication, articles with categories, nested comments, likes, a contact/ticket system and image uploads.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

</div>

---

## ✨ Features

- 🔐 **Authentication** - register, login, logout and edit profile.
- 📝 **Articles (CRUD)** - title, body, image, slug, publish status, multiple categories.
- 🗂️ **Categories** and category pages, plus 🔎 **search**.
- 💬 **Comments** with replies (self-referencing parent comments).
- ❤️ **Likes** on articles.
- 🎫 **Contact / ticket system** - visitors send messages; staff can list and delete them.
- 🖼️ **Image handling** for articles and profiles.
- 🧰 Uses both **class-based and function-based views**, and a **context processor** for shared template data.

## 🧩 Apps

| App | Responsibility |
|---|---|
| `account` | Profile model, login / register / logout / edit |
| `post_app` | Articles, categories, comments, likes, search, contact messages |
| `home_app` | Home page and sidebar partial |
| `context_processors` | Data available in every template |

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/django_first_Weblog.git
cd django_first_Weblog

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install django pillow django-browser-reload

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and manage content at `/admin/`.

## 🔗 Main routes

| Route | Purpose |
|---|---|
| `/` | Home |
| `/login`, `/register`, `/logout`, `/edit` | Account |
| `/articles/list` | All articles |
| `/articles/detail/<slug>` | Article detail with comments |
| `/articles/category/<id>` | Articles in a category |
| `/articles/search/` | Search |
| `/articles/contactus/` | Contact form |
| `/articles/like/<slug>/<id>` | Like an article |

## 📁 Project Structure

```
.
├── manage.py
├── blog_app/           # Project settings and root URLs
├── account/            # Users and profiles
├── post_app/           # Articles, comments, likes, tickets
├── home_app/           # Landing page
├── context_processors/
├── templates/  assets/ media/
└── LICENSE
```

## 🛠️ Tech Stack

`Python` · `Django` · `Bootstrap` · `SQLite` · `Pillow`
