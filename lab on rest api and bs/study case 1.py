from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
customers = {}
current_id = 1


# POST - Create Customer
@app.route('/customers', methods=['POST'])
def create_customer():
    global current_id

    data = request.json
    data['id'] = current_id
    customers[current_id] = data
    current_id += 1

    return jsonify(data), 201


# GET - Retrieve Customer
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    if customer_id in customers:
        return jsonify(customers[customer_id]), 200
    return jsonify({"error": "Customer not found"}), 404


# PUT - Full Update
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    if customer_id in customers:
        data = request.json
        data['id'] = customer_id
        customers[customer_id] = data
        return jsonify(data), 200
    return jsonify({"error": "Customer not found"}), 404


# PATCH - Partial Update
@app.route('/customers/<int:customer_id>', methods=['PATCH'])
def patch_customer(customer_id):
    if customer_id in customers:
        data = request.json
        customers[customer_id].update(data)
        return jsonify(customers[customer_id]), 200
    return jsonify({"error": "Customer not found"}), 404


# DELETE - Remove Customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_id in customers:
        del customers[customer_id]
        return '', 204
    return jsonify({"error": "Customer not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)