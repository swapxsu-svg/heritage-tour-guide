from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from dotenv import load_dotenv
from groq import Groq
 
load_dotenv()
 
app = Flask(__name__)
 
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
 
MODEL_NAME = "llama-3.3-70b-versatile"
 
 
# ==========================
# DATABASE CONNECTION
# ==========================
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
 
 
# ==========================
# HOME PAGE (Leaflet map)
# ==========================
@app.route("/")
def home():
    return render_template("home.html")
 
 
@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/metro_map")
def metro_map():
    return render_template("metro_map.html")
 
 
# ==========================
# API ENDPOINT FOR MONUMENTS
# ==========================
@app.route("/api/monuments")
def monuments_api():
 
    conn = get_db()
    c = conn.cursor()
 
    c.execute("""
        SELECT
            id,
            name,        hi_name,
            lat,         lon,
            color,
            image_url,
            history,     hi_history,
            secondary,   hi_secondary,
            visitor,     hi_visitor,
            experience,  hi_experience,
            nearby,      hi_nearby,
            condition,   hi_condition,
            translation, hi_translation
        FROM monuments
    """)
 
    rows = c.fetchall()
    conn.close()
 
    monuments = []
 
    for row in rows:
 
        images = []
        if row["image_url"]:
            images = [u.strip() for u in row["image_url"].split(",")]
 
        monuments.append({
 
            "id":       row["id"],
 
            # Names
            "name":     row["name"],
            "hi_name":  row["hi_name"] or row["name"],
 
            # Coordinates — both lat/lon AND lat/lng so frontend works either way
            "lat":      float(row["lat"]),
            "lon":      float(row["lon"]),
            "lng":      float(row["lon"]),   # alias for Leaflet
 
            # Marker colour from DB, fallback to gold
            "color":    row["color"] or "#a07840",
 
            # Photos
            "images":   images,
 
            # English content
            "history":      row["history"]     or "",
            "secondary":    row["secondary"]   or "",
            "visitor":      row["visitor"]      or "",
            "experience":   row["experience"]  or "",
            "nearby":       row["nearby"]       or "",
            "condition":    row["condition"]   or "",
            "translation":  row["translation"] or "",
 
            # Hindi content
            "hi_history":     row["hi_history"]     or "",
            "hi_secondary":   row["hi_secondary"]   or "",
            "hi_visitor":     row["hi_visitor"]     or "",
            "hi_experience":  row["hi_experience"]  or "",
            "hi_nearby":      row["hi_nearby"]      or "",
            "hi_condition":   row["hi_condition"]   or "",
            "hi_translation": row["hi_translation"] or "",
 
        })
 
    return jsonify(monuments)
 
 
# ==========================
# CHAT PAGE
# ==========================
@app.route("/chat", methods=["GET", "POST"])
def chat():
 
    reply = None
 
    if request.method == "POST":
 
        user_message = request.form.get("user_message", "")
 
        try:
 
            response = client.chat.completions.create(
 
                model=MODEL_NAME,
 
                messages=[
                    {
                        "role": "system",
                        "content":
                        """You are Djinn, 
                        You can answer ANY question. If user asks about shah alam, then by deafult consider it shah alam, a sufi saint during tuglah era. if the user asks about imam zamin, then a sufi saint in 16th century, until especified clearly. If the question is general, answer normally."""
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
 
                temperature=0.7,
                max_tokens=800
            )
 
            reply = response.choices[0].message.content
 
        except Exception as e:
            reply = str(e)
 
    return render_template("chat.html", reply=reply)
  
# ==========================
# MONUMENTS LIST PAGE
# ==========================
@app.route("/monuments")
def monuments_text_page():
 
    conn = get_db()
    c = conn.cursor()
 
    c.execute("""
        SELECT id, name
        FROM monuments
        ORDER BY name ASC
    """)
 
    monuments = c.fetchall()
    conn.close()
 
    return render_template("monuments.html", monuments=monuments)
 
 
# ==========================
# SINGLE MONUMENT API
# ==========================
@app.route("/api/monument/<int:monument_id>")
def monument_detail_api(monument_id):
 
    conn = get_db()
    c = conn.cursor()
 
    c.execute("""
        SELECT
            id,
            name,        hi_name,
            lat,         lon,
            color,
            image_url,
            history,     hi_history,
            secondary,   hi_secondary,
            visitor,     hi_visitor,
            experience,  hi_experience,
            nearby,      hi_nearby,
            condition,   hi_condition,
            translation, hi_translation
        FROM monuments
        WHERE id = ?
    """, (monument_id,))
 
    row = c.fetchone()
    conn.close()
 
    if not row:
        return jsonify({"error": "Monument not found"}), 404
 
    images = []
    if row["image_url"]:
        images = [u.strip() for u in row["image_url"].split(",")]
 
    return jsonify({
 
        "id":       row["id"],
 
        "name":     row["name"],
        "hi_name":  row["hi_name"] or row["name"],
 
        "lat":      float(row["lat"]),
        "lon":      float(row["lon"]),
        "lng":      float(row["lon"]),
 
        "color":    row["color"] or "#a07840",
 
        "images":   images,
 
        "history":      row["history"]     or "",
        "secondary":    row["secondary"]   or "",
        "visitor":      row["visitor"]     or "",
        "experience":   row["experience"]  or "",
        "nearby":       row["nearby"]      or "",
        "condition":    row["condition"]   or "",
        "translation":  row["translation"] or "",
 
        "hi_history":     row["hi_history"]     or "",
        "hi_secondary":   row["hi_secondary"]   or "",
        "hi_visitor":     row["hi_visitor"]     or "",
        "hi_experience":  row["hi_experience"]  or "",
        "hi_nearby":      row["hi_nearby"]      or "",
        "hi_condition":   row["hi_condition"]   or "",
        "hi_translation": row["hi_translation"] or "",
 
    })
 
 
# ==========================
# ERROR HANDLERS
# ==========================
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404
 
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
 
 
# ==========================
# SECURITY HEADERS
# ==========================
@app.after_request
def add_security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = \
        "default-src 'self' https: data: 'unsafe-inline' 'unsafe-eval'"
    return response
 
 
# ==========================
# RUN
# ==========================
if __name__ == "__main__":
    app.run(debug=True)