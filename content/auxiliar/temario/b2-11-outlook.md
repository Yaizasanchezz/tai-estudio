---
title: Tema II-11 · Correo electrónico: Outlook 365
description: Conceptos elementales y funcionamiento. El entorno de trabajo. Enviar, recibir, responder y reenviar mensajes. Creación de mensajes. Reglas de mensaje. Libreta de direcciones.
order: 211
---

!!! tip "Qué pide el programa"
    Correo electrónico: Outlook 365 · Conceptos elementales y funcionamiento · El entorno de trabajo · Enviar, recibir, responder y reenviar mensajes · Creación de mensajes · Reglas de mensaje · Libreta de direcciones.

    Se pregunta sobre **Outlook de escritorio** de Microsoft 365. Microsoft está sustituyendo el Outlook clásico por el **nuevo Outlook para Windows**; algunos menús cambian de sitio, pero las funciones son las mismas. En 2026 cayeron preguntas de **Retrasar entrega**, **Recuperar mensaje**, **Cifrar**, el **Asistente para programación** y las **@menciones**.

## 1. Conceptos elementales

- **Correo electrónico:** servicio para **enviar y recibir mensajes** con archivos adjuntos a través de una red.
- **Dirección:** `usuario@dominio` (por ejemplo, `nombre.apellido@correo.gob.es`). La **@** separa el usuario del dominio.
- **Cliente de correo:** el programa con el que se gestiona el correo (**Outlook**); también existe el **correo web** (Outlook en la web, Gmail).
- **Servidor de correo:** guarda los buzones y entrega los mensajes. En las organizaciones con Microsoft 365, **Exchange Online**.

| Protocolo | Función |
| --- | --- |
| **SMTP** | **Enviar** los mensajes |
| **POP3** | **Descargar** los mensajes al equipo (normalmente los **borra** del servidor) |
| **IMAP** | Leer los mensajes **sincronizados** con el servidor (se ven igual desde cualquier dispositivo) |
| **Exchange** (MAPI) | El de Microsoft: sincroniza correo, **calendario**, **contactos** y tareas |

**Archivos de datos de Outlook:** **.pst** (*Personal Storage Table*: copia local de correo, contactos y calendario, para cuentas POP o para **archivar**) y **.ost** (copia **sin conexión** de un buzón de Exchange o IMAP). Un mensaje guardado suelto es un **.msg**.

## 2. El entorno de trabajo

| Elemento | Qué es |
| --- | --- |
| **Barra de navegación** | Cambia entre **Correo**, **Calendario**, **Contactos** (Personas) y **Tareas** (Microsoft To Do). En la versión actual está a la izquierda |
| **Panel de carpetas** | **Bandeja de entrada**, **Borradores**, **Elementos enviados**, **Elementos eliminados**, **Correo no deseado**, **Bandeja de salida**, **Archivo**… Se pueden crear **carpetas** propias y marcar **Favoritos** |
| **Lista de mensajes** | Los mensajes de la carpeta. La **Bandeja de entrada Prioritarios** separa lo importante (**Prioritarios**) del resto (**Otros**) |
| **Panel de lectura** | Muestra el mensaje seleccionado sin abrirlo |
| **Cinta de opciones** | Fichas **Archivo**, **Inicio**, **Enviar y recibir**, **Carpeta**, **Vista**, **Ayuda** |
| **Buscar** | Cuadro de búsqueda arriba, con filtros (de, asunto, con datos adjuntos…) |

## 3. Enviar, recibir, responder y reenviar

| Acción | Cómo | Qué pasa |
| --- | --- | --- |
| **Nuevo mensaje** | Inicio > **Nuevo correo electrónico** (**Ctrl + Mayús + M** desde cualquier vista) | Se abre una ventana de mensaje |
| **Enviar** | Botón **Enviar** (**Alt + S** o **Ctrl + Intro**) | Pasa por la **Bandeja de salida** y, una vez enviado, queda en **Elementos enviados** |
| **Enviar y recibir** | Ficha Enviar y recibir (**F9**) | Comprueba si hay mensajes nuevos y envía los pendientes |
| **Responder** | **Ctrl + R** | Contesta **solo al remitente**; el asunto empieza por **RE:**. **No** incluye los adjuntos originales |
| **Responder a todos** | **Ctrl + Mayús + R** | Contesta al remitente y a **todos los destinatarios** (Para y CC, nunca a los CCO) |
| **Reenviar** | **Ctrl + F** | Envía el mensaje **a otras personas**, **con sus adjuntos**; el asunto empieza por **RV:** |

**Cambiar de vista:** **Ctrl + 1** Correo, **Ctrl + 2** Calendario, **Ctrl + 3** Contactos, **Ctrl + 4** Tareas.

## 4. Creación de mensajes

| Campo u opción | Uso |
| --- | --- |
| **Para** | Destinatarios principales |
| **CC** (copia de carbón) | Destinatarios **en copia**, a título informativo. Todos los ven |
| **CCO** (copia de carbón oculta) | Destinatarios **ocultos**: los demás **no los ven**. Útil para envíos masivos (protege las direcciones) |
| **Asunto** | Resumen del mensaje |
| **Cuerpo** | Formatos: **HTML** (el habitual), **texto enriquecido** o **texto sin formato** |
| **Adjuntar archivo** | Archivos (o **vínculos** a OneDrive en lugar de copias). Hay un **límite de tamaño** (en Microsoft 365, normalmente unos 20–25 MB) |
| **Firma** | Texto automático al final (Archivo > Opciones > Correo > Firmas) |
| **Importancia** | **Alta** o **baja** (ficha Mensaje) |
| **Confirmaciones** | **De entrega** y **de lectura** (Opciones > Seguimiento) |
| **@menciones** | Escribir **@** y el nombre de alguien de la organización **resalta** su nombre y lo **añade al campo Para** |

**Opciones del mensaje (ficha Opciones):**

- **Retrasar entrega:** **Opciones > Más opciones > Retrasar entrega** y marcar **«No entregar antes de»** una fecha y hora. Así se **programa** el envío.
- **Dirigir respuestas a:** que las respuestas vayan a otra dirección.
- **Botones de voto** (Aprobar / Rechazar…).
- **Cifrar:** **Cifrar solo** (solo lo leen los destinatarios) o **No reenviar** (el destinatario **no puede reenviar, imprimir ni copiar** el mensaje). Es la protección de Microsoft Purview (IRM).

**Recuperar un mensaje enviado:** desde el mensaje en **Elementos enviados** > **Archivo > Información > Volver a enviar o recuperar > Recuperar este mensaje** (eliminar las copias no leídas o sustituirlas por otro mensaje). Solo funciona si remitente y destinatario tienen cuentas de **Microsoft 365/Exchange en la misma organización** y el destinatario **no lo ha abierto**. El nuevo Outlook y Outlook en la web tienen además **«Deshacer envío»** (unos segundos de margen).

**Organizar el correo:** **marcas** de seguimiento (para hoy, mañana…, con aviso), **categorías** de colores, **anclar**, **Limpiar** conversaciones, **Archivar**, **Pasos rápidos** (varias acciones con un clic), **Correo no deseado** (remitentes bloqueados y seguros) y **Respuestas automáticas** («fuera de la oficina», en **Archivo > Respuestas automáticas**).

## 5. Reglas de mensaje

Las **reglas** hacen automáticamente algo con los mensajes que cumplen unas **condiciones**. Se crean en **Inicio > Reglas > Crear regla** (a partir de un mensaje) o en **Administrar reglas y alertas**.

| Parte de la regla | Ejemplos |
| --- | --- |
| **Condiciones** | De una persona, con unas palabras en el asunto, enviado solo a mí, con datos adjuntos, de importancia alta |
| **Acciones** | **Mover a una carpeta**, copiar, eliminar, reenviar, marcar, asignar una categoría, reproducir un sonido, mostrar una alerta |
| **Excepciones** | Salvo si… |

Las reglas pueden ejecutarse en el **servidor** (funcionan aunque Outlook esté cerrado) o **solo en el cliente**. Se pueden **ejecutar ahora** sobre los mensajes que ya hay en una carpeta.

## 6. Libreta de direcciones y contactos

- **Libreta de direcciones** (**Ctrl + Mayús + B** o botón **Para…**): busca destinatarios en la **Lista global de direcciones** (**GAL**, todos los usuarios de la organización), en los **Contactos** propios y en otras listas.
- **Contactos** (Personas): fichas con nombre, correos, teléfonos, empresa, dirección… Se pueden **importar y exportar** (CSV, PST).
- **Grupos de contactos** (antes, listas de distribución): un nombre que agrupa varias direcciones para escribir a todas a la vez.
- **Autocompletar:** Outlook sugiere direcciones usadas antes mientras se escribe.

## 7. El calendario

- **Cita:** algo que se apunta en el **propio** calendario. **Reunión:** cita con **asistentes** a los que se envía una **convocatoria** (pueden **aceptar, rechazar** o proponer otra hora). **Evento:** dura **todo el día**.
- **Asistente para programación:** muestra la **disponibilidad** (libre u ocupado) de los asistentes para elegir una hora que vaya bien a todos.
- **Periodicidad** (diaria, semanal…), **recordatorios**, reunión de **Teams** integrada, **compartir** el calendario y ver los de los compañeros.
- Las **tareas** se gestionan con **Microsoft To Do**, integrado en Outlook (listas de tareas sincronizadas).

## Resumen

| Dato | Respuesta |
| --- | --- |
| Protocolo de envío | SMTP |
| Responder a todos | Ctrl + Mayús + R (no llega a los CCO) |
| Reenviar | Ctrl + F (incluye los adjuntos) |
| Destinatarios ocultos | CCO |
| Programar un envío | Opciones > Retrasar entrega > No entregar antes de |
| Recuperar un mensaje | Misma organización Microsoft 365 y no leído |
| Impedir reenviar e imprimir | Cifrar > No reenviar |
| Ver la disponibilidad de los asistentes | Asistente para programación |
| @mención | Resalta el nombre y lo añade a Para |
| Archivo de datos local | .pst |
