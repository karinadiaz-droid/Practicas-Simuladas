# 🏛️ Software FJ - Sistema de Gestión de Reservas y Servicios (POO)

## Sistema Integral Orientado a Objetos ##

   ##   JOSE ARMANDO BLANCO GAMEZ   ##

Este proyecto es un simulador modular de gestión de clientes, servicios y reservas desarrollado bajo Programación Orientada a Objetos (POO) en Python. El sistema opera completamente en memoria y cuenta con control de excepciones y auditoría local.

## 🚀 Características del Proyecto
* **POO Estricto**: Uso de herencia, clases abstractas, encapsulamiento (`@property`) y polimorfismo.
* **Arquitectura Modular**: Separación limpia de responsabilidades en paquetes independientes.
* **Control de Excepciones**: Captura de errores de lógica de negocio mediante excepciones personalizadas.
* **Auditoría (Logs)**: Registro automático de fallos en un archivo físico (`log.txt`).
* **Simulador**: Flujo secuencializado de 10 operaciones de prueba (5 exitosas y 5 fallidas).

## 📂 Estructura del Directorio
```text
software FJ/
├── exceptions/     # Excepciones personalizadas del negocio
├── models/         # Clases base, Cliente, Reserva y Subclases de Servicio
├── repository/     # Simulación de persistencia en memoria
├── utils/          # Módulo de utilidades (Generador de Logs en txt)
├── README.md       # Portada de presentación del proyecto
└── main.py         # Punto de entrada y simulador de operaciones
```

## 🛠️ Cómo Ejecutar el Proyecto Localmente
1. Descarga o clona este repositorio.
2. Abre la terminal de comandos dentro de la carpeta raíz `software FJ`.
3. Ejecuta el comando:
   ```bash
   python main.py
   ```
