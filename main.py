import sys
from pathlib import Path
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask, render_template

# Add the project directory to PYTHONPATH for module resolution
sys.path.append(str(Path(__file__).parent))

# Import sub-applications
from qr_code_generator.app import qr_app
from scanner.app import scanner_app

# Main Flask app
main_app = Flask(__name__, template_folder="templates", static_folder="static")

# Combine the apps using DispatcherMiddleware
main_app.wsgi_app = DispatcherMiddleware(
    main_app.wsgi_app,
    {
        '/qrcode': qr_app,  # QR Code Generator app accessible via /qrcode
        '/scanner': scanner_app,  # QR Code Scanner app accessible via /scanner
    }
)

@main_app.route('/')
def index():
    return render_template('index.html')  # Render the styled homepage

if __name__ == "__main__":
    main_app.run(host="0.0.0.0", port=3000, debug=True)  # Enable debug mode for easier development
