# Sistema Integral de Gestión - Software FJ

Este proyecto es una solución académica desarrollada en **Python** que implementa un sistema de reservas y gestión de servicios aplicando los pilares de la Programación Orientada a Objetos (POO).

## 🚀 Características y Requerimientos
El sistema cumple con los siguientes puntos técnicos:
- **Abstracción:** Uso de la clase base `Servicio`.
- **Herencia:** Clases `AlquilerSala` y `AlquilerEquipos`.
- **Polimorfismo:** Métodos de cálculo de costo especializados por servicio.
- **Encapsulamiento:** Validación de datos sensibles en la clase `Cliente`.
- **Manejo de Excepciones:** Uso de bloques `try/except/finally` y excepciones personalizadas.
- **Persistencia en Log:** Registro automático de errores en la carpeta `/logs`.

## 📁 Estructura del Proyecto
- `main.py`: Punto de entrada y ejecución de pruebas.
- `modules/`: Lógica de negocio (Modelos, Servicios y Excepciones).
- `logs/`: Historial de errores detectados.

## 🛠️ Instrucciones de Uso
1. Clonar el repositorio.
2. Ejecutar el comando:
   ```bash
   python main.py
   ```
