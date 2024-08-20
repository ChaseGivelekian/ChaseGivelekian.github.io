from flask import Flask, request, redirect, render_template_string
import csv
import os

app = Flask(__name__)

# Directory for CSV file
csv_file_path = os.path.join(os.getcwd(), "messages.csv")

@app.route('/')
def home():
    return "Server is running!"

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Write form data to CSV
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])

    # Redirect to a thank you page
    return render_template_string("""
        <h2>Thank You!</h2>
        <p>Your message has been sent successfully.</p>
        <a href="http://127.0.0.1:5500/index.html">Return to Home</a>
    """)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)