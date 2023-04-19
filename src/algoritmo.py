def algoritmo_greedy(requisitos, limite_coste):
    requisitos_ordenados = sorted(requisitos, key=lambda r: r.calcular_satisfaccion(), reverse=True)

    solucion = []
    coste_acumulado = 0

    for requisito in requisitos_ordenados:
        if not requisito.es_factible(solucion):
            continue

        # Verificar si las implicaciones están en la solución
        implicaciones_cumplidas = all(implicacion in solucion for implicacion in requisito.implicaciones)

        # Si las implicaciones no se cumplen, pasar al siguiente requisito
        if not implicaciones_cumplidas:
            continue
        
        coste_combinado = sum([r.calcular_coste() for r in requisito.combinaciones]) + requisito.calcular_coste()
        if coste_acumulado + coste_combinado <= limite_coste:
            solucion.append(requisito)
            coste_acumulado += requisito.calcular_coste()
            for combinado in requisito.combinaciones:
                if combinado not in solucion:
                    solucion.append(combinado)
                    coste_acumulado += combinado.calcular_coste()
        elif requisito.combinaciones:
            continue
        elif coste_acumulado + requisito.calcular_coste() <= limite_coste:
            solucion.append(requisito)
            coste_acumulado += requisito.calcular_coste()

    return solucion
