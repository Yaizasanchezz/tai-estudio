---
title: Tema II-10 · Bases de datos: Access 365
description: Principales funciones y utilidades. Tablas, consultas, formularios, informes y relaciones. Importación, vinculación y exportación de datos.
order: 210
---

!!! tip "Qué pide el programa"
    Bases de datos: Access 365 · Principales funciones y utilidades · Tablas · Consultas · Formularios · Informes · Relaciones · Importación, vinculación y exportación de datos.

    En 2026 cayeron **cinco** preguntas de Access (vistas de formularios, criterios de consultas, Texto de validación, importar HTML y borrar registros). Si quieres la base teórica de las bases de datos relacionales, está en el [temario de TAI]({{base}}temario/desarrollo/).

## 1. Qué es Access

**Microsoft Access** es un **sistema gestor de bases de datos relacionales** (SGBD) de escritorio. Guarda **todo** (tablas, consultas, formularios, informes, macros y módulos) en **un solo archivo** con extensión **.accdb** (el tamaño máximo es de **2 GB**).

- **Base de datos relacional:** los datos se organizan en **tablas** relacionadas entre sí mediante campos comunes, para **no repetir información**.
- **Registro** = cada **fila** (un cliente, un expediente). **Campo** = cada **columna** (nombre, DNI, fecha).
- **Panel de navegación** (a la izquierda): lista de los **objetos** de la base de datos.

| Objeto | Para qué sirve |
| --- | --- |
| **Tablas** | **Almacenar** los datos. Son la base de todo |
| **Consultas** | **Preguntar** a los datos: seleccionar, filtrar, calcular o modificar |
| **Formularios** | **Introducir, consultar y modificar** datos de forma cómoda en pantalla |
| **Informes** | **Presentar e imprimir** los datos con formato, agrupados y con totales |
| **Macros** | **Automatizar** tareas sin programar |
| **Módulos** | Código en **VBA** (Visual Basic para Aplicaciones) |

**Archivos relacionados:** **.accdb** (base de datos), **.accde** (compilada: no se puede modificar el diseño ni ver el código), **.accdt** (plantilla), **.laccdb** (archivo de **bloqueo** que se crea mientras alguien la tiene abierta) y **.mdb** (formato antiguo, de Access 2003 y anteriores).

**Mantenimiento:** **Archivo > Información > Compactar y reparar** reduce el tamaño y corrige errores.

!!! warning "Lo que no se puede deshacer"
    En Access, los cambios en los datos se **guardan automáticamente** al pasar a otro registro, y **un registro eliminado no se puede recuperar con Deshacer**: Access pide confirmación antes de borrarlo.

## 2. Tablas

**Vistas:** **Hoja de datos** (ver y escribir los datos, como en Excel) y **Vista Diseño** (definir los **campos**, sus **tipos** y **propiedades**). En una tabla **no puede haber dos campos con el mismo nombre**.

### Tipos de datos

| Tipo | Uso |
| --- | --- |
| **Texto corto** | Texto o números que no se usan para calcular (DNI, teléfono, código postal). **Máximo 255 caracteres** |
| **Texto largo** | Textos extensos (observaciones). Antes se llamaba **Memo** |
| **Número** | Números para **calcular** (con distintos tamaños: byte, entero, entero largo, simple, doble, decimal) |
| **Número grande** | Enteros muy grandes |
| **Fecha/Hora** | Fechas y horas |
| **Moneda** | Importes, sin errores de redondeo |
| **Autonumeración** | Número **único** que Access pone **automáticamente** a cada registro (no se puede modificar). Típico de la clave principal |
| **Sí/No** | Valores **booleanos** (casilla de verificación) |
| **Objeto OLE** | Objetos de otros programas (en desuso) |
| **Hipervínculo** | Direcciones web o de archivos |
| **Datos adjuntos** | Archivos adjuntos (imágenes, documentos) |
| **Calculado** | Resultado de una **expresión** con otros campos |
| **Asistente para búsquedas** | Crea una **lista desplegable** con valores de otra tabla o de una lista |

### Propiedades de los campos

**Tamaño del campo**, **Formato**, **Lugares decimales**, **Máscara de entrada** (plantilla para escribir el dato, por ejemplo, el formato del DNI), **Título** (nombre que se muestra), **Valor predeterminado**, **Regla de validación** (condición que debe cumplir el dato, por ejemplo `>=0`), **Texto de validación** (el **mensaje** que aparece si no se cumple la regla), **Requerido** (obligatorio), **Permitir longitud cero** e **Indexado** (No / Sí, con duplicados / **Sí, sin duplicados**). **No todas las propiedades existen para todos los tipos** (por ejemplo, Lugares decimales solo en los numéricos).

**Clave principal:** el campo (o campos) que **identifica de forma única** cada registro. **No puede repetirse ni quedar vacío** (nulo). Se marca con una **llave**.

## 3. Relaciones

Se definen en **Herramientas de base de datos > Relaciones**, arrastrando el campo común de una tabla a otra.

| Tipo | Ejemplo |
| --- | --- |
| **Uno a uno** (1:1) | Un empleado tiene una ficha médica |
| **Uno a varios** (1:N) | Un cliente tiene **muchos** pedidos. La más habitual: la **clave principal** de una tabla se relaciona con la **clave externa** de la otra |
| **Varios a varios** (N:M) | Alumnos y asignaturas. Se resuelve con una **tabla intermedia** (de unión) y dos relaciones 1:N |

- **Integridad referencial:** impide tener registros «huérfanos» (un pedido de un cliente que no existe) y borrar registros del lado «uno» que tengan registros relacionados.
- **Actualizar en cascada los campos relacionados:** si cambia la clave principal, se cambia en la tabla relacionada.
- **Eliminar en cascada los registros relacionados:** al borrar un registro principal, se borran sus relacionados.
- **Tipo de combinación:** interna (solo los registros coincidentes) o externa (todos los de una tabla aunque no tengan pareja).

## 4. Consultas

**Vistas:** **Hoja de datos** (resultado), **Vista Diseño** (la **cuadrícula QBE**) y **Vista SQL**. Se crean con el **Asistente para consultas** o el **Diseño de consulta** (ficha Crear).

| Tipo | Qué hace |
| --- | --- |
| **De selección** | **Muestra** datos que cumplen unos criterios (la más común). **No modifica** nada |
| **De parámetros** | Pide un dato al ejecutarla: en Criterios se escribe `[Introduzca la provincia]` |
| **De totales** | Agrupa y calcula (suma, promedio, cuenta…) con el botón **Σ Totales** |
| **De tabla de referencias cruzadas** | Resume datos en filas y columnas, como una tabla dinámica |
| **De acción: creación de tabla** | Crea una **tabla nueva** con el resultado |
| **De acción: datos anexados** | **Añade** registros a otra tabla |
| **De acción: actualización** | **Modifica** datos de forma masiva |
| **De acción: eliminación** | **Borra** registros |

### Criterios en la cuadrícula de diseño

| Criterio | Significado |
| --- | --- |
| `"Suministros"` | Texto **entre comillas** |
| `#01/01/2025#` | Fecha **entre almohadillas** |
| `>#01/01/2025#` | **Posterior** al 1 de enero de 2025 |
| `Entre 100 Y 500` | Entre dos valores |
| `Como "A*"` | Empieza por A (**comodines**: `*` cualquier número de caracteres, `?` uno solo) |
| `Es Nulo` / `No Es Nulo` | Vacío / con datos |
| Criterios en la **misma fila** | Se cumplen **todos** (**Y**) |
| Criterios en **filas distintas** («o») | Basta con que se cumpla **uno** (**O**) |

## 5. Formularios

Sirven para trabajar con los datos registro a registro, de forma cómoda. Se crean en la ficha **Crear**: **Formulario** (automático), **Diseño del formulario**, **Formulario en blanco**, **Asistente para formularios**, **Navegación** y **Más formularios** (varios elementos, hoja de datos, **formulario dividido**).

**Vistas** (botón **Ver** de la ficha Inicio):

| Vista | Para qué |
| --- | --- |
| **Vista Formulario** | **Introducir, consultar y modificar** los datos |
| **Vista Presentación** | Cambiar el diseño **viendo los datos** reales |
| **Vista Diseño** | Modificar la **estructura** en detalle (secciones y controles) |

**Controles:** **etiqueta** (texto fijo), **cuadro de texto** (muestra o recoge un dato), **cuadro combinado** (lista desplegable), **cuadro de lista**, **casilla de verificación**, **botón de opción**, **botón de comando**, imagen, **subformulario** (para mostrar los registros relacionados, por ejemplo, los pedidos de un cliente).

## 6. Informes

Presentan los datos para **imprimir** o exportar, con **agrupaciones**, **ordenaciones** y **totales**. Se crean con **Informe**, **Diseño de informe**, **Informe en blanco**, el **Asistente para informes** o el **Asistente para etiquetas**.

- **Vistas:** **Vista Informes**, **Vista preliminar** (como se imprimirá), **Vista Presentación** y **Vista Diseño**.
- **Secciones:** **Encabezado del informe** (solo al principio), **Encabezado de página**, **Encabezado de grupo**, **Detalle** (cada registro), **Pie de grupo** (subtotales), **Pie de página** (número de página) y **Pie del informe** (totales generales, solo al final).

## 7. Importación, vinculación y exportación

Desde la ficha **Datos externos**:

| Operación | Qué hace |
| --- | --- |
| **Importar** | **Copia** los datos de otro origen en una **tabla nueva** de Access. Los cambios posteriores en el original **no** se reflejan |
| **Vincular** | Crea una **tabla vinculada** (con una flecha en su icono) que **se conecta** al origen: los datos siguen en el archivo original y se ven **actualizados** |
| **Exportar** | Saca datos de Access a **Excel**, **texto**, **XML**, **PDF o XPS**, **Word** (RTF), otra base de datos Access, SharePoint… |

**Nuevo origen de datos** agrupa los orígenes:

| Grupo | Orígenes |
| --- | --- |
| **De un archivo** | **Excel**, **HTML**, **XML**, **archivo de texto** |
| **De una base de datos** | **Access**, SQL Server, Azure… |
| **De servicios en línea** | Listas de **SharePoint**, Dynamics 365… |
| **De otros orígenes** | **ODBC**, carpeta de **Outlook** |

## Resumen

| Dato | Respuesta |
| --- | --- |
| Extensión | .accdb (máximo 2 GB) |
| Texto corto | Máximo 255 caracteres |
| Número automático único | Autonumeración |
| Mensaje si no se cumple la regla de validación | Texto de validación |
| Identifica cada registro | Clave principal (ni repetida ni nula) |
| Vistas de un formulario | Formulario, Presentación y Diseño |
| Introducir y modificar datos en un formulario | Vista Formulario |
| Texto y fecha en criterios | "Texto" y #fecha# |
| Criterios en la misma fila | Y |
| Importar HTML | Datos externos > Nuevo origen de datos > De un archivo |
| ¿Se puede deshacer el borrado de un registro? | No |
