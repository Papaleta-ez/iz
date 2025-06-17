def calcular_presupuesto(monto):
    recursos_humanos = monto * 0.50
    manufactura = monto * 0.25
    empaquetado = monto * 0.15
    publicidad = monto * 0.10

    print(f"Recursos Humanos: ${recursos_humanos:.2f}")
    print(f"Manufactura: ${manufactura:.2f}")
    print(f"Empaquetado: ${empaquetado:.2f}")
    print(f"Publicidad: ${publicidad:.2f}")

monto = float(input("Ingrese el presupuesto anual: "))
calcular_presupuesto(monto)
