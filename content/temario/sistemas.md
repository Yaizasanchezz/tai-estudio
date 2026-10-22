---
title: Bloque IV · Sistemas y comunicaciones
description: Administración de SO y BBDD, backup, correo, contenedores, LAN, seguridad, OSI/TCP-IP, Internet y VPN.
order: 5
---

## IV.1 Administración del sistema operativo y del software de base

- **Tareas:** alta y baja de usuarios y grupos, permisos, instalación y actualización de software y parches, gestión de servicios, planificación de tareas, monitorización de recursos, análisis de logs, copias de seguridad y documentación.
- **Linux:** gestión de paquetes con `apt` (Debian/Ubuntu) o `dnf`/`yum` (Red Hat); servicios con `systemctl start|stop|enable|status`; logs con `journalctl` y en /var/log; tareas programadas con **cron** (`crontab -e`); usuarios con `useradd`, `usermod`, `passwd`; ficheros /etc/passwd, /etc/shadow (contraseñas cifradas) y /etc/group.
- **Formato cron:** minuto, hora, día del mes, mes, día de la semana. `30 2 * * 1-5 /opt/backup.sh` ejecuta la copia a las 02:30 de lunes a viernes.
- **Windows Server:** Active Directory (dominios, unidades organizativas, directivas de grupo o GPO), servicios, Visor de eventos, Programador de tareas, PowerShell, WSUS para actualizaciones.
- **Software de base:** controladores, firmware, servidores web y de aplicaciones (Apache, Nginx, IIS, Tomcat), máquinas virtuales Java, bases de datos.
- **Mantenimiento y reparación:** gestión de cambios y de parches (probar en preproducción antes de producción), arranque en modo seguro o de rescate, restauración del sistema.

## IV.2 Administración de bases de datos, almacenamiento, virtualización y copias de seguridad

- **Funciones del DBA:** instalación y configuración del SGBD, seguridad (usuarios, roles, privilegios), copias de seguridad, rendimiento (índices, planes de ejecución, estadísticas), alta disponibilidad (réplicas, clústeres) y control de la integridad.
- **Tipos de copia:** **completa** (todo); **incremental** (lo cambiado desde la última copia de cualquier tipo: rápida de hacer, lenta de restaurar porque se necesita la completa y todas las incrementales); **diferencial** (lo cambiado desde la última completa: crece cada día, pero solo se necesitan la completa y la última diferencial).
- **Conceptos:** regla **3-2-1** (3 copias, en 2 soportes distintos, 1 fuera de las instalaciones); **RPO** (pérdida de datos máxima tolerable, en tiempo) y **RTO** (tiempo máximo para recuperar el servicio); copia en frío y en caliente; copias inmutables contra ransomware.
- **RAID:**

| Nivel | Funcionamiento | Discos mínimos | Tolera | Capacidad útil |
| --- | --- | --- | --- | --- |
| RAID 0 | Striping (reparto) sin redundancia | 2 | Ningún fallo | 100 % |
| RAID 1 | Espejo | 2 | 1 disco | 50 % |
| RAID 5 | Striping con paridad distribuida | 3 | 1 disco | (n−1)/n |
| RAID 6 | Doble paridad distribuida | 4 | 2 discos | (n−2)/n |
| RAID 10 (1+0) | Espejos unidos con striping | 4 | 1 disco por espejo | 50 % |

- **Almacenamiento:** DAS (conectado directamente al servidor), **NAS** (almacenamiento en red a nivel de fichero: NFS, SMB/CIFS) y **SAN** (red dedicada a nivel de bloque: Fibre Channel, iSCSI). Almacenamiento de objetos (tipo S3), deduplicación, *thin provisioning*, snapshots.
- **Virtualización de servidores:** hipervisor **tipo 1 o nativo** (sobre el hardware: VMware ESXi, Microsoft Hyper-V, KVM, Xen) y **tipo 2 o alojado** (sobre un SO anfitrión: VirtualBox, VMware Workstation). Migración en caliente (vMotion), alta disponibilidad, plantillas.
- **Virtualización del puesto:** VDI (escritorios virtuales en el CPD), virtualización de aplicaciones. Nube: IaaS, PaaS y SaaS; nube pública, privada, híbrida (en la AGE, servicios en la nube SARA).

Ejemplo resuelto: RAID 5 con 4 discos de 2 TB da 6 TB útiles (3 × 2) y soporta el fallo de 1 disco. Con RAID 6 serían 4 TB útiles y soportaría 2 fallos.

Ejemplo de copias: completa el domingo, incrementales de lunes a viernes. Si el disco falla el jueves, se restauran la completa del domingo y las incrementales del lunes, martes y miércoles. Con diferenciales, bastaría la completa y la diferencial del miércoles.

## IV.3 Servidores de correo, contenedores y microservicios

- **Componentes del correo:** MUA (cliente: Outlook, Thunderbird), MTA (transfiere: Postfix, Exchange, Sendmail), MDA (entrega en el buzón) y MSA (recibe el envío del cliente).

| Protocolo | Función | Puertos |
| --- | --- | --- |
| SMTP | Envío y transferencia entre servidores | 25 (entre servidores), 587 (envío con STARTTLS), 465 (SMTPS) |
| POP3 | Descarga del buzón al cliente (normalmente borra del servidor) | 110 / 995 (TLS) |
| IMAP | Acceso al buzón sincronizado en el servidor (carpetas) | 143 / 993 (TLS) |

- **DNS y seguridad del correo:** registro **MX** (servidor de correo del dominio); **SPF** (IP autorizadas a enviar en nombre del dominio); **DKIM** (firma criptográfica del mensaje); **DMARC** (política ante fallos de SPF/DKIM e informes). MIME para adjuntos; S/MIME y PGP para cifrar y firmar.
- **Contenedores (Docker):** virtualización a nivel de sistema operativo; los contenedores comparten el núcleo del anfitrión y son más ligeros que las máquinas virtuales. Conceptos: imagen (plantilla de solo lectura por capas), contenedor (instancia en ejecución), **Dockerfile** (receta de construcción: FROM, RUN, COPY, EXPOSE, CMD), registro (Docker Hub o privado), volúmenes, redes, Docker Compose (varios contenedores).
- **Orquestación (Kubernetes):** clúster con nodos *control plane* y *workers*; **pod** (unidad mínima, uno o varios contenedores), Deployment (réplicas y actualizaciones progresivas), Service (punto de acceso estable y balanceo), Ingress, ConfigMap y Secret, namespaces; `kubectl` como herramienta de línea de comandos. OpenShift es la distribución de Red Hat.
- **Microservicios:** cada servicio, una función de negocio con su propia base de datos; API Gateway, *service mesh*, circuit breaker, observabilidad (logs, métricas, trazas).

Ejemplo práctico: un correo enviado desde la AGE a un Gmail viaja así: cliente (MUA) → SMTP 587 → MTA del Ministerio → consulta del registro MX de gmail.com → SMTP 25 → MTA de Google → MDA → el destinatario lo lee por IMAP 993. Si el dominio no tiene SPF, DKIM y DMARC, es probable que el mensaje acabe en spam.

## IV.4 Administración de redes de área local

- **Gestión de usuarios y dispositivos:** servicios de directorio (**LDAP** puerto 389 / LDAPS 636, Active Directory), autenticación centralizada (**802.1X** con RADIUS), inventario de equipos, gestión de puestos (SCCM/Intune, MDM).
- **DHCP:** asigna IP, máscara, puerta de enlace y DNS. Proceso **DORA**: Discover, Offer, Request, Acknowledge. Puertos UDP 67 (servidor) y 68 (cliente). Concesiones (*lease*) y reservas por MAC.
- **DNS:** traduce nombres a IP; puerto 53 (UDP y TCP). Registros A (IPv4), AAAA (IPv6), CNAME (alias), MX (correo), NS (servidores del dominio), PTR (resolución inversa), TXT (SPF, verificaciones), SOA. DNSSEC firma las respuestas.
- **VLAN (IEEE 802.1Q):** dividen un switch en redes lógicas separadas; enlaces troncales (*trunk*) que llevan varias VLAN etiquetadas. Para comunicar VLAN hace falta un router o un switch de capa 3.
- **Monitorización:** **SNMP** (UDP 161 para consultas, 162 para *traps*; versión 3 con autenticación y cifrado), herramientas Nagios, Zabbix, PRTG; análisis de tráfico con Wireshark, NetFlow/sFlow, puertos espejo (*port mirroring*). Syslog (UDP 514) para centralizar logs.
- **Control del tráfico:** QoS (priorizar voz y vídeo), listas de control de acceso (ACL), limitación de ancho de banda, **STP** (Spanning Tree, evita bucles en capa 2).

Ejemplo práctico: un equipo nuevo obtiene la IP 169.254.x.x. Es una dirección APIPA: el equipo no ha recibido respuesta del servidor DHCP. Se comprueba el cable o la VLAN del puerto y el estado del servicio DHCP.

## IV.5 Seguridad de los sistemas de información

- **Dimensiones:** confidencialidad, integridad y disponibilidad (tríada CIA), más autenticidad y trazabilidad (ENS).
- **Conceptos:** activo, amenaza, vulnerabilidad, impacto, **riesgo** (probabilidad × impacto) y salvaguarda. Metodología de análisis de riesgos de la Administración: **MAGERIT** (con la herramienta PILAR del CCN).
- **Seguridad física:** control de acceso al CPD, detección y extinción de incendios (gases inertes), climatización, SAI (UPS), grupos electrógenos, suelo técnico.
- **Seguridad lógica:** identificación y autenticación (algo que sabes, que tienes, que eres; MFA), control de acceso (DAC, MAC, RBAC), mínimo privilegio, cifrado, registros de auditoría.
- **Amenazas:** malware (virus, gusano, troyano, ransomware, spyware, rootkit, botnet), phishing y spear phishing, ingeniería social, DoS/DDoS, man-in-the-middle, inyección, fuerza bruta, amenazas persistentes avanzadas (APT), vulnerabilidades de día cero.
- **Criptografía:**

| Tipo | Claves | Ejemplos | Uso |
| --- | --- | --- | --- |
| Simétrica | Una clave compartida | AES (128/192/256 bits), ChaCha20; obsoletos DES y 3DES | Cifrar grandes volúmenes de datos |
| Asimétrica | Pública y privada | RSA, curvas elípticas (ECC), Diffie-Hellman (intercambio de claves) | Intercambio de claves y firma digital |
| Hash | Sin clave | SHA-256, SHA-3; inseguros MD5 y SHA-1 | Integridad, almacenar contraseñas (con salt) |

- **Firma digital:** se calcula el hash del documento y se cifra con la **clave privada del firmante**. El receptor lo descifra con la **clave pública** del firmante y compara hashes. Garantiza autenticidad, integridad y no repudio (no confidencialidad).
- **Cifrado para confidencialidad:** se cifra con la **clave pública del destinatario**; solo él lo descifra con su privada.
- **PKI:** autoridad de certificación (CA), autoridad de registro (RA), certificados X.509, listas de revocación (CRL) y consulta en línea (OCSP).
- **CPD (TIA-942 / Uptime Institute):** Tier I (básico, 99,671 %), Tier II (componentes redundantes, 99,741 %), Tier III (mantenimiento concurrente, 99,982 %) y Tier IV (tolerante a fallos, 99,995 %).
- **Gestión de incidencias:** ITIL (incidencia frente a problema, mesa de ayuda o *service desk*, acuerdos de nivel de servicio o SLA); respuesta a incidentes de seguridad (preparación, detección, contención, erradicación, recuperación, lecciones aprendidas). CERT de referencia: **CCN-CERT** (sector público) e **INCIBE-CERT** (ciudadanos y empresas). Herramientas del CCN: LUCIA (gestión de incidentes), PILAR, CLARA, MicroClaudia, INES.
- **Control remoto:** herramientas de asistencia remota con consentimiento del usuario, conexión cifrada y registro de sesiones.

Ejemplo práctico: Ana quiere enviar a Luis un PDF firmado y confidencial. Firma con su clave privada (Luis verifica con la pública de Ana) y cifra con la clave pública de Luis (solo Luis lo abre con su privada). En la práctica se cifra el documento con AES y solo la clave AES se cifra con RSA (cifrado híbrido).

## IV.6 Comunicaciones: medios, equipos y redes móviles e inalámbricas

- **Medios guiados:** par trenzado (UTP, FTP, STP; categorías 5e = 1 Gbit/s, 6 = 1 Gbit/s y 10 Gbit/s hasta 55 m, 6A = 10 Gbit/s a 100 m, 8 = 25/40 Gbit/s a 30 m; conector RJ45; longitud máxima 100 m), coaxial y **fibra óptica** (monomodo: núcleo de ~9 µm, láser, largas distancias; multimodo: núcleo de 50/62,5 µm, LED o VCSEL, distancias cortas). La fibra es inmune a interferencias electromagnéticas.
- **Medios no guiados:** radio, microondas, satélite (GEO, a 36.000 km, con más latencia, y LEO como Starlink), infrarrojos.
- **Modos de transmisión:** símplex (un sentido, como la radio), semidúplex (ambos sentidos, pero no a la vez, como un walkie-talkie) y dúplex completo (ambos a la vez, como el teléfono).
- **Conmutación:** de circuitos (camino dedicado: telefonía clásica) y de paquetes (datagramas como IP, o circuitos virtuales como MPLS). Multiplexación por división de tiempo (TDM), frecuencia (FDM) y longitud de onda (WDM, en fibra).
- **Equipos:** módem, repetidor, hub, switch, router, punto de acceso, firewall, balanceador.
- **Redes móviles:** 2G GSM (voz digital, SMS), 2.5G GPRS, 3G UMTS, 4G **LTE** (todo IP), **5G** (alta velocidad, muy baja latencia, IoT masivo; *network slicing*).
- **Wi-Fi (IEEE 802.11):** 802.11n = Wi-Fi 4 (2,4 y 5 GHz); 802.11ac = Wi-Fi 5 (5 GHz); 802.11ax = Wi-Fi 6 (y Wi-Fi 6E en 6 GHz); 802.11be = Wi-Fi 7. Seguridad: WEP (rota), WPA, **WPA2** (AES-CCMP), **WPA3** (SAE); modo Personal (PSK) y Enterprise (802.1X/RADIUS).
- **Otras inalámbricas:** Bluetooth (802.15.1, corto alcance), Zigbee (802.15.4, IoT), NFC (centímetros, pagos y DNIe), RFID, LoRaWAN.

## IV.7 Modelos OSI y TCP/IP

| Capa OSI | Nº | Función | Protocolos y equipos | Capa TCP/IP |
| --- | --- | --- | --- | --- |
| Aplicación | 7 | Servicios al usuario | HTTP, FTP, SMTP, DNS, SSH, SNMP | Aplicación |
| Presentación | 6 | Formato, cifrado, compresión | TLS (en parte), JPEG, ASCII | Aplicación |
| Sesión | 5 | Diálogo entre aplicaciones | RPC, NetBIOS | Aplicación |
| Transporte | 4 | Extremo a extremo, puertos | TCP, UDP (unidad: segmento) | Transporte |
| Red | 3 | Direccionamiento lógico y encaminamiento | IP, ICMP, OSPF, BGP; router (paquete) | Internet |
| Enlace | 2 | Tramas, direccionamiento físico (MAC) | Ethernet, Wi-Fi, PPP, ARP; switch (trama) | Acceso a red |
| Física | 1 | Bits sobre el medio | Cables, conectores; hub, repetidor | Acceso a red |

Truco para recordar las capas de abajo arriba: "**F**ísica, **E**nlace, **R**ed, **T**ransporte, **S**esión, **P**resentación, **A**plicación" → "Fe-Re-Tra-Se-Pre-A".

- **TCP:** orientado a conexión, fiable (acuses de recibo, retransmisión, control de flujo con ventana deslizante, control de congestión). Conexión en tres pasos (*three-way handshake*): **SYN → SYN-ACK → ACK**; cierre con FIN. **UDP:** sin conexión, sin garantías, más rápido (DNS, DHCP, VoIP, streaming, SNMP).
- **Puertos bien conocidos (0–1023):** 20/21 FTP, 22 SSH/SFTP, 23 Telnet, 25 SMTP, 53 DNS, 67/68 DHCP, 80 HTTP, 110 POP3, 123 NTP, 143 IMAP, 161/162 SNMP, 389 LDAP, 443 HTTPS, 445 SMB, 3306 MySQL, 3389 RDP, 5432 PostgreSQL.
- **IPv4:** 32 bits. Clases históricas: A (1–126, /8), B (128–191, /16), C (192–223, /24), D (224–239, multicast), E (240–255, experimental). 127.0.0.0/8 es loopback.
- **Rangos privados (RFC 1918):** 10.0.0.0/8, 172.16.0.0/12 (172.16 a 172.31) y 192.168.0.0/16. Se traducen a IP pública con **NAT/PAT**.
- **IPv6:** 128 bits en 8 grupos hexadecimales de 16 bits; se omiten los ceros a la izquierda y una sola secuencia de grupos a cero se sustituye por `::`. Sin broadcast (usa multicast y anycast); autoconfiguración SLAAC; ::1 es loopback; fe80::/10 son direcciones de enlace local.
- **Otros protocolos:** ARP (de IP a MAC), ICMP (ping, traceroute), protocolos de encaminamiento interior (RIP por vector distancia, OSPF por estado de enlace) y exterior (BGP).

**Ejemplo resuelto de subnetting.** Red 192.168.10.0/24 que hay que dividir en 4 subredes iguales:

- Se toman 2 bits de host → máscara /26 = 255.255.255.192. Cada subred tiene 2⁶ = 64 direcciones y 62 hosts útiles.
- Subredes: 192.168.10.0/26, .64/26, .128/26 y .192/26.
- Para la segunda subred (.64/26): primer host .65, último host .126, broadcast .127.
- Fórmula: hosts útiles = 2ʰ − 2, donde h es el número de bits de host. Una /27 tiene 30 hosts; una /28, 14; una /30, 2 (enlaces punto a punto).

## IV.8 Internet: arquitectura, servicios y protocolos HTTP, HTTPS y TLS

- **Historia:** ARPANET (1969, Departamento de Defensa de EE. UU.); adopción de TCP/IP el 1 de enero de 1983; la World Wide Web, de Tim Berners-Lee en el CERN (1989–1991).
- **Gobernanza:** ICANN e IANA (nombres, números y puertos), IETF (estándares RFC), W3C (estándares web), registros regionales (RIPE NCC en Europa). En España, el dominio .es lo gestiona Red.es.
- **Servicios:** web, correo, DNS, transferencia de ficheros (FTP, SFTP), mensajería, VoIP, streaming, CDN.
- **HTTP:** protocolo cliente-servidor sin estado. Versiones: HTTP/1.1 (conexiones persistentes), **HTTP/2** (binario, multiplexación, compresión de cabeceras), **HTTP/3** (sobre QUIC, que usa UDP).
- **Métodos:** GET, POST, PUT, PATCH, DELETE, HEAD (solo cabeceras), OPTIONS (métodos admitidos, CORS).
- **Códigos de estado:** 1xx informativos; **2xx** éxito (200 OK, 201 Created, 204 No Content); **3xx** redirección (301 permanente, 302 temporal, 304 Not Modified); **4xx** error del cliente (400 Bad Request, 401 no autenticado, 403 prohibido, 404 no encontrado, 429 demasiadas peticiones); **5xx** error del servidor (500 error interno, 502 Bad Gateway, 503 servicio no disponible, 504 Gateway Timeout).
- **HTTPS:** HTTP sobre TLS, puerto 443. **TLS** sustituye a SSL (SSL 2.0 y 3.0 y TLS 1.0 y 1.1 están obsoletos; se usan **TLS 1.2 y 1.3**). El handshake negocia el algoritmo de cifrado, el servidor presenta su certificado X.509 y se acuerda una clave de sesión simétrica. TLS 1.3 reduce el handshake a 1 RTT y exige secreto perfecto hacia adelante (*forward secrecy*). HSTS obliga al navegador a usar siempre HTTPS.

Ejemplo práctico: un usuario pulsa en un enlace a una página que se ha movido para siempre. El servidor responde 301 con una cabecera Location; el navegador repite la petición en la nueva URL y obtiene 200.

## IV.9 Seguridad en redes

- **Seguridad perimetral:** cortafuegos de filtrado de paquetes (sin estado), con inspección de estado (*stateful*), de aplicación o proxy, de nueva generación (NGFW) y de aplicaciones web (**WAF**, contra inyección y XSS).
- **DMZ:** zona desmilitarizada donde se colocan los servidores accesibles desde Internet (web, correo), separada de la red interna.
- **IDS/IPS:** detección (alerta) frente a prevención (bloquea); basados en firmas o en anomalías; de red (NIDS) o de host (HIDS). SIEM para correlacionar eventos.
- **Proxy:** directo (los usuarios salen a Internet a través de él; filtrado y caché) e inverso (delante de los servidores; balanceo, terminación TLS).
- **Acceso remoto seguro:** **SSH** (puerto 22; autenticación por clave pública), RDP (3389, nunca expuesto directamente a Internet), escritorios remotos a través de pasarelas.
- **VPN:** **IPsec** (capa 3; AH da autenticación e integridad; **ESP** añade cifrado; modo transporte, solo la carga útil, frente a modo túnel, el paquete completo; IKE para negociar claves), VPN SSL/TLS (por navegador o cliente), WireGuard. Tipos: sitio a sitio y acceso remoto (teletrabajo).
- **Puesto de usuario:** antivirus y EDR, actualizaciones automáticas, cortafuegos local, cifrado de disco (BitLocker), usuario sin privilegios de administrador, bloqueo de USB, formación contra phishing. Enfoque de **confianza cero** (*Zero Trust*): no confiar por estar dentro de la red; verificar siempre.

Ejemplo práctico: una Delegación del Gobierno publica su web. El servidor web va en la DMZ detrás de un WAF; el cortafuegos permite desde Internet solo 443 hacia la DMZ y bloquea cualquier conexión directa de Internet a la red interna; el personal en teletrabajo entra por VPN con doble factor.

## IV.10 Redes locales: tipología, transmisión, acceso e interconexión

- **Topologías:** bus, **estrella** (la habitual con switch central; si falla el centro cae todo), anillo, malla (total o parcial; muy redundante), árbol o jerárquica.
- **Clasificación por alcance:** PAN, LAN, MAN, WAN.
- **Ethernet (IEEE 802.3):** trama con MAC de destino y de origen (48 bits), tipo, datos (46–1500 bytes, MTU 1500) y FCS (CRC). Estándares 10BASE-T, 100BASE-TX (Fast Ethernet), 1000BASE-T (Gigabit sobre cobre), 10GBASE-T, y sus equivalentes en fibra (1000BASE-SX/LX…).
- **Métodos de acceso al medio:** **CSMA/CD** (detección de colisiones, Ethernet semidúplex clásica; con switches en dúplex completo ya no hay colisiones), **CSMA/CA** (evitación de colisiones, Wi-Fi), paso de testigo (Token Ring 802.5, FDDI).
- **Técnicas de transmisión:** banda base (señal digital directa, Ethernet) frente a banda ancha (modulación sobre portadora); codificaciones Manchester, 4B/5B, 8B/10B; PoE (802.3af/at/bt) para alimentar teléfonos IP y puntos de acceso por el cable de red.
- **Dispositivos de interconexión:**

| Dispositivo | Capa OSI | Qué hace |
| --- | --- | --- |
| Repetidor / hub | 1 | Regenera y reenvía la señal a todos los puertos (un único dominio de colisión) |
| Puente (bridge) / switch | 2 | Reenvía tramas según la tabla de direcciones MAC; cada puerto es un dominio de colisión |
| Switch de capa 3 / router | 3 | Encamina paquetes entre redes según la IP; separa dominios de difusión |
| Pasarela (gateway) | 4–7 | Traduce entre protocolos o arquitecturas distintas |

Ejemplo práctico: en una oficina con un hub de 8 puertos, todos los equipos comparten un dominio de colisión. Al cambiarlo por un switch hay 8 dominios de colisión y un único dominio de difusión; para separar la difusión de dos departamentos se crean dos VLAN o se pone un router.
