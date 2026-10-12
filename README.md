# 🛒 My Grocery Shop

A simple, responsive grocery price management web application built with Python Flask, SQLite, HTML, CSS, and JavaScript. It helps shopkeepers maintain grocery prices, calculate quantities for a customer's budget, and manage items from a single interface.

## ✨ Features

- **Grocery Price List:** View grocery names, prices, and measurements.
- **Quick Calculator:** Calculate the cost of a quantity or find the quantity a customer can buy for a given amount.
- **Live Search:** Find grocery items by name.
- **Add Items:** Add new products with prices and units.
- **Edit Items:** Update existing product details.
- **Delete Items:** Remove products from the list.
- **SQLite Database:** Store grocery item records locally.
- **Responsive Interface:** CSS styling designed to support desktop and mobile screens.

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and API |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layout |
| JavaScript | Search, calculator, and dynamic item management |
| Gunicorn | Production WSGI server |
| Render | Web hosting and deployment |

## 📂 Project Structure

```text
My_Grocery_Shop/
├── app.py
├── grocery.db
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Arnab2762/My_Grocery_Shop.git
cd My_Grocery_Shop
```

### 2. Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open your browser at:

http://127.0.0.1:5000

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/items` | Retrieve grocery items |
| POST | `/api/items` | Add a grocery item |
| PUT | `/api/items/<id>` | Update a grocery item |
| DELETE | `/api/items/<id>` | Delete a grocery item |

## 🌐 Deployment

This project can be deployed on [Render](https://render.com/) using the connected GitHub repository.

Suggested Render settings:

- **Runtime:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

After deployment, add your live website URL here:

**Live Demo:** [https://my-grocery-shop.onrender.com/]

### Database note

The application uses a local SQLite database file named `grocery.db`. On hosting platforms, local files may not persist across certain redeployments or instance replacements. For reliable production data storage, use a persistent disk or a managed database and configure the application accordingly.

## 🎯 Project Goals

This project demonstrates practical skills in:

- Building a web application using Flask.
- Connecting Python to an SQLite database.
- Creating REST-style API endpoints.
- Using JavaScript to update page content dynamically.
- Implementing CRUD operations.
- Organizing HTML templates and static CSS files.
- Preparing a Python application for deployment.

## 🔮 Future Improvements

- User authentication and role-based access.
- Product categories and stock management.
- Sales history and printable receipts.
- Input validation and clearer error messages.
- Persistent production database configuration.
- Further accessibility and mobile usability improvements.

## 👨‍💻 Author

**Arnab Sadhukhan**

BCA Student | Aspiring Software Developer

- GitHub: [@Arnab2762](https://github.com/Arnab2762)

## 📄 License

This project is available for learning and personal portfolio use. Add a LICENSE file if you want to specify formal reuse and distribution terms.

---

⭐ If you find this project useful, consider starring the repository!
