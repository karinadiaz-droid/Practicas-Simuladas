# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del Proyecto

Este proyecto corresponde al desarrollo de un sistema orientado a objetos para la empresa Software FJ, capaz de gestionar clientes, servicios y reservas sin utilizar bases de datos.

El sistema permite:

- Registrar clientes
- Gestionar servicios
- Procesar reservas
- Validar información
- Manejar excepciones
- Registrar errores en archivos logs

El proyecto fue desarrollado en Python aplicando Programación Orientada a Objetos (POO) y manejo avanzado de excepciones.

---

# Tecnologías Utilizadas

- Python 3
- Programación Orientada a Objetos
- Manejo de archivos
- GitHub

---

# Estructura del Proyecto

```text
SoftwareFJ/
│
├── main.py
├── README.md
├── logs.txt
│
├── modelos/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── reserva.py
│   ├── sala.py
│   ├── equipo.py
│   ├── asesoria.py
│
├── excepciones/
│   ├── excepciones.py
│
├── utilidades/
│   ├── logger.py
```

---

# Funcionalidades

## Gestión de Clientes

- Registro de clientes
- Validación de correo electrónico
- Validación de teléfono

## Gestión de Servicios

- Reserva de salas
- Alquiler de equipos
- Asesorías especializadas

## Gestión de Reservas

- Confirmación de reservas
- Cancelación de reservas
- Cálculo de costos

## Manejo de Excepciones

- Excepciones personalizadas
- Validaciones robustas
- Registro de errores
- Encadenamiento de excepciones

---

# Características de Programación Orientada a Objetos

El proyecto implementa:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación

---

# Ejecución del Proyecto

## Requisitos

- Python 3 instalado

## Ejecutar el sistema

```bash
python main.py
```

---

# Manejo de Logs

Todos los errores y eventos importantes se almacenan en:

```text
logs.txt
```

---

# Integrantes del Grupo

- Karina Paola Diaz Arroyo
- Rafael Torres Blanco
- Jose Armando Blanco Gamez
---

# Resultados Esperados

El sistema debe:

- Continuar funcionando aunque existan errores
- Manejar excepciones correctamente
- Registrar eventos en logs
- Validar entradas del usuario
- Ejecutar reservas exitosas y fallidas

---

# Autor

Proyecto académico desarrollado para la actividad de Programación Orientada a Objetos y Manejo de Excepciones.
