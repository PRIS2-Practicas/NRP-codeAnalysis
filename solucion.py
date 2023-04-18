from requisito import Requisito
from stakeholder import Stakeholder
from algoritmo import algoritmo_greedy

def main():
    # Crear stakeholders
    stakeholder1 = Stakeholder("Stakeholder 1")
    stakeholder2 = Stakeholder("Stakeholder 2")
    stakeholder3 = Stakeholder("Stakeholder 3")
    stakeholder4 = Stakeholder("Stakeholder 4")
    stakeholder5 = Stakeholder("Stakeholder 5")

    # Agregar recomendaciones
    stakeholder3.agregar_recomendacion(stakeholder2)
    stakeholder2.agregar_recomendacion(stakeholder3)
    stakeholder1.agregar_recomendacion(stakeholder2)


    # Crear requisitos
    requisito1 = Requisito("Requisito 1")
    requisito2 = Requisito("Requisito 2")
    requisito3 = Requisito("Requisito 3")
    requisito4 = Requisito("Requisito 4")
    requisito5 = Requisito("Requisito 5")

    # Agregar stakeholders a requisitos
    requisito1.agregar_stakeholder(stakeholder1)
    requisito2.agregar_stakeholder(stakeholder2)
    requisito3.agregar_stakeholder(stakeholder3)
    requisito1.agregar_stakeholder(stakeholder4)
    requisito4.agregar_stakeholder(stakeholder5)
    requisito4.agregar_stakeholder(stakeholder1)

    requisito1.agregar_exclusion(requisito2)
    #requisito2.agregar_implicacion(requisito3)
    requisito3.agregar_combinacion(requisito1)
    

    # Definir límite de coste
    limite_coste = 30

    # Obtener solución óptima con algoritmo Greedy
    solucion_optima = algoritmo_greedy([requisito1, requisito2, requisito3, requisito4], limite_coste)

    # Mostrar solución óptima
    for requisito in solucion_optima:
        print(f"{requisito.descripcion}: Satisfacción {requisito.calcular_satisfaccion()} - Coste {requisito.calcular_coste()}")


if __name__ == "__main__":
    main()
