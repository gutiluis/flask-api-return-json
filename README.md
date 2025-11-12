# Flask API to Return JSON from HTML Forms

This is a simple Flask application that serves an HTML form and returns a JSON response when the form is submitted, showing form data, headers, files, raw request body, JSON body, client IP, and URL in the jsonify response.

---

## Features

- Serves an HTML form for user input.
- Accepts `POST` requests and returns all submitted data as JSON.
- Supports:
  - Form fields (`request.form`)
  - File uploads (`request.files`)
  - Query parameters (`request.args`)
  - HTTP headers (`request.headers`)
  - Raw body (`request.data`)
  - JSON body (`request.get_json`)
- Shows client IP (`request.remote_addr`) and request URL (`request.url`).

---

## Requirements

- Python 3.7+
- Flask

## How to run:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

