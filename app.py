import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuración de la página
st.set_page_config(page_title="Desintegración Radiactiva - Fracción vs Periodos")

st.title("📉 Desintegración Radiactiva: Acumulación o Desintegración")

# Selección de tipo de simulación
modo = st.radio("Selecciona el tipo de simulación:", ["Acumulación", "Desintegración"])

# Entradas del usuario
num_periodos = st.slider("Número de periodos a simular", min_value=1, max_value=30, value=10)
dt = st.slider("Paso entre puntos (en periodos)", min_value=0.1, max_value=5.0, value=1.0)

# Parámetro constante
lambda_ln2 = np.log(2)  # ln(2)

# Inicializar listas para graficar
datos_n = []
datos_frac = []

# Contenedor para la gráfica
grafico = st.empty()

# Simulación
n = 0.0
while n <= num_periodos:
    if modo == "Acumulación":
        N_frac = 1 - np.exp(-lambda_ln2 * n)
    else:  # Desintegración
        N_frac = np.exp(-lambda_ln2 * n)

    datos_n.append(n)
    datos_frac.append(N_frac)

    # Graficar con escala fija
    fig, ax = plt.subplots()
    ax.plot(datos_n, datos_frac, color='green', marker='o', linestyle='-')
    ax.set_xlim(0, num_periodos)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Número de periodos")
    ax.set_ylabel("Fracción acumulada" if modo == "Acumulación" else "Fracción remanente")
    ax.set_title(f"Simulación de {modo}")
    ax.grid(True)
    grafico.pyplot(fig)

    n += dt
    time.sleep(1)

# Mostrar fórmula final
if modo == "Acumulación":
    st.latex(r"1 - e^{-\ln(2) \cdot \frac{t}{t_{1/2}}}")
else:
    st.latex(r"e^{-\ln(2) \cdot \frac{t}{t_{1/2}}}")

st.markdown("Donde:")
st.markdown("- \( N_0 \): número inicial de núcleos")
st.markdown("- \( t_{1/2} \): vida media")
st.markdown("- \( n = t / t_{1/2} \): número de periodos")

st.success("✅ Simulación completada.")
