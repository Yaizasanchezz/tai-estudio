---
title: "Tema II-7 · El Explorador de archivos, accesorios y herramientas del sistema"
description: Gestión de carpetas y archivos, búsquedas, «Este equipo» y «Acceso rápido», accesorios y herramientas del sistema de Windows 11.
order: 207
---

!!! tip "Qué pide el programa"
    El explorador de Windows · Gestión de carpetas y archivos · Operaciones de búsqueda · Herramientas «Este equipo» y «Acceso rápido» · Accesorios · Herramientas del sistema.

## 1. Archivos y carpetas

- Un **archivo** (fichero) es un conjunto de información guardado de forma **permanente** en un soporte, identificado por un **nombre** y normalmente una **extensión** (tras el punto) que indica su **tipo** y con qué programa se abre: `Informe.docx`.
- Una **carpeta** (directorio) agrupa archivos y otras carpetas (**subcarpetas**), formando una estructura en **árbol**.
- La **ruta** indica dónde está: `C:\Users\Ana\Documentos\Informe.docx`.
- **No se pueden usar** en los nombres los caracteres `\ / : * ? " < > |`.

| Extensión | Tipo |
| --- | --- |
| .docx / .dotx / .docm | Documento / plantilla / documento con macros de **Word** |
| .xlsx / .xltx / .xlsm | Libro / plantilla / libro con macros de **Excel** |
| .accdb | Base de datos de **Access** |
| .pptx | Presentación de **PowerPoint** |
| .pst / .msg | Archivo de datos / mensaje de **Outlook** |
| .pdf | Documento PDF |
| .txt | Texto plano |
| .jpg / .png / .gif | Imágenes |
| .mp3 / .mp4 | Audio / vídeo |
| .zip | Carpeta **comprimida** |
| .exe / .msi | **Aplicación** / instalador |

## 2. El Explorador de archivos

Se abre con **Windows + E** o desde su icono (una carpeta amarilla) en la barra de tareas.

| Parte | Función |
| --- | --- |
| **Pestañas** | Como en un navegador: varias carpetas en la misma ventana (**Ctrl + T** abre una nueva) |
| **Barra de comandos** | **Nuevo**, **Cortar**, **Copiar**, **Pegar**, **Cambiar nombre**, **Compartir**, **Eliminar**, **Ordenar**, **Ver**, **Filtrar** y «Ver más» (…) |
| **Barra de direcciones** | La **ruta** de la carpeta actual; se puede escribir una ruta |
| **Cuadro de búsqueda** | Busca dentro de la carpeta actual y sus subcarpetas |
| **Panel de navegación** (izquierda) | **Inicio**, **Galería**, **OneDrive**, carpetas de usuario, **Este equipo**, **Red**… |
| **Panel de detalles / vista previa** | Información o contenido del archivo seleccionado |
| **Barra de estado** | Número de elementos y seleccionados |

### «Este equipo» y «Acceso rápido»

- **Este equipo:** muestra las **unidades** (disco local **C:**, otras particiones, memorias **USB**, unidades de red) con su espacio libre, y las **carpetas del usuario** (**Escritorio, Descargas, Documentos, Imágenes, Música y Vídeos**).
- **Acceso rápido:** lista de **carpetas ancladas** para llegar a ellas con un clic (Escritorio, Descargas, Documentos e Imágenes por defecto; se pueden **anclar** otras con el botón derecho > **Anclar a Acceso rápido**). En Windows 11 aparece en la página **Inicio** del Explorador, junto a **Favoritos** y **Recientes**.

### Vistas, ordenar y agrupar

- **Ver:** iconos muy grandes, grandes, medianos y pequeños; **Lista**; **Detalles** (columnas con nombre, fecha de modificación, tipo y tamaño); **Mosaicos**; **Contenido**. Ahí se activan **Extensiones de nombre de archivo** y **Elementos ocultos**.
- **Ordenar por:** nombre, **fecha de modificación**, **tipo**, **tamaño**…, de forma **ascendente o descendente**.
- **Agrupar por:** crea **grupos** (por ejemplo, por **tipo**); los grupos se ordenan alfabéticamente por su nombre y, dentro de cada uno, se aplica el orden elegido.

!!! example "Así lo preguntaron en 2026"
    Agrupando las Descargas **por Tipo** y ordenando por fecha ascendente, el primer elemento es el del grupo **«Aplicación»** (.exe), que va antes que «Carpeta comprimida» (.zip), «Documento de Microsoft Word» (.docx) y «Elemento de Outlook» (.msg).

## 3. Gestión de carpetas y archivos

| Operación | Cómo |
| --- | --- |
| **Crear carpeta** | Nuevo > Carpeta o **Ctrl + Mayús + N** |
| **Cambiar nombre** | **F2** o botón derecho > Cambiar nombre |
| **Seleccionar** | Clic; varios **salteados** con **Ctrl + clic**; varios **seguidos** con **Mayús + clic**; **todo** con **Ctrl + A** (los atajos de Windows no cambian con el idioma, a diferencia de los de Word o Excel) |
| **Copiar / Cortar / Pegar** | **Ctrl + C** / **Ctrl + X** / **Ctrl + V** |
| **Deshacer / Rehacer** | **Ctrl + Z** / **Ctrl + Y** |
| **Eliminar** | **Supr**: va a la **Papelera de reciclaje** (se puede **restaurar**). **Mayús + Supr**: se elimina **definitivamente**. Lo borrado de memorias USB o unidades de red no pasa por la Papelera |
| **Propiedades** | **Alt + Intro** o botón derecho > Propiedades (tamaño, ubicación, fechas, atributos **Solo lectura** y **Oculto**) |
| **Comprimir** | Botón derecho > **Comprimir en archivo ZIP** (las versiones recientes permiten también 7z y TAR); **Extraer todo** para descomprimir |
| **Abrir con otra aplicación** | Botón derecho > **Abrir con** > **Elegir otra aplicación** (con «Usar siempre» se convierte en la predeterminada). También en Configuración > Aplicaciones > **Aplicaciones predeterminadas** |
| **Crear acceso directo** | Botón derecho > Mostrar más opciones > Crear acceso directo, o arrastrar con **Alt** |

**Arrastrar y soltar:** en la **misma unidad**, **mueve**; a **otra unidad**, **copia**. Con **Ctrl** se fuerza **copiar**, con **Mayús** **mover** y con **Alt** se crea un **acceso directo**.

## 4. Operaciones de búsqueda

- El **cuadro de búsqueda** del Explorador (**Ctrl + F** o **Ctrl + E** para ir a él) busca en la carpeta actual y sus subcarpetas, por **nombre** y también por **contenido** en las ubicaciones indexadas.
- **Comodines:** `*` sustituye a **cualquier número** de caracteres (`*.pdf` = todos los PDF) y `?` a **un solo** carácter.
- **Filtros:** `tipo:pdf`, `fechademodificación:`, `tamaño:grande`, `autor:`…; o el botón **Filtrar** de la barra de comandos.
- Desde la **búsqueda de la barra de tareas** se buscan aplicaciones, documentos, configuraciones y en la web.

## 5. Accesorios

Pequeños programas que vienen con Windows:

| Accesorio | Para qué |
| --- | --- |
| **Bloc de notas** | Texto **sin formato** (.txt). Ahora con pestañas y autoguardado |
| **Paint** | Dibujo y edición sencilla de imágenes |
| **Recortes** (*Snipping Tool*) | **Capturas de pantalla** y grabación de vídeo (**Windows + Mayús + S** o **Impr Pant**) |
| **Calculadora** | Estándar, científica, gráfica, programador y conversor |
| **Fotos** | Ver y editar imágenes y vídeos |
| **Grabadora de sonido** | Grabar audio |
| **Reloj** | Alarmas, temporizador, cronómetro y sesiones de concentración |
| **Mapa de caracteres** | Insertar símbolos especiales |
| **Conexión a Escritorio remoto** | Controlar otro equipo |
| **Herramientas de accesibilidad** | **Lupa**, **Narrador**, **Teclado en pantalla**, reconocimiento de voz |

**WordPad** se eliminó en la versión **24H2** de Windows 11.

## 6. Herramientas del sistema

| Herramienta | Para qué |
| --- | --- |
| **Administrador de tareas** (**Ctrl + Mayús + Esc**) | Ver y **finalizar procesos** que no responden; **Rendimiento** (CPU, memoria, disco, red en tiempo real); **Aplicaciones de arranque**; usuarios; servicios |
| **Configuración** (**Windows + I**) y **Panel de control** | Ajustes del sistema (el Panel de control sigue existiendo para opciones clásicas) |
| **Sensor de almacenamiento** y **Liberador de espacio en disco** | Eliminar archivos temporales e innecesarios |
| **Desfragmentar y optimizar unidades** | Optimizar los discos (en los SSD hace **TRIM**, no desfragmenta) |
| **Información del sistema** (msinfo32) | Datos del hardware y el software |
| **Monitor de recursos** y **Visor de eventos** | Uso detallado de recursos y registro de errores y sucesos |
| **Restaurar sistema** | Volver a un **punto de restauración** anterior sin afectar a los documentos |
| **Copia de seguridad de Windows** | Copiar carpetas, configuración y aplicaciones a **OneDrive** |
| **Programador de tareas** | Ejecutar tareas automáticamente |
| **Administrador de dispositivos** y **Administración de discos** | Controladores (drivers) y particiones |
| **Terminal** (PowerShell y Símbolo del sistema) | Ejecutar comandos |
| **Windows Update** | Actualizaciones del sistema |
| **Seguridad de Windows** | Antivirus **Microsoft Defender**, firewall, control de aplicaciones |

## Resumen

| Dato | Respuesta |
| --- | --- |
| Abrir el Explorador | Windows + E |
| Nueva carpeta | Ctrl + Mayús + N |
| Cambiar nombre | F2 |
| Borrar sin pasar por la Papelera | Mayús + Supr |
| Arrastrar a otra unidad | Copia (en la misma, mueve) |
| Comodín de varios caracteres | * |
| Carpetas ancladas | Acceso rápido |
| Unidades y carpetas del usuario | Este equipo |
| Capturas de pantalla | Recortes (Windows + Mayús + S) |
| Finalizar un proceso | Administrador de tareas (Ctrl + Mayús + Esc) |
