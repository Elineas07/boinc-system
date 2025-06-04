from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)
latest_data = {}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>BOINC Status</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .box { border: 1px solid #ccc; padding: 15px; margin-bottom: 10px; border-radius: 8px; }
        h2 { margin-top: 0; }
    </style>
</head>
<body>
    <h1>BOINC Statusoversikt</h1>
    {% if data %}
        <div class="box">
            <h2>Fra: {{ data.hostname }}</h2>
            <p><strong>Oppdatert:</strong> {{ data.timestamp }}</p>
            <p><strong>Status:</strong> {{ data.status }}</p>
            <p><strong>Feil:</strong> {{ data.error or "Ingen" }}</p>
        </div>
    {% else %}
        <p>Ingen data mottatt ennå.</p>
    {% endif %}
</body>
</html>
"""

@app.route('/boinc-update', methods=['POST'])
def receive_boinc_data():
    global latest_data
    latest_data = request.json
    print(f"Mottatt fra {latest_data.get('hostname')} @ {latest_data.get('timestamp')}")
    return "OK", 200

@app.route('/')
def show_status():
    return render_template_string(HTML_TEMPLATE, data=latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)