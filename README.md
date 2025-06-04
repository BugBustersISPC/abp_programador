
# SmartHome - Proyecto Integrador (Módulo Programador)

Este proyecto simula un sistema básico de gestión de dispositivos inteligentes en un hogar, desarrollado como parte del *ABP del Módulo Programador* del ISPC.

Permite a los usuarios:
- Registrar, listar, buscar y eliminar dispositivos.
- Activar automatizaciones como "Modo Fiesta" y "Modo Noche".



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



## Uso del sistema

Al ejecutar el programa (main.py), se accede a un menú de consola:


1. Agregar dispositivo
2. Listar dispositivos
3. Buscar dispositivo
4. Eliminar dispositivo
5. Activar Modo Fiesta
6. Activar Modo Noche
7. Salir



##  Estructura del proyecto

```
abp_programador_ispc/
├── __pycache__/ # Archivos compilados de Python
├── automatizaciones.py # Funciones de escenarios predefinidos
├── dispositivos.py # Funciones de gestión de dispositivos
├── main.py # Menú principal y flujo de usuario
└── README.md # Documentación de este proyecto
```

##  Requisitos técnicos

- Python 3.10 o superior
- Consola o terminal



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
