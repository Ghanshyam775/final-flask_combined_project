from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask, render_template
from qr_code_generator.app import qr_app  # Importing QR code generator app
from scanner.app import scanner_app  # Importing scanner app

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

# Route for the homepage
@main_app.route('/')
def index():
    return render_template('index.html')  # Render the homepage (make sure index.html exists in templates folder)

if __name__ == "__main__":
    main_app.run(host="0.0.0.0", port=3000, debug=True)  # Run the app in debug mode on all IPs (0.0.0.0)
