from flask import Flask, send_file
import pandas as pd


app = Flask(__name__)

def load_csv_to_dataframe():
    df = pd.read_csv('datos.csv')
    return df

@app.route('/api/tablas', methods=['GET'])
def get_tablas():
    df = load_csv_to_dataframe()
    excel_file = 'datos.xlsx'
    df.to_excel(excel_file, index=False)
#    data = df.to_dict(orient='records')
#    return jsonify(data)
    return send_file(excel_file)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
