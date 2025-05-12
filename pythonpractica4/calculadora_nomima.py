# --- Constantes ---
PORCENTAJE_TSS = 0.0304  # 3.04% del sueldo bruto
PORCENTAJE_BONIFICACION = 0.0833  # 8.33% de bonificación

# --- Rangos del ISR Anual ---
RANGO_EXENTO_ANUAL = 416220
RANGO_MEDIO1_ANUAL = 624329
RANGO_MEDIO2_ANUAL = 867123

# --- Montos fijos según el tramo ---
MONTO_FIJO_RANGO_MEDIO2 = 31216
MONTO_FIJO_RANGO_ALTO = 79776

# --- Función para calcular el ISR ---
def calcular_isr(sueldo_mensual):
    sueldo_anual = sueldo_mensual * 12

    if sueldo_anual <= RANGO_EXENTO_ANUAL:
        isr_anual = 0
    elif sueldo_anual <= RANGO_MEDIO1_ANUAL:
        excedente = sueldo_anual - RANGO_EXENTO_ANUAL
        isr_anual = excedente * 0.15
    elif sueldo_anual <= RANGO_MEDIO2_ANUAL:
        excedente = sueldo_anual - RANGO_MEDIO1_ANUAL
        isr_anual = MONTO_FIJO_RANGO_MEDIO2 + (excedente * 0.20)
    else:
        excedente = sueldo_anual - RANGO_MEDIO2_ANUAL
        isr_anual = MONTO_FIJO_RANGO_ALTO + (excedente * 0.25)

    return isr_anual / 12  # ISR mensual

# --- Función principal ---
def main():
    print("===== CALCULADORA DE NÓMINA 2025 - R.D. =====")

    while True:
        try:
            sueldo_bruto = float(input("\nIngrese el sueldo bruto mensual (RD$): "))
            if sueldo_bruto <= 0:
                print("Error: El sueldo debe ser mayor que 0.")
            else:
                break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    while True:
        try:
            otros_descuentos = float(input("Ingrese otros descuentos (RD$) [0 si no aplica]: "))
            if otros_descuentos < 0:
                print("Error: No puede ingresar descuentos negativos.")
            else:
                break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    # Cálculos
    descuento_tss = sueldo_bruto * PORCENTAJE_TSS
    retencion_isr = calcular_isr(sueldo_bruto)
    bonificacion = sueldo_bruto * PORCENTAJE_BONIFICACION
    sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion

    # Resultados
    print("\n===== RESULTADOS =====")
    print(f"Sueldo Bruto: RD$ {sueldo_bruto:.2f}")
    print(f"Descuento TSS (3.04%): RD$ {descuento_tss:.2f}")
    print(f"Retención ISR: RD$ {retencion_isr:.2f}")
    print(f"Otros Descuentos: RD$ {otros_descuentos:.2f}")
    print(f"Bonificación (8.33%): RD$ {bonificacion:.2f}")
    print(f"SUELDO NETO: RD$ {sueldo_neto:.2f}")

    print("\nDetalle:")
    print(f"- Total descuentos: RD$ {descuento_tss + retencion_isr + otros_descuentos:.2f}")
    print(f"- Bonificación aplicada: RD$ {bonificacion:.2f}")

if __name__ == "__main__":
    main()
