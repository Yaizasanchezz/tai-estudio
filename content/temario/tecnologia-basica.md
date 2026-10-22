---
title: Bloque II · Tecnología básica
description: Representación de la información, componentes, estructuras de datos, sistemas operativos y SGBD.
order: 3
---

## II.1 Informática básica y representación de la información

- **Sistemas de numeración:** binario (base 2), octal (base 8), decimal (base 10) y hexadecimal (base 16: 0–9 y A–F). Cada dígito hexadecimal equivale a 4 bits y cada octal a 3 bits.
- **Unidades:** bit, byte (8 bits). Sistema internacional: 1 kB = 1.000 bytes, 1 MB = 10⁶. Sistema binario IEC: 1 KiB = 1.024 bytes, 1 MiB = 1.024 KiB. Orden: kilo, mega, giga, tera, peta, exa, zetta, yotta.
- **Enteros con signo:** signo-magnitud, complemento a 1 y **complemento a 2** (el habitual: rango con n bits de −2ⁿ⁻¹ a 2ⁿ⁻¹−1; con 8 bits, de −128 a 127).
- **Coma flotante IEEE 754:** simple precisión, 32 bits (1 signo, 8 exponente, 23 mantisa); doble precisión, 64 bits (1, 11, 52).
- **Códigos de caracteres:** ASCII (7 bits, 128 caracteres), ASCII extendido / ISO-8859-1 (8 bits), **Unicode** con codificaciones UTF-8 (1 a 4 bytes, compatible con ASCII), UTF-16 y UTF-32. Códigos detectores de errores: paridad, CRC, Hamming (corrige 1 bit).
- **Arquitectura Von Neumann:** CPU (unidad de control, ALU y registros como PC, IR, MAR y MDR), memoria principal que almacena datos e instrucciones, unidad de E/S y buses (datos, direcciones y control). La arquitectura Harvard separa la memoria de datos y la de instrucciones.
- **Jerarquía de memoria:** registros → caché L1/L2/L3 → RAM → almacenamiento secundario (SSD/HDD) → terciario (cintas). Más arriba, más rápida, cara y pequeña.
- **CISC vs RISC:** x86 es CISC (instrucciones complejas); ARM y RISC-V son RISC (instrucciones simples de tamaño fijo).

Ejemplos resueltos:

- 45 decimal a binario: 45 = 32 + 8 + 4 + 1 → **101101**.
- 101101 binario a hexadecimal: se agrupan de 4 en 4 desde la derecha, 0010 1101 → **2D**.
- 0x3F a decimal: 3 × 16 + 15 = **63**.
- −5 en complemento a 2 con 8 bits: 5 = 00000101 → se invierten los bits, 11111010 → se suma 1 → **11111011**.
- "Hola" en UTF-8 ocupa 4 bytes; "Ñ" ocupa 2 bytes; un emoji, 4 bytes.

## II.2 Componentes, periféricos y almacenamiento

| Elemento | Datos que se preguntan |
| --- | --- |
| Placa base | Chipset, zócalo (socket) de la CPU, ranuras de RAM DIMM, PCIe, firmware UEFI (sustituye a la BIOS; usa tablas de particiones GPT frente a MBR) |
| RAM | DDR4 y DDR5; volátil. ROM y flash: no volátiles |
| USB | 2.0: 480 Mbit/s · 3.2 Gen 1: 5 Gbit/s · 3.2 Gen 2: 10 · 3.2 Gen 2x2: 20 · USB4: 40 (v2: 80). El conector USB-C es reversible |
| Vídeo | HDMI, DisplayPort, Thunderbolt (40 Gbit/s en la versión 3 y 4); VGA es analógica |
| Discos | HDD (platos, RPM, tiempo de búsqueda); SSD SATA (~550 MB/s); SSD NVMe por PCIe (varios GB/s); formato M.2 |
| Impresoras | Láser (tóner, alta velocidad), inyección de tinta, térmica (tickets), matricial (impacto, copias autocopiativas). Resolución en ppp/dpi |
| Pantallas | LCD/LED, OLED; resolución (Full HD 1920×1080, 4K UHD 3840×2160), frecuencia en Hz, tamaño en pulgadas |
| Digitalización | Escáner (resolución óptica), OCR para reconocer texto; cámaras |
| Color | RGB es aditivo (pantallas); CMYK es sustractivo (impresión) |

Ejemplo práctico: un puesto de usuario necesita copiar 10 GB a un disco externo. Con USB 2.0 (480 Mbit/s ≈ 60 MB/s teóricos) tarda unos 3 minutos; con USB 3.2 Gen 1 (5 Gbit/s), teóricamente unos 16 segundos.

## II.3 Estructuras de datos, ficheros, algoritmos y formatos

- **Estructuras lineales:** array o vector (acceso directo por índice), lista enlazada (simple, doble, circular), **pila** (LIFO: push/pop; se usa en llamadas a funciones y en deshacer) y **cola** (FIFO: encolar/desencolar; se usa en colas de impresión).
- **No lineales:** árbol (raíz, nodos, hojas, altura), **árbol binario de búsqueda** (a la izquierda los menores, a la derecha los mayores), árboles equilibrados AVL y B/B+ (usados en índices de bases de datos), montículo (heap) y **grafos** (dirigidos o no, ponderados; recorridos en anchura BFS y en profundidad DFS; Dijkstra para el camino más corto).
- **Tablas hash:** acceso medio O(1); colisiones resueltas por encadenamiento o direccionamiento abierto.
- **Recorridos de un árbol binario:** preorden (raíz–izquierda–derecha), inorden (izquierda–raíz–derecha; en un ABB da los valores ordenados) y postorden (izquierda–derecha–raíz).
- **Complejidad:** búsqueda secuencial O(n); búsqueda binaria O(log n), requiere el vector ordenado; burbuja, selección e inserción O(n²); **mergesort** O(n log n); **quicksort** O(n log n) en el caso medio y O(n²) en el peor.
- **Organización de ficheros:** secuencial (acceso en orden), directa o aleatoria (posición calculada, *hashing*), secuencial indexada (índice + área de datos) e indexada.
- **Formatos:** texto (TXT, CSV, JSON, XML, YAML); documentos (PDF, **PDF/A** para conservación, ODF como estándar abierto, DOCX); imagen (JPEG con pérdida, PNG sin pérdida y con transparencia, GIF de 256 colores y animación, SVG vectorial, TIFF); audio (MP3, AAC, FLAC sin pérdida, WAV sin comprimir); vídeo (MP4/H.264, H.265, WebM); comprimidos (ZIP, 7z, TAR.GZ).

Ejemplo práctico: si insertas en un ABB vacío 50, 30, 70, 20, 40, el recorrido inorden devuelve 20, 30, 40, 50, 70 (ordenado) y el preorden 50, 30, 20, 40, 70.

## II.4 Sistemas operativos

- **Funciones:** gestión de procesos, memoria, ficheros, E/S y seguridad, e interfaz con el usuario. Núcleo monolítico (Linux), micronúcleo e híbrido (Windows NT, macOS).
- **Procesos e hilos:** un proceso es un programa en ejecución con su propio espacio de memoria; los hilos comparten la memoria del proceso. Estados: nuevo, listo, en ejecución, bloqueado y terminado.
- **Planificación de CPU:** FCFS (primero en llegar), SJF (trabajo más corto primero), **Round Robin** (por turnos con quantum de tiempo, apropiativo), por prioridades y colas multinivel.
- **Memoria:** paginación (páginas de tamaño fijo), segmentación, **memoria virtual** (fallos de página, swap). Algoritmos de reemplazo: FIFO, LRU y óptimo.
- **Interbloqueo (deadlock):** se produce si se dan las cuatro condiciones de Coffman: exclusión mutua, retención y espera, no expropiación y espera circular.
- **Windows:** sistema de ficheros NTFS (permisos, cifrado EFS, cuotas), ReFS; registro de Windows; PowerShell; Active Directory; versión vigente Windows 11.
- **Linux/Unix:** distribuciones (Debian, Ubuntu, Red Hat/RHEL, SUSE). Jerarquía FHS: /etc (configuración), /var (datos variables y logs), /home, /bin y /usr/bin, /tmp, /dev, /proc. Sistemas de ficheros ext4, XFS, Btrfs.
- **Permisos en Linux:** propietario, grupo y otros; lectura (4), escritura (2) y ejecución (1). `chmod 754` = rwx para el propietario, r-x para el grupo, r-- para otros.
- **Comandos frecuentes:** `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `mkdir`, `cat`, `grep`, `find`, `chmod`, `chown`, `ps`, `top`, `kill`, `df` (espacio de disco), `du` (uso de directorios), `tar`, `ssh`, `sudo`, `systemctl`.
- **Móviles:** Android (núcleo Linux, Google) e iOS (Apple). Gestión de dispositivos móviles (MDM) en la Administración.

Ejemplo práctico: un script `backup.sh` debe poder ejecutarlo solo su propietario y leerlo su grupo. Se usa `chmod 740 backup.sh` (rwx r-- ---).

## II.5 Sistemas de gestión de bases de datos

- **SGBD:** software que permite definir, manipular y controlar bases de datos garantizando integridad, seguridad, concurrencia y recuperación.
- **Arquitectura ANSI/SPARC:** tres niveles (externo o vistas, conceptual y interno o físico) que dan **independencia lógica y física** de los datos.
- **Propiedades ACID de una transacción:** Atomicidad (todo o nada), Consistencia, Aislamiento (Isolation) y Durabilidad.
- **Niveles de aislamiento SQL:** READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ y SERIALIZABLE (lecturas sucias, no repetibles y fantasma).
- **Modelos:** jerárquico, en red, **relacional** (Oracle, PostgreSQL, MySQL/MariaDB, SQL Server), orientado a objetos y objeto-relacional.
- **NoSQL:** clave-valor (Redis), documental (MongoDB, documentos JSON/BSON), columnar (Cassandra, HBase) y grafos (Neo4j). Siguen el modelo **BASE** (Basically Available, Soft state, Eventual consistency).
- **Teorema CAP:** un sistema distribuido solo puede garantizar a la vez dos de tres propiedades: consistencia, disponibilidad y tolerancia a particiones.

Ejemplo práctico: en una transferencia entre dos cuentas, si falla el abono después del cargo, la **atomicidad** obliga a deshacer el cargo (ROLLBACK).
