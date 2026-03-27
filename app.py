from flask import Flask, jsonify

app = Flask(__name__)

tenants = [
    {"id": 1, "name": "Shop A1", "rent": 50000, "paid": 30000},
    {"id": 2, "name": "Shop B2", "rent": 40000, "paid": 40000}
]

@app.route('/')
def home():
    return "Rent Tracker API is alive!"

@app.route('/tenants', methods=['GET'])
def get_tenants():
    return jsonify(tenants)

@app.route('/arrears', methods=['GET'])
def get_arrears():
    arrears = []
    for tenant in tenants:
        balance = tenant["rent"] - tenant["paid"]
        if balance > 0:
            arrears.append({"name": tenant["name"], "balance": balance})
    return jsonify(arrears)

if __name__ == '__main__':
    app.run(debug=True)