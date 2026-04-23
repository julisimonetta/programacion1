"""
La empresa de logística Distribuciones del Centro S.A. se encuentra en pleno proceso de modernización de sus sistemas de 
gestión. Debido al crecimiento sostenido en la demanda de envíos y almacenamiento, la organización ha detectado que uno de 
los principales problemas radica en la planificación del espacio dentro de sus depósitos. Actualmente, los productos llegan 
y se almacenan en distintas cantidades según la demanda de los clientes. Sin embargo, el sistema de organización interna 
del depósito trabaja con unidades agrupadas en centenas. Esto significa que los espacios físicos, los pallets y las zonas
de almacenamiento están diseñados para contener productos en bloques de 100 unidades. El inconveniente surge cuando la 
cantidad real de productos no coincide exactamente con estos bloques. Por ejemplo, si llegan 245 unidades de un producto, 
el sistema debe prever espacio suficiente para una cantidad mayor, ya que no es posible asignar fracciones de espacio. En 
este caso, se debería considerar la próxima centena completa (300 unidades), para asegurar que haya lugar suficiente para 
almacenar todo el lote sin inconvenientes. El área de sistemas ha sido convocada para desarrollar una solución que permita 
automatizar este cálculo. La idea es que, al ingresar la cantidad actual de productos de un determinado artículo, el sistema
determine automáticamente cuál es la siguiente centena completa mayor. Esta información será utilizada tanto por el área de 
depósito como por el área de planificación logística para organizar la distribución del espacio y anticiparse a futuras 
necesidades. Además, se busca que este cálculo sea claro, confiable y reutilizable dentro de otros módulos del sistema, ya 
que también podría aplicarse a la planificación de envíos, donde los transportes se organizan en capacidades similares.
Como parte del equipo de desarrollo, se te solicita analizar esta problemática y diseñar una solución que permita resolver 
este requerimiento de manera eficiente.
"""

cantProductos = int(input("Ingrese la cantidad de productos: "))
cantProductosTop = ((cantProductos + 99) // 100) * 100
print(cantProductosTop)