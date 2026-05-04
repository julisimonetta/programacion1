"""
Ejercicio 18: Aplicación de delivery
Registrar la cantidad de pedidos entregados por 15 repartidores. Calcular el pago de cada
repartidor considerando un bono si supera las 30 entregas.
"""
cantPedidos = 0
for i in range(1, 16, 1):
    pedidosExtra = 0
    pedidos = 0
    pedidosPorRepartidor = int(input(f"Ingrese la cantidad de pedidos realizados por el repartidor #{i}: "))

    if pedidosPorRepartidor > 30:
        pedidosExtra = pedidosPorRepartidor - 30
        pedidos = 30

        pedidosExtra = pedidosExtra * 20

    else:
        pedidos = pedidosPorRepartidor
    
    pedidos = pedidos * 10

    cantPedidos += pedidosPorRepartidor

    print(f"El repartidor #{i} realizó {pedidosPorRepartidor} pedidos, por lo que le corresponde ${pedidos} por los pedidos y ${pedidosExtra} por los pedidos extra")

print(f"La cantidad de pedidos fue de {cantPedidos}")

