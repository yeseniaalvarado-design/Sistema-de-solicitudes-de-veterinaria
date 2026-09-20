# PQRPet
## Sistema De Solicitudes De Veterinaria

<img src="https://github.com/yeseniaalvarado-design/Sistema-de-solicitudes-de-veterinaria/blob/8b9c763bffd91cda273fa6245b274a2dc4be8105/Logo%20Pet%20Service.png" alt="Imagen subida" width="300px">

### - Descripción
El presente proyecto consiste en la creación de un sistema de gestión para la atención del servicio veterinario de la Universidad de Antioquia, el nombre PQRPet combina las siglas PQRS con la palabra Pet, haciendo referencia directa al propósito principal del sistema: gestionar Peticiones, Quejas, Reclamos y Sugerencias (PQRS) desarrollado para facilitar el registro, organización, consulta y seguimiento de las solicitudes relacionadas con la atención de perros y gatos.

El sistema permite registrar la información de los solicitantes y de cada PQRS, asignar un número de radicado consecutivo, controlar el estado de las solicitudes y generar información para el análisis y seguimiento de la gestión.

El proyecto se desarrolla como un programa de consola utilizando Python y archivos planos para el almacenamiento y gestión de la información. 

### - Equipo desarrollador
Miguel Angel Guardia Vergara - 
Ingeniería industrial.

Diego Esteban Marín Mahecha - 
Ingeniería industrial.

Yesenia Paola Alvarado Arteaga - 
Ingeniería industrial.

### - Habilidades y fortalezas
### Miguel

Miguel se caracteriza por su responsabilidad, perseverancia y capacidad de adaptación. Se desenvuelve con facilidad ante los cambios y los nuevos desafíos, manteniendo una actitud orientada a encontrar soluciones. Además, cuenta con habilidades en el manejo de herramientas digitales y la resolución de problemas, especialmente en contextos de trabajo colaborativo, donde aporta ideas y contribuye al cumplimiento eficiente de los objetivos.

### Diego

Diego se destaca por la pasión y compromiso que demuestra en cada una de sus labores. Su responsabilidad y disposición para aprender le permiten asumir nuevos retos con entusiasmo y buscar constantemente oportunidades para mejorar. Asimismo, posee buenas habilidades para el trabajo colaborativo, aportando al equipo desde la comunicación, la cooperación y el compromiso con el cumplimiento de los objetivos.

### Yesenia

Yesenia se caracteriza por ser una persona responsable, disciplinada y observadora. Su capacidad de análisis y pensamiento crítico le permite identificar situaciones que requieren atención y proponer alternativas de solución. Además, tiene facilidad para potenciar las habilidades de sus compañeros, promoviendo un ambiente de colaboración y contribuyendo a que el trabajo en equipo sea más organizado, eficiente y orientado a resultados.

### - Licencia 
<a href="https://github.com/yeseniaalvarado-design">PQRPet</a> © 2026 by <a href="https://github.com/yeseniaalvarado-design/Sistema-de-solicitudes-de-veterinaria">Yesenia Alvarado, Miguel Guardia, Diego Marín</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">

## Visión Del Proyecto

### - Descripción General del Software
**PQRPet** es un sistema de gestión en consola desarrollado en Python, diseñado para optimizar el registro, seguimiento y control de las Peticiones, Quejas, Reclamos y Sugerencias (PQRS) de los servicios de atención veterinaria para perros y gatos en la Universidad de Antioquia. Reemplaza el proceso tradicional en papel de MEPEGA, garantizando persistencia mediante archivos planos independientes y comprobantes.

### - Objetivos del Proyecto
* **Actualización del proceso:** Evitar el registro a papel y lápiz, automatizando la asignación de números de radicado consecutivos e independientes para cada tipo de PQRS.
* **Control de tiempos:** Monitorear los plazos de respuesta (máximo 30 días calendario) para evitar vencimientos y generación de nuevas quejas o reclamos.
* **Análisis de datos:** Consolidar estadísticas clave sobre la atención de mascotas (perros y gatos) y sedes de la UdeA para la toma de decisiones.

### - Beneficios
* Optimización del tiempo de los estudiantes y funcionarios.
* Trazabilidad y transparencia en el estado de cada solicitud (`Registrada`, `En proceso`, `Solucionada`).
* Generación de comprobantes de radicado estandarizados de 120 caracteres.

## Especificaciones 

### - Requisitos Funcionales
* **RF-01 (Módulo de Autenticación):** El sistema debe restringir el acceso al menú principal mediante un login obligatorio validando el usuario y contraseña contra el archivo de credenciales autorizadas, con un bloqueo temporal de pantalla tras 3 intentos fallidos.
* **RF-02 (Registro Consecutivo Independiente):** El sistema debe permitir registrar nuevas PQRS (Peticiones, Quejas, Reclamos o Sugerencias) asignando un ID entero auto-incremental independiente para cada uno de los 4 archivos planos de datos.
* **RF-03 (Validación de Datos del Solicitante):** El sistema debe validar estrictamente que el nombre no contenga números, que el tipo de documento pertenezca a los permitidos (`CC`, `TI`, `CE`, `PP`, `NIT`), que el número tenga entre 3 y 15 dígitos, y que el teléfono tenga exactamente 10 dígitos.
* **RF-04 (Validación de Canales y Mascotas):** El sistema debe obligar a seleccionar una especie de mascota válida (`Perro`, `Gato`, `Otro`) y un canal de recepción autorizado de la UdeA.
* **RF-05 (Gestión de Tiempos y Plazos):** El sistema debe calcular automáticamente la fecha máxima de respuesta sumando 30 días calendario a la fecha de radicación.
* **RF-06 (Generación de Comprobante ASCII):** Tras un registro exitoso, el sistema debe generar e imprimir en consola (y guardar en `docs`) un comprobante estandarizado en formato ASCII con un ancho fijo exacto de 120 caracteres.
* **RF-07 (Consulta y Actualización de Estado):** El sistema debe permitir consultar los registros activos y actualizar el estado de la PQRS siguiendo obligatoriamente el flujo: `Registrada` `En proceso` `Solucionada`.
* **RF-08 (Módulo de Estadísticas):** El sistema debe calcular y mostrar en consola métricas clave, iniciando obligatoriamente con el promedio de días en valores enteros que toma dar respuesta a una PQRS.

### - Requisitos No Funcionales
* **RNF-01 (Persistencia en Archivos Planos):** Toda la información debe almacenarse exclusivamente en archivos planos delimitados por barras (`|`) organizados en la carpeta `data/` (`Peticion.txt`, `Queja.txt`, `Reclamo.txt`, `Sugerencia.txt` y el archivo de usuarios).
* **RNF-02 (Modularidad del Código):** El código fuente en Python debe estructurarse obligatoriamente de forma modular en la carpeta `src/`, separando validaciones (`validaciones.py`), manejo de archivos (`archivos.py`), reportes (`reportes.py`) y el menú principal (`main.py`).
* **RNF-03 (Usabilidad en Consola):** La interfaz de usuario en consola debe ser limpia, interactiva, intuitiva y mostrar mensajes de error claros ante ingresos inválidos.
* **RNF-04 (Compatibilidad y Versiones):** El software debe ser compatible con Python y utilizar las librerías propias (como `datetime`, `re`, `os`) sin dependencias externas complejas.

---

## Plan de Proyecto

### - Cronograma de Actividades.
El desarrollo del proyecto se divide en fases ágiles desde la semana 1 hasta la semana 16 del semestre académico:

```text
Fases / Semanas        | S1-S3 | S4-S6 | S7-S8 | S9 (Entrega 1) | S10-S13 | S14-S15 | S16 (Sustentación)
-----------------------|:-----:|:-----:|:-----:|:--------------:|:-------:|:-------:|:------------------:
1. Análisis y Visión   |   X   |       |       |                |         |         |                    
2. Estructura de Datos |       |   X   |       |                |         |         |                    
3. Desarrollo Python   |       |       |   X   |                |         |         |                    
4. Entrega 1           |       |       |       |       X        |         |         |                    
5. Comprobante         |       |       |       |                |    X    |         |                    
6. Dashboard Power BI  |       |       |       |                |    X    |         |                    
7. Pruebas y Ajustes   |       |       |       |                |         |    X    |                    
8. Entrega Final y Demo|       |       |       |                |         |         |         X
```

### - Presupuesto y Gestión del Tiempo del Proyecto
Dado que el proyecto se evalúa en función del esfuerzo y la dedicación académica y no monetaria, el presupuesto se define en horas de trabajo colaborativo e investigación:

* **Dedicación mínima total:** 50 horas de trabajo en equipo distribuidas entre los 3 integrantes del grupo.
* **Distribución equitativa base:** 
  * **Yesenia Paola Alvarado Arteaga:** 16.6 horas (Liderazgo, análisis y documentación).
  * **Miguel Angel Guardia Vergara:** 16.7 horas (Desarrollo en Python y persistencia).
  * **Diego Esteban Marín Mahecha:** 16.7 horas (Pruebas, validación y reportes).
* **Flexibilidad y Disponibilidad:** De requerirse para cumplir a cabalidad con los objetivos y la calidad del software, los 3 integrantes destinarán tiempo adicional a requerimiento, ajustando la disponibilidad según la complejidad de las fases de desarrollo y entrega.
