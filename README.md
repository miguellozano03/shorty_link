# Shorty.Link 🚀

Shorty.Link is a URL shortener service that allows you to shorten a URL without registration.

---

## 🛠 Technologies

<span>

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
  ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) 
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white) 
  ![Render](https://img.shields.io/badge/Render-ffffff?style=for-the-badge&logo=render&logoColor=black) 
  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) 
  ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) 
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

</span>

---

## ⚡ Functionalities

- Shorten URLs quickly and easily
- Redirect to the original URL
- Optional: Custom short links
- Optional: Click statistics

---

## 🚀 Installation


```bash
git clone https://github.com/tu-usuario/shorty-link.git
cd shorty-link
python -m venv venv
source venv/bin/activate
cd shorty_link
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Note:** Create a database and configure the .env file:

```dotenv
DJANGO_SECRET_KEY= 
DEBUG=True
HOSTS=

#PREFIX FOR URL SHORTENER SERVICE
PREFIX=localhost:8000

#DATABASE CONFIG
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

Try the service [here](https://shorty-link.onrender.com/)