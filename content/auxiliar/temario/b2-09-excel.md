---
title: "Tema II-9 · Hojas de cálculo: Excel 365"
description: Libros, hojas y celdas. Configuración. Introducción y edición de datos. Fórmulas y funciones. Gráficos. Gestión de datos. Personalización del entorno de trabajo.
order: 209
---

!!! tip "Qué pide el programa"
    Hojas de cálculo: Excel 365 · Principales funciones y utilidades · Libros, hojas y celdas · Configuración · Introducción y edición de datos · Fórmulas y funciones · Gráficos · Gestión de datos · Personalización del entorno de trabajo.

    Es el tema de ofimática que **más pesa** (en 2026, seis preguntas de Excel). En Excel en español, las **funciones tienen nombres en español** (SUMA, BUSCARX…) y los argumentos se separan con **punto y coma** (`;`).

## 1. Libros, hojas y celdas

| Concepto | Qué es |
| --- | --- |
| **Libro** | El **archivo** de Excel (**.xlsx**). Contiene una o varias **hojas** |
| **Hoja de cálculo** | Cuadrícula de **filas** (numeradas: **1.048.576**) y **columnas** (letras: de A a **XFD**, **16.384**). Pestañas abajo: insertar (**Mayús + F11**), cambiar nombre (doble clic), mover, copiar, color, ocultar |
| **Celda** | Intersección de fila y columna; se identifica por su **referencia**: **B3**. La activa aparece en el **cuadro de nombres** |
| **Rango** | Conjunto rectangular de celdas: **A1:C5**. Varios rangos separados: **A1:A5;C1:C5** |
| **Barra de fórmulas** | Muestra el **contenido real** de la celda (por ejemplo, la fórmula, no su resultado) |

**Formatos de archivo:** **.xlsx** (libro), **.xlsm** (con **macros**), **.xltx** (**plantilla**), **.xlsb** (binario), **.xls** (Excel 97-2003), **.csv** (texto separado por comas o punto y coma: **solo guarda la hoja activa y sin formato**), **.pdf**, **.ods** (OpenDocument).

## 2. Introducción y edición de datos

- **Tipos de datos:** **texto** (se alinea a la **izquierda**), **números** y **fechas** (a la **derecha**) y **fórmulas** (empiezan por **=**).
- **Las fechas son números de serie:** el **1** es el **1/1/1900**, el 2 el 2/1/1900… Por eso se puede restar una fecha a otra y obtener los días entre ambas. Si a una celda con el valor **1** se le da formato de fecha corta, muestra **01/01/1900**.
- **Editar una celda:** **F2** o doble clic. **Alt + Intro**: **salto de línea** dentro de la celda. **Supr** borra el contenido (no el formato).
- **Controlador de relleno** (el cuadradito de la esquina): arrastrándolo se **copian** datos o fórmulas o se crean **series** (1, 2, 3…; lunes, martes…; enero, febrero…).
- **Relleno rápido:** Excel detecta un patrón y completa la columna (Datos > Relleno rápido).
- **Pegado especial** (**Ctrl + Alt + V**): pegar solo **valores**, **formatos**, **fórmulas**, **transponer**, operaciones…
- **Validación de datos** (Datos > Validación de datos): limitar lo que se puede escribir (lista desplegable, números entre…, fechas…) con mensaje de entrada y de error.
- **Notas** y **comentarios** en las celdas.

### Formato de celdas (**Ctrl + 1**)

Pestañas **Número**, **Alineación**, **Fuente**, **Bordes**, **Relleno** y **Proteger**.

| Formato de número | Ejemplo con 0,758 |
| --- | --- |
| General | 0,758 |
| Número con 2 decimales | 0,76 |
| **Porcentaje sin decimales** | **76 %** (multiplica por 100 y **redondea**) |
| Moneda | 0,76 € |
| Fecha corta (con el valor 1) | 01/01/1900 |

El formato **solo cambia cómo se ve**: el valor real sigue siendo 0,758.

**Formato condicional** (Inicio > Formato condicional): aplica formato según el valor (resaltar celdas mayores que, duplicados, **barras de datos**, **escalas de color**, **conjuntos de iconos**, reglas con fórmulas).

## 3. Fórmulas

- Empiezan por **=**. **Operadores:** `+ - * / ^` (potencia), `&` (unir textos) y de comparación `= < > <= >= <>`.
- **Orden de cálculo:** paréntesis → potencias → multiplicación y división → suma y resta.

### Referencias

| Tipo | Ejemplo | Al copiar la fórmula… |
| --- | --- | --- |
| **Relativa** | `A1` | **Cambia** fila y columna |
| **Absoluta** | `$A$1` | **No cambia** |
| **Mixta** | `$A1` o `A$1` | Fija solo la columna o solo la fila |
| **A otra hoja** | `Hoja2!A1` | |
| **A otro libro** | `[Ventas.xlsx]Hoja1!A1` | |

**F4** alterna entre los tipos de referencia mientras se escribe la fórmula. También se puede **asignar un nombre** a un rango (cuadro de nombres o Fórmulas > Administrador de nombres).

### Errores

| Error | Causa |
| --- | --- |
| **#####** | No es un error de fórmula: la **columna es demasiado estrecha** o hay una **fecha u hora negativa** |
| **#¡DIV/0!** | **División entre cero** o entre una celda vacía |
| **#N/D** | El valor **no está disponible** (por ejemplo, BUSCARV no encuentra lo que busca) |
| **#¿NOMBRE?** | Excel **no reconoce** un texto de la fórmula (función mal escrita, texto sin comillas) |
| **#¡REF!** | **Referencia no válida** (se borró una celda a la que apuntaba la fórmula) |
| **#¡VALOR!** | **Tipo de dato incorrecto** (operar con texto) |
| **#¡NUM!** | Número no válido o demasiado grande |
| **#¡NULO!** | Intersección de rangos que no se cruzan |
| **#¡DESBORDAMIENTO!** | Una fórmula de **matriz dinámica** no tiene espacio para mostrar sus resultados |

## 4. Funciones

**Sintaxis:** `=NOMBRE(argumento1;argumento2;…)`. Se insertan con el botón **fx** (**Mayús + F3**) o desde la ficha **Fórmulas**. La **Autosuma** (Σ, **Alt + =**; en teclado español, **Alt + Mayús + 0**) inserta SUMA.

| Categoría | Funciones | Qué hacen |
| --- | --- | --- |
| **Matemáticas** | **SUMA**, **REDONDEAR**, ENTERO, TRUNCAR, ABS, POTENCIA, RAIZ, **SUMAR.SI**, **SUMAR.SI.CONJUNTO**, SUMAPRODUCTO, ALEATORIO.ENTRE | Sumar, redondear, sumar con condiciones |
| **Estadísticas** | **PROMEDIO**, **MAX**, **MIN**, **CONTAR** (cuenta **números**), **CONTARA** (cuenta celdas **no vacías**), **CONTAR.BLANCO** (vacías), **CONTAR.SI**, **CONTAR.SI.CONJUNTO**, PROMEDIO.SI, MEDIANA, MODA | Contar y promediar |
| **Lógicas** | **SI**, **Y**, **O**, **NO**, **SI.ERROR**, SI.CONJUNTO | Decidir según condiciones |
| **Búsqueda** | **BUSCARX**, **BUSCARV** (en vertical), BUSCARH (en horizontal), **INDICE**, **COINCIDIR**, **COINCIDIRX** | Buscar un valor en una tabla |
| **Texto** | **CONCAT**, CONCATENAR, **UNIRCADENAS**, **IZQUIERDA**, **DERECHA**, **EXTRAE**, **LARGO**, **MAYUSC**, **MINUSC**, **NOMPROPIO**, **ESPACIOS**, ENCONTRAR, HALLAR, SUSTITUIR, TEXTO | Unir, cortar y transformar textos |
| **Fecha y hora** | **HOY**, **AHORA**, FECHA, **AÑO**, **MES**, **DIA**, DIASEM, DIAS, DIAS.LAB, SIFECHA | Trabajar con fechas |
| **Información** | ESBLANCO, ESNUMERO, **ESTEXTO**, ESERROR | Comprobar el tipo de contenido |
| **Matrices dinámicas** (365) | **FILTRAR**, **ORDENAR**, ORDENARPOR, **UNICOS**, SECUENCIA, LET | Devuelven **varios resultados** que se «desbordan» a las celdas vecinas |
| **Expresiones regulares** (365, nuevas) | **REGEXPRUEBA** (comprueba si el texto coincide con un **patrón**: VERDADERO/FALSO), REGEXEXTRAER, REGEXREEMPLAZAR | Trabajar con patrones de texto |

**Ejemplos:**

- `=SI(B2>=5;"Aprobado";"Suspenso")`
- `=CONTAR.SI(C2:C100;"Madrid")` → cuántas veces aparece Madrid.
- `=SUMAR.SI.CONJUNTO(C2:C6;B2:B6;"Nómina";C2:C6;">2000")` → suma los importes de C cuyo concepto (B) es exactamente «Nómina» **y** que son mayores de 2.000. El **primer argumento** es el rango que se suma; después van **pares** rango-criterio que deben cumplirse **todos**. El rango de suma puede ser también rango de criterio.
- `=BUSCARX(A2;Empleados!A:A;Empleados!C:C;"No existe")` → busca A2 en la columna A de la hoja Empleados y devuelve el dato de la columna C. **BUSCARX** busca en cualquier dirección, usa **coincidencia exacta** por defecto y sustituye a BUSCARV y BUSCARH.
- `=BUSCARV(A2;Tabla;3;FALSO)` → busca A2 en la **primera columna** de la tabla y devuelve la **tercera**; FALSO = coincidencia exacta.

## 5. Gráficos

- Se crean seleccionando los datos e **Insertar > Gráficos** (o **Gráficos recomendados**). **Alt + F1** crea un gráfico **incrustado** en la hoja; **F11**, un gráfico en una **hoja nueva**.
- **Tipos:** **columnas** y **barras** (comparar), **líneas** (evolución en el tiempo), **circular** (partes de un total; una sola serie), **área**, **dispersión (XY)**, **combinado**, **cascada**, **histograma**, **mapa**, **embudo**…
- **Elementos:** título, **ejes**, **leyenda**, **etiquetas de datos**, líneas de cuadrícula, **área del gráfico** y **área de trazado**. Se cambian con el botón **+** o en **Diseño de gráfico** y **Formato**.
- **Minigráficos** (*sparklines*): gráficos diminutos **dentro de una celda** (línea, columna, ganancia o pérdida).

## 6. Gestión de datos

| Herramienta | Para qué |
| --- | --- |
| **Ordenar** | Por una o varias columnas, de A a Z, de menor a mayor, por color… |
| **Filtro** (**Ctrl + Mayús + L**) | Mostrar solo las filas que cumplen criterios; **filtro avanzado** con criterios en otro rango |
| **Tablas** (Insertar > Tabla) | Convertir un rango en **tabla**: formato automático, filtros, **fila de totales** y fórmulas con nombres de columna |
| **Quitar duplicados** | Eliminar filas repetidas |
| **Texto en columnas** | Separar un texto en varias columnas (por ejemplo, «Apellido, Nombre») |
| **Subtotales** y **Agrupar** (esquemas) | Totales por grupos y ocultar o mostrar detalles |
| **Tablas dinámicas** (Insertar > Tabla dinámica) | **Resumir** grandes cantidades de datos arrastrando campos a **filas**, **columnas**, **valores** y **filtros** |
| **Obtener y transformar** (Power Query) | Importar y limpiar datos de otras fuentes |
| **Análisis de hipótesis** | **Buscar objetivo**, **Administrador de escenarios** y **Tabla de datos** |
| **Inmovilizar paneles** (Vista) | Dejar fijas las filas o columnas de títulos al desplazarse |

## 7. Configuración, impresión y personalización

- **Configurar página** (Disposición de página): **márgenes**, **orientación**, **tamaño**, **área de impresión**, **saltos de página**, **imprimir títulos** (repetir filas en cada página), **encabezado y pie**, **ajustar** a una página de ancho.
- **Vistas:** **Normal**, **Diseño de página** y **Vista previa de salto de página**.
- **Proteger:** **proteger hoja** (impedir cambios en celdas bloqueadas) y **proteger libro** (estructura); **cifrar con contraseña** en Archivo > Información.
- **Recuperar:** la **Autorrecuperación** guarda copias temporales; los libros sin guardar se recuperan en **Archivo > Información > Administrar libro > Recuperar libros no guardados**.
- **Personalizar:** **Archivo > Opciones** (fórmulas, revisión, guardar, idioma, avanzadas, **cinta de opciones**, **barra de acceso rápido**), mostrar u ocultar líneas de cuadrícula y encabezados, zoom.

## 8. Atajos de Excel

| Atajo | Acción | Atajo | Acción |
| --- | --- | --- | --- |
| **F2** | Editar la celda | **Ctrl + 1** | **Formato de celdas** |
| **F4** | Referencia absoluta / repetir | **Ctrl + Mayús + L** | **Filtros** |
| **Alt + Intro** | Salto de línea en la celda | **Alt + F1** / **F11** | Gráfico incrustado / en hoja nueva |
| **Ctrl + Inicio** | Ir a **A1** | **Mayús + F11** | Nueva hoja |
| **Ctrl + Fin** | Última celda con datos | **Ctrl + Av Pág / Re Pág** | Hoja siguiente / anterior |
| **Ctrl + flechas** | Ir al extremo de los datos | **Ctrl + Alt + V** | Pegado especial |
| **Ctrl + N / K / S** | Negrita / cursiva / subrayado (en español) | **Ctrl + G** | Guardar (en español) |
| **F9** | Recalcular | **Mayús + F3** | Insertar función |

## Resumen

| Dato | Respuesta |
| --- | --- |
| Filas y columnas | 1.048.576 filas y 16.384 columnas (XFD) |
| Separador de argumentos | Punto y coma |
| Referencia absoluta | $A$1 (F4) |
| 1 en formato fecha | 01/01/1900 |
| ##### | Columna estrecha o fecha/hora negativa |
| Buscar avanzado | BUSCARX |
| Comprobar un patrón de texto | REGEXPRUEBA |
| Sumar con varias condiciones | SUMAR.SI.CONJUNTO (rango de suma primero) |
| Cuenta celdas no vacías | CONTARA |
| Resumir muchos datos | Tabla dinámica |
