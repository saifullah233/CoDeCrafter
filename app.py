from flask import Flask, render_template, request, send_file
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

app = Flask(_name_)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def home():
    return render_template("index.html")


# ------------------ FILE UPLOAD CONVERT TO EXCEL ------------------
@app.route('/convert_file', methods=['POST'])
def convert_file():
    file = request.files['file']

    if file.filename == "":
        return "No file selected!"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        # Detect file type and read
        if file.filename.endswith(".csv"):
            df = pd.read_csv(filepath)

        elif file.filename.endswith(".json"):
            df = pd.read_json(filepath)

        else:   # plain text
            data = file.read().decode("utf-8")
            df = pd.DataFrame({"Data": data.splitlines()})

        output_excel = "converted_file.xlsx"
        df.to_excel(output_excel, index=False)

        return send_file(output_excel, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}"


# ------------------ WEBSITE SCRAPER TO EXCEL ------------------
@app.route('/convert_url', methods=['POST'])
def convert_url():
    url = request.form['url']

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table")
        if table is None:
            return "No table found on this website!"

        rows = []
        for tr in table.find_all("tr"):
            row = [td.text.strip() for td in tr.find_all(["td", "th"])]
            rows.append(row)

        df = pd.DataFrame(rows)
        output_excel = "website_data.xlsx"
        df.to_excel(output_excel, index=False)

        return send_file(output_excel, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}"


if _name_ == "_main_":
    app.run(debug=True)
