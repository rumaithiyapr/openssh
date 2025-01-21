from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# SQLite database setup (change the path as needed)
DATABASE = "d:/my-flask-app/shareholders.db"

# Helper function to get the database connection
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To fetch rows as dictionaries
    return conn

# Root route
@app.route('/')
def home():
    return "Welcome to the Shareholders API!"

# API Route to fetch all shareholders (or implement your custom query)
@app.route('/api/shareholders', methods=['GET'])
def get_shareholders():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        # Example: Get all shareholders from the database
        cursor.execute("SELECT * FROM shareholders")
        shareholders = cursor.fetchall()
        
        # Convert rows to a list of dictionaries
        result = [dict(row) for row in shareholders]
        
        conn.close()
        return jsonify(result)  # Send the list as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Route to fetch a single shareholder by parameters
@app.route('/api/get-shareholder', methods=['GET'])
def get_shareholder():
    box_number = request.args.get('box_number')
    civil_id = request.args.get('civil_id')

    if not box_number or not civil_id:
        return jsonify({"message": "Missing required parameters"}), 400

    try:
        conn = get_db()
        cursor = conn.cursor()
        
        # Query to fetch a specific shareholder
        cursor.execute("SELECT * FROM shareholders WHERE box_number = ? AND civil_id = ?", (box_number, civil_id))
        row = cursor.fetchone()
        
        conn.close()

        if row:
            return jsonify(dict(row))  # Return as JSON
        else:
            return jsonify({"message": "Shareholder not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
