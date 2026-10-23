---
title: "Tema II-5 · Informática básica"
description: Conceptos fundamentales sobre hardware y software, sistemas de almacenamiento de datos, sistemas operativos y nociones básicas de seguridad informática.
order: 205
---

!!! tip "Qué pide el programa"
    Informática básica: conceptos fundamentales sobre el hardware y el software · Sistemas de almacenamiento de datos · Sistemas operativos · Nociones básicas de seguridad informática.

    En el examen de 2026 salieron de aquí preguntas sobre **almacenamiento secundario**, **UTF-8**, **plug and play**, **malvertising**, **SGSI**, ***insider*** e **IA generativa**. Si quieres ampliar, el temario de TAI tiene un tema entero de [tecnología básica]({{base}}temario/tecnologia-basica/).

## 1. Conceptos básicos

- **Informática:** tratamiento **automático** de la información mediante ordenadores.
- **Hardware:** la parte **física** (lo que se puede tocar). **Software:** los **programas** y datos (lo que no se toca).
- **Unidades de información:** el **bit** (0 o 1) es la unidad mínima; un **byte** son **8 bits** (un carácter).

| Unidad | Equivale a |
| --- | --- |
| Kilobyte (KB) | 1.024 bytes |
| Megabyte (MB) | 1.024 KB |
| Gigabyte (GB) | 1.024 MB |
| Terabyte (TB) | 1.024 GB |
| Petabyte (PB) | 1.024 TB |

(En sentido estricto, los múltiplos de 1.024 se llaman KiB, MiB, GiB…, y KB, MB, GB son múltiplos de 1.000; los fabricantes de discos usan los de 1.000.)

**Codificación de caracteres:**

| Código | Bits | Qué representa |
| --- | --- | --- |
| **ASCII** | **7** (128 caracteres) | Letras inglesas, números y símbolos básicos |
| **ASCII extendido** | 8 (256) | Añade letras acentuadas, ñ… (varias versiones) |
| **EBCDIC** | 8 | Codificación de los grandes ordenadores de IBM |
| **Unicode / UTF-8** | **Variable: de 1 a 4 bytes** | **Casi todos los idiomas, símbolos y emojis**. Es el más usado en sistemas operativos y en la web |

## 2. El hardware

### La unidad central de proceso (CPU o procesador)

Ejecuta las instrucciones de los programas. Sus partes:

| Parte | Función |
| --- | --- |
| **Unidad de control (UC)** | **Dirige** el funcionamiento: lee e interpreta las instrucciones y coordina al resto |
| **Unidad aritmético-lógica (ALU)** | Hace los **cálculos** y las **comparaciones lógicas** |
| **Registros** | Memorias pequeñísimas y rapidísimas **dentro de la CPU** |
| **Memoria caché** | Memoria rápida entre la CPU y la RAM para acelerar el acceso a los datos más usados |

La velocidad se mide en **GHz**; los procesadores actuales tienen **varios núcleos**. Fabricantes: Intel, AMD, Apple (M), Qualcomm (ARM).

### La memoria principal

| Memoria | Características |
| --- | --- |
| **RAM** (*Random Access Memory*) | **Volátil**: se borra al apagar. Guarda los programas y datos **en uso**. Se mide en GB (8, 16, 32…) |
| **ROM** (*Read Only Memory*) | **No volátil** y de **solo lectura**. Contiene el firmware de arranque (**BIOS/UEFI**) |

### Placa base, buses y puertos

- La **placa base** conecta todos los componentes. Los **buses** transportan datos, direcciones y control.
- **Puertos y conexiones:** **USB** (tipo A y **tipo C**), **HDMI** y **DisplayPort** (vídeo), **Ethernet RJ45** (red), conector de audio, **Thunderbolt**; inalámbricas: **wifi** y **Bluetooth**.
- **Plug and play:** el sistema **reconoce y configura automáticamente** un dispositivo al conectarlo, sin configuración manual.

### Periféricos

| Tipo | Ejemplos |
| --- | --- |
| **De entrada** | Teclado, ratón, escáner, micrófono, webcam, lector de código de barras, lector de DNIe |
| **De salida** | Monitor, impresora, altavoces, proyector |
| **De entrada y salida** | Pantalla táctil, impresora multifunción, módem, router, unidades de almacenamiento |

## 3. El software

| Tipo | Qué es | Ejemplos |
| --- | --- | --- |
| **De sistema** | Gestiona el ordenador | Sistema operativo, controladores (**drivers**), firmware |
| **De aplicación** | Para que el usuario haga tareas | Word, Excel, Access, Outlook, navegadores |
| **De programación** | Para crear programas | Editores, compiladores, lenguajes (Java, Python…) |

**Según su licencia:** **propietario** (de pago, con código cerrado: Windows, Microsoft 365), **libre** (se puede usar, estudiar, modificar y distribuir: Linux, LibreOffice, Firefox), **de código abierto** (*open source*), **freeware** (gratuito pero cerrado) y **shareware** (prueba limitada).

**Ofimática:** programas para el trabajo de oficina: procesador de textos (**Word**), hoja de cálculo (**Excel**), base de datos (**Access**), presentaciones (**PowerPoint**) y correo (**Outlook**). **Microsoft 365** es la suscripción que los incluye junto a servicios en la nube (**OneDrive**, **Teams**, **SharePoint**, **To Do**, **Copilot**…).

**Inteligencia artificial:**

- **IA generativa:** crea contenido **original** (texto, imágenes, música, código) a partir de lo que ha aprendido: Copilot, ChatGPT, Gemini.
- **RPA** (*Robotic Process Automation*): «robots» de software que **automatizan tareas repetitivas** basadas en reglas.
- En la UE, el **Reglamento de Inteligencia Artificial** (UE) 2024/1689 regula su uso según el riesgo.

## 4. Sistemas de almacenamiento de datos

**Almacenamiento primario** (memoria principal: RAM, volátil) frente a **almacenamiento secundario**: **no volátil**, guarda los datos **de forma permanente** aunque se apague el equipo.

| Tecnología | Ejemplos | Notas |
| --- | --- | --- |
| **Magnética** | **Disco duro (HDD)**, cintas | Partes móviles (platos y cabezales); mucha capacidad y barata; las **cintas** se usan para copias de seguridad |
| **Óptica** | **CD** (≈700 MB), **DVD** (4,7 GB una capa), **Blu-ray** (25 GB por capa) | Lectura por láser; en desuso |
| **Estado sólido (flash)** | **SSD**, memorias **USB**, tarjetas **SD** | Sin partes móviles: **más rápida**, silenciosa y resistente |
| **En red** | **NAS** (almacenamiento en red local), **SAN** | Compartido por varios usuarios |
| **En la nube** | **OneDrive**, SharePoint, Google Drive | En servidores de Internet; sincronizado entre dispositivos |

**Copias de seguridad:**

| Tipo | Qué copia |
| --- | --- |
| **Completa** | **Todo** |
| **Incremental** | Lo que ha cambiado desde la **última copia de cualquier tipo** (rápida de hacer, lenta de restaurar) |
| **Diferencial** | Lo que ha cambiado desde la **última copia completa** |

La regla **3-2-1**: **3** copias, en **2** soportes distintos y **1** fuera de la oficina.

**Sistemas de archivos:** **NTFS** (el de Windows), **FAT32** (compatible, pero con archivos de **4 GB como máximo**), **exFAT** (memorias USB y tarjetas grandes).

## 5. Sistemas operativos

**Qué es:** el software básico que **gestiona los recursos** del ordenador y hace de **intermediario** entre el usuario, los programas y el hardware.

**Funciones:** gestión de **procesos** (qué programa usa la CPU), de la **memoria**, de los **archivos** y carpetas, de los **dispositivos** de entrada y salida, de la **seguridad** y los usuarios, y la **interfaz** con el usuario (gráfica o de comandos).

| Clasificación | Tipos |
| --- | --- |
| Por usuarios | **Monousuario** / **multiusuario** |
| Por tareas | **Monotarea** / **multitarea** (varios programas a la vez) |
| Por interfaz | De **texto** (línea de comandos) / **gráfica** (ventanas, iconos) |

**Ejemplos:** **Windows 11** (Microsoft; el que pide el examen), **macOS** (Apple), **Linux** (libre: Ubuntu, Debian…), **Android** (Google, basado en Linux) e **iOS** (Apple). **Windows 10** dejó de tener soporte en **octubre de 2025**.

## 6. Nociones básicas de seguridad informática

**Dimensiones de la seguridad:** **confidencialidad** (solo accede quien debe), **integridad** (los datos no se alteran) y **disponibilidad** (están accesibles cuando hacen falta); además, **autenticidad** y **trazabilidad** (las del Esquema Nacional de Seguridad).

### Amenazas

| Amenaza | Qué es |
| --- | --- |
| **Virus** | Código que se **adjunta a otros archivos** y se propaga al ejecutarlos |
| **Gusano** (*worm*) | Se **replica solo** por la red, sin necesidad de un archivo |
| **Troyano** | Se **disfraza** de programa legítimo para abrir una puerta trasera |
| **Ransomware** | **Cifra** los datos y pide un **rescate** |
| **Spyware** | **Espía** la actividad del usuario |
| **Adware** | Muestra **publicidad** no deseada |
| **Keylogger** | Registra lo que se **teclea** |
| **Botnet** | Red de equipos infectados («zombis») controlados a distancia, usada para ataques **DDoS** |
| **Malvertising** | **Publicidad maliciosa**: anuncios manipulados que instalan malware al pulsarlos |
| **Phishing** | **Correo** que suplanta a una entidad para robar datos. Variantes: **smishing** (SMS), **vishing** (llamada) |
| **Ingeniería social** | Manipular a las **personas** para que revelen información o hagan algo |
| ***Insider*** | Amenaza **interna**: persona de la propia organización que provoca un incidente, de forma **intencionada o accidental** |

### Medidas de protección

- **Antivirus** (en Windows 11, **Microsoft Defender**) y **cortafuegos** (*firewall*).
- **Actualizar** el sistema y los programas (Windows Update).
- **Contraseñas robustas** (largas, con mayúsculas, minúsculas, números y símbolos; distintas para cada servicio) y **autenticación multifactor** (algo que sabes + algo que tienes + algo que eres).
- **Copias de seguridad** periódicas.
- **Cifrado** de discos (**BitLocker** en Windows) y conexiones seguras (**HTTPS**, **VPN**).
- **Desconfiar** de adjuntos y enlaces inesperados; **bloquear el equipo** al levantarse (**Windows + L**).
- En el sector público, el **Esquema Nacional de Seguridad** (RD 311/2022; ver [ENS]({{base}}leyes/ens/)).

### Organismos y normas

- **SGSI** (Sistema de Gestión de la Seguridad de la Información): conjunto de elementos que usa una organización para fijar su política y objetivos de seguridad, con un enfoque de **gestión del riesgo** y **mejora continua**. Lo regula la familia **ISO/IEC 27000** (se certifica con la **ISO 27001**).
- **CCN-CERT** (Centro Criptológico Nacional): ciberseguridad del **sector público**.
- **INCIBE** (Instituto Nacional de Ciberseguridad): ciudadanos y empresas; línea de ayuda gratuita **017**.

## Resumen

| Dato | Respuesta |
| --- | --- |
| 1 byte | 8 bits |
| Memoria volátil | RAM |
| Almacenamiento secundario | No volátil, permanente |
| Codificación con emojis y longitud variable | UTF-8 (Unicode) |
| Partes de la CPU | Unidad de control, ALU y registros |
| Plug and play | Reconocer y configurar dispositivos automáticamente |
| Copia de lo cambiado desde la última completa | Diferencial |
| Publicidad maliciosa | Malvertising |
| Amenaza interna | *Insider* |
| SGSI | ISO/IEC 27000 (27001) |
| Ayuda en ciberseguridad | INCIBE, 017 |
