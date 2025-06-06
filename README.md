
# SmartHome - Proyecto Integrador (Módulo Programador)

Este proyecto es una simulación de un sistema de domótica desarrollado en Python, que permite gestionar dispositivos, automatizaciones y usuarios a través de una interfaz de línea de comandos. Forma parte del trabajo práctico de la materia ABP del ISPC.

---


## Funcionalidades

### Gestión de dispositivos

- *Agregar dispositivo*: con nombre, tipo (cámara, luz, música) y estado (encendido/apagado).
- *Listar dispositivos*: muestra todos los dispositivos registrados con sus detalles.
- *Buscar dispositivo*: por nombre, muestra el tipo y estado actual.
- *Eliminar dispositivo*: por nombre.

### Escenarios predefinidos (automatización elegida)

- *Modo Fiesta*:
  - Enciende automáticamente las luces y los equipos de música.
- *Modo Noche*:
  - Apaga las luces y enciende las cámaras de seguridad.



##  Tipos de dispositivos

| Tipo   | Código | Afectado por        |
|--------|--------|---------------------|
| Cámara | 1    | Modo Noche          |
| Luz    | 2    | Modo Fiesta / Noche |
| Música | 3    | Modo Fiesta         |



## 🚀 Funcionalidades Implementadas

* **Inicio de Sesión:** Permite a los usuarios autenticarse en el sistema.
* **Crear Cuenta:** Los nuevos usuarios pueden registrarse en el sistema.
* **Consultar Datos Personales:** Los usuarios pueden visualizar su información personal. 
* **Consultar Automatizaciones Activas:** Muestra el estado actual de las automatizaciones configuradas. 
* **Configurar Automatización:** Permite a los usuarios establecer automatizaciones personalizadas.
* **Modificar Rol de Usuario:** Los administradores pueden cambiar los roles de los usuarios.
* **Asignar Ubicaciones a Dispositivos:** Los dispositivos pueden ser asociados a ubicaciones específicas dentro de la vivienda.
* **Gestión de Vivienda:** Permite la administración de diferentes viviendas y sus dispositivos asociados.

---

## 🧑‍💻 Distribución del Equipo

| Funcionalidad                      | Estado    | Responsable |
| ---------------------------------- | --------- | ----------- |
| Consultar Datos Personales         | Terminado | Fausto      |
| Crear Cuenta                       | Terminado | Emiliano    |
| Configurar Automatización          | Terminado | Matias      |
| Consultar Automatizaciones Activas | Terminado | Kevin       |
| Modificar Rol de Usuario           | Terminado | Genaro      |
| Asignar Ubicaciones a Dispositivos | Terminado | Ignacio     |
| Gestión de Vivienda                | Terminado | Ignacio     |
| Inicio de Sesión                   | Terminado | Kevin       |

---

##  Estructura del proyecto

```
abp_programador/
├── main.py
├── usuarios.py
├── dispositivos.py
├── automatizaciones.py
├── funciones_auxiliares.py
├── README.md
├── roles.py
└── viviendas.py
```
* `main.py`: Contiene el menú principal y la lógica de navegación.
* `usuarios.py`: Maneja la autenticación y gestión de usuarios.
* `dispositivos.py`: Gestiona los dispositivos del sistema.
* `automatizaciones.py`: Controla las automatizaciones configuradas.
* `funciones_auxiliares.py`: Funciones de utilidad para validaciones y entradas.
* `roles.py`: Almacena los roles.
* `viviendas.py`: Gestiona todas las funciones de vivienda

---

##  Requisitos técnicos

- Python 3.10 o superior
- Consola o terminal

---

## 👥Créditos

**Desarrollado por:**
- Sánchez Matías Emanuel  
- Moreira Ignacio Javier  
- Cura Genaro  
- Requelme Kevin Agustín  
- Díaz Esteban Emiliano Gabriel

**Con la guía de:**
- ROJAS CÓRSICO Ivana Soledad  
- MAINERO Alejandro Luis  
- APERLO Agustina
- OLIVERO José

---

## 🛡️ Política de Protección de Datos para Sistema

- **Tipos de datos personales recolectados:**  
  El sistema puede manejar datos de dispositivos como nombre, tipo y estado. No se almacena información sensible del usuario.

- **Finalidad del procesamiento de datos:**  
  Los datos son utilizados exclusivamente para permitir la automatización del sistema en entornos simulados.

- **Medidas de seguridad implementadas:**  
  El sistema está limitado a ejecución local. No existe comunicación externa ni almacenamiento en la nube, asegurando aislamiento total.

- **Derechos del usuario sobre sus datos:**  
  Los usuarios podrán modificar, eliminar o consultar la información de dispositivos en cualquier momento desde el menú del sistema.

---

## 📜 Plan de Gestión del Trabajo en Equipo

- **Herramientas utilizadas:**  
  GitHub, VS Code, Discord, WhatsApp.

- **División del trabajo:**  
  El proyecto se dividió en tres módulos principales:  
  1. Gestión de dispositivos  
  2. Automatización de escenarios  
  3. Menú principal y flujo del usuario  

- **Coordinación del trabajo:**  
  Se realizaron reuniones por Discord y seguimiento en WhatsApp.  
  El repositorio en GitHub sirvió para compartir avances y hacer control de versiones.

- **Acuerdos de conducta y compromiso ético:**  
  Se acordó responsabilidad compartida, comunicación clara, y entrega en tiempo y forma como compromiso del equipo.

---

## 📌 Notas Adicionales

* El proyecto sigue las buenas prácticas del AWS Well-Architected Framework, enfocándose en la excelencia operativa, seguridad, confiabilidad, eficiencia en el rendimiento, optimización de costos y sostenibilidad.
* Se recomienda revisar los módulos y funciones para comprender la implementación detallada de cada funcionalidad.

---