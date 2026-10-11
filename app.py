import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_NAME = "grocery.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                unit TEXT NOT NULL
            )
        """)
        # Seed default items if empty
        cursor = conn.execute("SELECT COUNT(*) FROM items")
        if cursor.fetchone()[0] == 0:
            defaults = [
                ("Basmati Rice", "₹90", "1 Kg"),
                ("Mustard Oil", "₹145", "1 Litre"),
                ("Sugar", "₹42", "1 Kg"),
                ("Toor Dal", "₹160", "1 Kg"),
                ("Salt (Tata)", "₹28", "1 Packet (1 Kg)"),
                ("Wheat Flour (Atta)", "₹210", "5 Kg"),
                ("Turmeric Powder", "₹35", "100 gm"),
                ("Eggs", "₹72", "1 Dozen (12 pcs)")
            ]
            conn.executemany("INSERT INTO items (name, price, unit) VALUES (?, ?, ?)", defaults)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM items ORDER BY id DESC").fetchall()
        return jsonify([dict(row) for row in rows])

@app.route("/api/items", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data.get("name", "").strip()
    price = data.get("price", "").strip()
    unit = data.get("unit", "").strip()

    if not price.startswith("₹"):
        price = "₹" + price

    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO items (name, price, unit) VALUES (?, ?, ?)",
            (name, price, unit)
        )
        conn.commit()
        return jsonify({"id": cursor.lastrowid, "name": name, "price": price, "unit": unit}), 201

@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    name = data.get("name", "").strip()
    price = data.get("price", "").strip()
    unit = data.get("unit", "").strip()

    if not price.startswith("₹"):
        price = "₹" + price

    with get_db() as conn:
        conn.execute(
            "UPDATE items SET name = ?, price = ?, unit = ? WHERE id = ?",
            (name, price, unit, item_id)
        )
        conn.commit()
        return jsonify({"id": item_id, "name": name, "price": price, "unit": unit})

@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    with get_db() as conn:
        conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        return jsonify({"success": True})

if __name__ == "__main__":
    init_db()
    # Accessible locally and across your shop Wi-Fi network
    app.run(host="0.0.0.0", port=5000, debug=True)