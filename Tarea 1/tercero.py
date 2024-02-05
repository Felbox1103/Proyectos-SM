tasas_interes = [0.02, 0.03, 0.04] 

porcentaje_banco = 0.1  # 10% de las ganancias

cantidad_dinero = float(input("Ingresa la cantidad de dinero a invertir: "))

ganancias_mensuales = [cantidad_dinero * tasa for tasa in tasas_interes]

# Ganancia año
ganancias_totales = sum(ganancias_mensuales) * 12

# ganancias del banco
ganancias_banco = ganancias_totales * porcentaje_banco

# ganancias del cliente
ganancias_finales = ganancias_totales - ganancias_banco

print("Ganancias totales en un año:", ganancias_totales)
print("Ganancias que el banco se queda:", ganancias_banco)
print("Ganancias finales para el cliente:", ganancias_finales)