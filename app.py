from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return "API de Divisas Activa"

# Tasas de cambio (puedes ajustar los valores según el día)
TASA_EURO = 20.50
TASA_DOLAR = 18.50
TASA_DOLAR_CAN = 13.60
TASA_LIBRA = 24.00

# 1. Euro a Pesos MX
@app.route('/euro_a_pesos/<float:cantidad>')
def euro_a_pesos(cantidad):
    return jsonify({"resultado": cantidad * TASA_EURO})

# 2. Dólar US a Pesos MX
@app.route('/dolar_a_pesos/<float:cantidad>')
def dolar_a_pesos(cantidad):
    return jsonify({"resultado": cantidad * TASA_DOLAR})

# 3. Dólar Canadiense a Pesos MX
@app.route('/dolarcan_a_pesos/<float:cantidad>')
def dolarcan_a_pesos(cantidad):
    return jsonify({"resultado": cantidad * TASA_DOLAR_CAN})

# 4. Libra a Pesos MX
@app.route('/libra_a_pesos/<float:cantidad>')
def libra_a_pesos(cantidad):
    return jsonify({"resultado": cantidad * TASA_LIBRA})

# 5. Pesos MX a Euro
@app.route('/pesos_a_euro/<float:cantidad>')
def pesos_a_euro(cantidad):
    return jsonify({"resultado": cantidad / TASA_EURO})

# 6. Pesos MX a Dólar US
@app.route('/pesos_a_dolar/<float:cantidad>')
def pesos_a_dolar(cantidad):
    return jsonify({"resultado": cantidad / TASA_DOLAR})

# 7. Pesos MX a Dólar Canadiense
@app.route('/pesos_a_dolarcan/<float:cantidad>')
def pesos_a_dolarcan(cantidad):
    return jsonify({"resultado": cantidad / TASA_DOLAR_CAN})

# 8. Pesos MX a Libra
@app.route('/pesos_a_libra/<float:cantidad>')
def pesos_a_libra(cantidad):
    return jsonify({"resultado": cantidad / TASA_LIBRA})

if __name__ == '__main__':
    app.run(port=5000)
