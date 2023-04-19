from requisito import Requisito
from stakeholder import Stakeholder
from algoritmo import algoritmo_greedy

def main():
    # Crear stakeholders y agregar recomendaciones
    stakeholders = [
        Stakeholder("Stakeholder 1"),
        Stakeholder("Stakeholder 2"),
        Stakeholder("Stakeholder 3"),
        Stakeholder("Stakeholder 4"),
        Stakeholder("Stakeholder 5")
    ]

    recomendaciones = [(2, 1), (1, 2), (0, 1), (4, 0), (3, 0)]
    for i, j in recomendaciones:
        stakeholders[i].agregar_recomendacion(stakeholders[j])

    # Crear requisitos
    requisitos = [Requisito(f"Requisito {i+1}") for i in range(5)]

    # Agregar stakeholders a requisitos
    stakeholders_requisitos = [
        (0, 0), (1, 1), (2, 2), (3, 0), (4, 3),
        (4, 4), (3, 4), (1, 1), (2, 3), (0, 3)
    ]
    for stakeholder_idx, requisito_idx in stakeholders_requisitos:
        requisitos[requisito_idx].agregar_stakeholder(stakeholders[stakeholder_idx])

    # Agregar relaciones entre requisitos
    requisitos[0].agregar_exclusion(requisitos[1])
    requisitos[2].agregar_combinacion(requisitos[4])
    requisitos[3].agregar_implicacion(requisitos[1])

    # Definir límite de coste
    limite_coste = 40

    # Obtener solución óptima con algoritmo Greedy
    solucion_optima = algoritmo_greedy(requisitos, limite_coste)

    # Mostrar solución óptima
    for requisito in solucion_optima:
        print(f"{requisito.descripcion}: Satisfacción {requisito.calcular_satisfaccion()} - Coste {requisito.calcular_coste()}")


if __name__ == "__main__":
    main()