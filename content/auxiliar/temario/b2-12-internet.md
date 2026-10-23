---
title: Tema II-12 · La Red Internet
description: Origen, evolución y estado actual. Conceptos elementales sobre protocolos y servicios en Internet. Funcionalidades básicas de los navegadores web.
order: 212
---

!!! tip "Qué pide el programa"
    La Red Internet: origen, evolución y estado actual · Conceptos elementales sobre protocolos y servicios en Internet · Funcionalidades básicas de los navegadores web.

    En 2026 se preguntó por la **VPN**, el **DNS** y el **DHCP**. La seguridad (malware, phishing, malvertising) está en el [tema II-5]({{base}}auxiliar/temario/b2-05-informatica-basica/), y si quieres más profundidad en redes, en el [temario de TAI]({{base}}temario/sistemas/).

## 1. Origen, evolución y estado actual

**Internet** es una **red de redes** de alcance mundial, **descentralizada**, que conecta millones de redes y dispositivos usando un conjunto común de protocolos: **TCP/IP**.

| Año | Hito |
| --- | --- |
| **1969** | **ARPANET**, red del Departamento de Defensa de EE. UU. (agencia **ARPA**). Primera conexión entre la Universidad de California en Los Ángeles (UCLA) y el Instituto de Investigación de Stanford |
| **1971** | **Ray Tomlinson** envía el primer **correo electrónico** entre ordenadores conectados en red y elige la **@** |
| **1974** | **Vinton Cerf** y **Robert Kahn** publican el diseño de **TCP/IP** (por eso se les llama «padres de Internet») |
| **1 de enero de 1983** | ARPANET adopta **TCP/IP**. Se considera el **nacimiento de Internet** tal como la conocemos |
| **1983-1984** | Se diseña y pone en marcha el **DNS** (sistema de nombres de dominio) |
| **1988** | España registra el dominio **.es** |
| **1989-1991** | **Tim Berners-Lee**, en el **CERN** (Ginebra), crea la **World Wide Web**: **HTML**, **HTTP**, las **URL**, el primer navegador y el primer servidor web |
| **1993** | **Mosaic**, primer navegador gráfico popular. El CERN libera la Web para uso público |
| **1994** | Berners-Lee funda el **W3C** (World Wide Web Consortium), que fija los estándares de la Web |
| **1998** | Se crean **Google** e **ICANN** (organismo que coordina los nombres de dominio y las direcciones IP en todo el mundo) |
| **2000 en adelante** | **Web 2.0** (redes sociales, wikis, contenido de los usuarios), banda ancha, **móviles** (2007, el primer iPhone), **nube**, **Internet de las cosas** (IoT) e **inteligencia artificial** |

**Estado actual:** la mayoría de la población mundial está conectada; el acceso se hace sobre todo desde el **móvil** (4G y **5G**) y por **fibra óptica**. Coexisten **IPv4** e **IPv6**. En España, **Red.es** (entidad pública del Ministerio para la Transformación Digital y de la Función Pública) gestiona el registro de dominios **.es**. Para las Administraciones, la **Red SARA** conecta los organismos públicos entre sí y con la red europea (tema II-4).

## 2. Conceptos básicos

| Concepto | Qué es |
| --- | --- |
| **Dirección IP** | Número que **identifica** a cada dispositivo en la red. **IPv4**: 32 bits, cuatro números de 0 a 255 separados por puntos (`192.168.1.10`), unos 4.300 millones de direcciones, ya **agotadas**. **IPv6**: **128 bits**, en hexadecimal separado por dos puntos (`2001:db8::1`) |
| **Dominio** | **Nombre** fácil de recordar que se traduce a una IP: `inap.es`. Se lee de derecha a izquierda: **dominio de primer nivel** (genérico, como **.com**, **.org**, **.net**; o **territorial**, como **.es**, **.eu**), luego el de segundo nivel (`inap`). Las webs de la AGE suelen usar **.gob.es** (tercer nivel bajo .es), como `hacienda.gob.es` |
| **URL** | Dirección completa de un recurso: `https://www.inap.es/procesos-selectivos`. Partes: **protocolo** (`https`), **nombre del servidor** (`www.inap.es`) y **ruta** del recurso |
| **Proveedor (ISP)** | La empresa que da **acceso** a Internet |
| **Servidor / cliente** | El **servidor** ofrece un servicio (una web, el correo); el **cliente** lo usa (el navegador) |
| **Ancho de banda** | Cantidad de datos por segundo (**Mbps**, **Gbps**). **Bajada**: recibir; **subida**: enviar |
| **LAN / WAN** | Red **local** (una oficina) / red de área **extensa** (Internet es la mayor WAN) |
| **Intranet / extranet** | Red **privada** de una organización con tecnología de Internet / la parte de la intranet abierta a usuarios externos autorizados (proveedores, colaboradores) |
| **Router** | Conecta la red local con Internet y **encamina** los paquetes |
| **Wifi** | Conexión **inalámbrica** a la red local |

## 3. Protocolos

Un **protocolo** es un conjunto de **reglas** que permite comunicarse a los equipos. Internet funciona con la familia **TCP/IP**:

- **IP** (*Internet Protocol*): **direcciona** y **encamina** los paquetes de datos hasta su destino.
- **TCP** (*Transmission Control Protocol*): divide los datos en **paquetes**, los **ordena** y comprueba que lleguen **todos** y **sin errores** (fiable). **UDP** es más rápido pero no garantiza la entrega (vídeo en directo, llamadas).

| Protocolo | Para qué | Puerto habitual |
| --- | --- | --- |
| **HTTP** | Transferir **páginas web** | 80 |
| **HTTPS** | HTTP **cifrado** con **TLS** (el **candado** del navegador): protege la información y garantiza la identidad de la web mediante un **certificado** | **443** |
| **FTP** / **SFTP** | **Transferir archivos** (SFTP, de forma segura) | 21 / 22 |
| **SMTP** | **Enviar** correo | 25 / 587 |
| **POP3** | **Descargar** el correo al equipo | 110 / 995 |
| **IMAP** | Leer el correo **sincronizado** con el servidor | 143 / 993 |
| **DNS** | **Traduce los nombres de dominio a direcciones IP** (es la «guía telefónica» de Internet) | 53 |
| **DHCP** | **Asigna automáticamente** una **dirección IP** (y la puerta de enlace y los DNS) a los equipos que se conectan a la red | 67 / 68 |
| **SSH** | Acceso **remoto seguro** a otro equipo por comandos | 22 |
| **Telnet** | Acceso remoto **sin cifrar** (obsoleto) | 23 |

!!! example "La diferencia entre DNS y DHCP"
    El **DHCP** te **da** una IP al conectarte a la red (es automático: no hace falta configurarla a mano). El **DNS** te dice **qué IP tiene** el nombre que escribes en el navegador.

**VPN** (*Virtual Private Network*, red privada virtual): crea un **túnel cifrado** a través de Internet para conectarse a una **red privada** como si se estuviera dentro de ella. Es lo que se usa para **teletrabajar** con acceso a los sistemas internos de la Administración.

## 4. Servicios de Internet

| Servicio | Qué ofrece |
| --- | --- |
| **World Wide Web** | Páginas enlazadas por **hipervínculos** (**hipertexto**), escritas en **HTML** y que se ven con un **navegador**. **La Web no es lo mismo que Internet**: es uno de sus servicios |
| **Correo electrónico** | Mensajes con adjuntos (tema II-11) |
| **Transferencia de archivos** | FTP, servicios de **almacenamiento en la nube** (OneDrive, Google Drive) |
| **Mensajería instantánea y videoconferencia** | Chat, llamadas y reuniones en tiempo real (Teams, Webex) |
| **Buscadores** | Localizan información (Google, Bing). Ojo: un **buscador** no es un **navegador** |
| **Redes sociales, foros y blogs** | Comunicación y contenidos de los usuarios |
| **Comercio y administración electrónicos** | Compras, banca y trámites en línea (sedes electrónicas, Cl@ve) |
| **Computación en la nube** | **SaaS** (aplicaciones listas para usar: Microsoft 365), **PaaS** (plataformas para desarrollar) e **IaaS** (infraestructura: servidores, almacenamiento) |
| **Streaming** | Audio y vídeo **sin descargarlos** por completo |

## 5. Navegadores web

Un **navegador** es el programa que **interpreta** el HTML y muestra las páginas web.

| Navegador | Empresa | Notas |
| --- | --- | --- |
| **Microsoft Edge** | Microsoft | El de **Windows 11**. Basado en **Chromium** desde **2020** |
| **Google Chrome** | Google | El más usado del mundo. Basado en Chromium |
| **Mozilla Firefox** | Fundación Mozilla | De **código abierto** |
| **Safari** | Apple | El de macOS e iPhone |
| **Opera**, **Brave** | — | También basados en Chromium |

**Internet Explorer** quedó **retirado** el **15 de junio de 2022**: para las webs antiguas que solo funcionan con él, Edge tiene el **Modo Internet Explorer** (**modo IE**).

### Funcionalidades básicas

- **Barra de direcciones:** escribir una **URL** o una búsqueda (Edge y Chrome combinan ambas: es la **omnibox**). El **candado** indica una conexión **HTTPS**.
- **Botones:** **Atrás**, **Adelante**, **Actualizar** y **Página principal** (Inicio).
- **Pestañas:** varias páginas en la misma ventana. Se pueden **anclar**, **agrupar** y, en Edge, poner en **vertical**.
- **Favoritos** (marcadores): guardar las páginas que se visitan a menudo; **Barra de favoritos**.
- **Historial:** las páginas visitadas. **Descargas:** los archivos bajados (en la carpeta **Descargas** por defecto).
- **Navegación privada:** **InPrivate** en Edge, **incógnito** en Chrome, **ventana privada** en Firefox. **No guarda** el historial, las **cookies** ni los datos de formularios **al cerrar** la ventana, pero **no te hace anónimo** (el proveedor, la empresa o la web pueden ver lo que haces).
- **Cookies:** pequeños archivos que guarda la web en el navegador para **recordar** datos (inicio de sesión, idioma, carrito). Las de **terceros** sirven sobre todo para **publicidad** y seguimiento. La normativa exige pedir **consentimiento** para las que no son técnicas.
- **Caché:** copia local de partes de las webs para que carguen **más rápido**.
- **Borrar datos de exploración:** historial, cookies, caché, contraseñas… (**Ctrl + Mayús + Supr**).
- **Extensiones** (complementos): añaden funciones (bloquear anuncios, traducir, gestores de contraseñas).
- **Sincronización:** con una cuenta (Microsoft, Google), los **favoritos, historial y contraseñas** se ven en todos los dispositivos.
- **Gestor de contraseñas**, **traductor**, **lector inmersivo** (Edge), **imprimir** o **guardar como PDF**, **zoom**, **modo de pantalla completa**.
- **Página de inicio** y **motor de búsqueda predeterminado**: se configuran en Configuración.

### Atajos de teclado (Edge y Chrome)

| Atajo | Acción |
| --- | --- |
| **Ctrl + T** | Nueva **pestaña** |
| **Ctrl + N** | Nueva **ventana** |
| **Ctrl + Mayús + N** | Ventana **InPrivate / incógnito** (en **Firefox**, **Ctrl + Mayús + P**) |
| **Ctrl + W** | **Cerrar** la pestaña |
| **Ctrl + Mayús + T** | **Reabrir** la última pestaña cerrada |
| **Ctrl + Tab** / **Ctrl + Mayús + Tab** | Pestaña siguiente / anterior |
| **Ctrl + D** | Añadir a **favoritos** |
| **Ctrl + H** | **Historial** |
| **Ctrl + J** | **Descargas** |
| **Ctrl + L** o **F6** | Ir a la **barra de direcciones** |
| **F5** o **Ctrl + R** | **Actualizar** |
| **Ctrl + F5** | Actualizar **sin usar la caché** |
| **Ctrl + F** | **Buscar** en la página |
| **Ctrl + P** | **Imprimir** |
| **Ctrl + +** / **Ctrl + −** / **Ctrl + 0** | Ampliar / reducir / zoom al 100 % |
| **F11** | **Pantalla completa** |
| **Alt + Inicio** | Ir a la página principal |
| **Ctrl + Mayús + Supr** | **Borrar datos** de exploración |

## Resumen

| Dato | Respuesta |
| --- | --- |
| Origen | ARPANET, 1969 |
| Nacimiento de Internet | 1-1-1983, adopción de TCP/IP |
| Creador de la Web | Tim Berners-Lee, CERN, 1989-1991 |
| Estándares de la Web | W3C (1994) |
| Dominios .es | Red.es |
| Nombre → IP | DNS |
| IP automática | DHCP |
| Túnel cifrado a una red privada | VPN |
| Web segura | HTTPS (puerto 443, TLS) |
| IPv6 | 128 bits |
| Navegación privada en Edge | InPrivate, Ctrl + Mayús + N |
| Reabrir pestaña cerrada | Ctrl + Mayús + T |
| Internet Explorer | Retirado en 2022; Modo IE en Edge |
