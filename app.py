from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS to allow front-end and back-end communication

# Route to fetch data by category
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    try:
        # Path to your Excel file
        excel_file_path = 'data.xlsx'

        # Load the Excel file
        df = pd.read_excel(excel_file_path)

        # Filter by category if provided in query parameters
        category = request.args.get('category')
        if category:
            df = df[df['Category'] == category]

        # Convert to a list of dictionaries
        data = df.to_dict(orient='records')

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
