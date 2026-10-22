---
title: ENS · Esquema Nacional de Seguridad (RD 311/2022)
description: Principios básicos, requisitos mínimos, roles, categorización de sistemas, las 73 medidas del anexo II, auditoría, conformidad y respuesta a incidentes, con el vocabulario del CCN.
order: 12
---

!!! tip "Lo que más cae"
    Los **7 principios básicos**, los **15 requisitos mínimos**, las **5 dimensiones** (C, I, T, A, D), las **3 categorías** (BÁSICA, MEDIA, ALTA), los **4 responsables**, la **auditoría cada 2 años** y la **división de medidas** en **org / op / mp**. Si te aprendes esta página, tienes la pregunta.

## Idea general

- **Norma:** **Real Decreto 311/2022, de 3 de mayo**, por el que se regula el Esquema Nacional de Seguridad. **Deroga** el **RD 3/2010** (el ENS original).
- **Base legal:** **art. 156.2 de la Ley 40/2015**: el ENS tiene por objeto establecer la **política de seguridad** en la utilización de medios electrónicos y está constituido por los **principios básicos y requisitos mínimos** que garanticen adecuadamente la seguridad de la información tratada.
- **Objeto (art. 1):** proteger la información y los servicios para asegurar el **acceso, la confidencialidad, la integridad, la trazabilidad, la autenticidad, la disponibilidad y la conservación** de los datos, la información y los servicios. Se integra en el **Sistema de Seguridad Nacional** (Ley 36/2015).
- **Títulos competenciales:** art. **149.1.18.ª** (bases del régimen jurídico de las AA. PP.), **21.ª** (telecomunicaciones) y **29.ª** (seguridad pública) de la Constitución.
- **Adecuación:** los sistemas existentes tuvieron **24 meses** para adaptarse (hasta mayo de 2024); los **nuevos** aplican el ENS **desde su concepción**.

## Ámbito de aplicación (art. 2)

- **Todo el sector público** (art. 2 Ley 40/2015).
- Los sistemas que tratan **información clasificada** (con medidas complementarias).
- **Novedad del 2022:** también las **entidades del sector privado** que **presten servicios o provean soluciones** a las entidades públicas, que deben tener **política de seguridad**. Los **pliegos** deben exigir la conformidad con el ENS (declaraciones o certificaciones), también en la **cadena de suministro**.
- **Datos personales (art. 3):** se aplican además el **RGPD y la LOPDGDD**. **Prevalecen** las medidas derivadas del **análisis de riesgos** y la **EIPD** del RGPD si son más exigentes.

## Los 7 principios básicos (arts. 5 a 11)

| Principio | Idea clave |
| --- | --- |
| **Seguridad como proceso integral** (art. 6) | La seguridad abarca **elementos humanos, materiales, técnicos, jurídicos y organizativos**. Excluye las **actuaciones puntuales**. Máxima atención a la **concienciación** |
| **Gestión de la seguridad basada en los riesgos** (art. 7) | El **análisis y la gestión de riesgos** es parte esencial y **continua**; reducir los riesgos a **niveles aceptables** con medidas **proporcionadas** |
| **Prevención, detección, respuesta y conservación** (art. 8) | **Prevenir** (disuasión, reducir la superficie de exposición), **detectar** ciberincidentes, **responder** para restaurar, y **conservar** los datos durante todo su ciclo de vida |
| **Existencia de líneas de defensa** (art. 9) | **Defensa en profundidad**: **múltiples capas** de seguridad **organizativas, físicas y lógicas**, para que si una falla se pueda reaccionar y minimizar el impacto |
| **Vigilancia continua** (art. 10) | Detectar **actividades o comportamientos anómalos** y responder a tiempo |
| **Reevaluación periódica** (art. 10) | **Reevaluar y actualizar** las medidas según evolucionen los riesgos |
| **Diferenciación de responsabilidades** (art. 11) | Distinguir **responsable de la información, del servicio, de la seguridad y del sistema**. La responsabilidad de la **seguridad** está **separada** de la de la **explotación** |

## Política de seguridad y los 15 requisitos mínimos (art. 12)

**Política de seguridad:** conjunto de **directrices** que rigen cómo una organización gestiona y protege su información y servicios. Contiene, al menos: **objetivos o misión**, **marco regulatorio**, **roles** de seguridad (deberes, responsabilidades, designación y renovación), **comités** de seguridad, directrices de la **documentación** y los **riesgos derivados del tratamiento de datos personales**.

- Cada **Administración** y cada entidad con personalidad jurídica propia tiene una política **formalmente aprobada** (los organismos pueden acogerse a la de su Administración matriz).
- En la **AGE**, **cada Ministerio** tiene la suya, aprobada por **su titular**.
- Los **municipios** pueden compartir una política común elaborada por la **Diputación** o la comarca.

**Los 15 requisitos mínimos:**

1. **Organización e implantación del proceso de seguridad.**
2. **Análisis y gestión de los riesgos** (con una **metodología reconocida internacionalmente**, como **MAGERIT**, con la herramienta **PILAR** del CCN).
3. **Gestión de personal.**
4. **Profesionalidad.**
5. **Autorización y control de los accesos.**
6. **Protección de las instalaciones.**
7. **Adquisición de productos de seguridad y contratación de servicios de seguridad** (preferencia por productos **certificados**, según el **Catálogo de Productos y Servicios de Seguridad TIC, CPSTIC**, del CCN).
8. **Mínimo privilegio.**
9. **Integridad y actualización del sistema.**
10. **Protección de la información almacenada y en tránsito.**
11. **Prevención ante otros sistemas de información interconectados.**
12. **Registro de la actividad y detección de código dañino.**
13. **Incidentes de seguridad.**
14. **Continuidad de la actividad.**
15. **Mejora continua del proceso de seguridad.**

Los requisitos se exigen **en proporción a los riesgos** de cada sistema; alguno puede obviarse en sistemas sin riesgos significativos.

## Los cuatro responsables (arts. 11 y 13)

| Rol | Qué hace |
| --- | --- |
| **Responsable de la información** | Determina los **requisitos de la información** tratada (y **valora** su nivel en cada dimensión) |
| **Responsable del servicio** | Determina los **requisitos de los servicios** prestados (y los valora) |
| **Responsable de la seguridad** | Determina las **decisiones para satisfacer los requisitos de seguridad**, **supervisa** la implantación de las medidas, **reporta** y **determina la categoría** del sistema |
| **Responsable del sistema** | **Desarrolla la forma concreta de implementar** la seguridad y **supervisa la operación diaria**; puede delegar en administradores y operadores |

!!! warning "Regla de oro"
    El **responsable de la seguridad** debe ser **distinto del responsable del sistema**, **sin dependencia jerárquica** entre ellos. Solo excepcionalmente, por falta justificada de recursos, pueden coincidir, aplicando **medidas compensatorias**.

- En los **servicios externalizados**, el prestador designa un **POC** (Punto o Persona de Contacto) de seguridad, aunque la **responsabilidad última** sigue siendo de la entidad pública.
- **Valoración y categoría (art. 41):** la **valoración** de cada dimensión la hacen los **responsables de la información y del servicio**; la **determinación de la categoría** del sistema, el **responsable de la seguridad**.

## Categorización de los sistemas (art. 40 y anexo I)

**Las 5 dimensiones de la seguridad:**

| Dimensión | Pregunta que responde |
| --- | --- |
| **[C] Confidencialidad** | ¿Accede solo quien está autorizado? |
| **[I] Integridad** | ¿La información está completa y sin alteraciones no autorizadas? |
| **[T] Trazabilidad** | ¿Se puede saber **quién hizo qué y cuándo**? |
| **[A] Autenticidad** | ¿Quien dice ser es quien es? ¿El origen es el que dice? |
| **[D] Disponibilidad** | ¿Está accesible cuando se necesita? |

**Niveles por dimensión**, según el perjuicio que causaría un incidente:

| Nivel | Perjuicio | Ejemplos de perjuicio |
| --- | --- | --- |
| **BAJO** | **Limitado** | Reducción **apreciable** de la capacidad; daño **menor**; incumplimiento **formal subsanable**; perjuicio molesto pero **fácilmente reparable** |
| **MEDIO** | **Grave** | Reducción **significativa**; daño **significativo**; incumplimiento **material** o formal no subsanable; perjuicio **de difícil reparación** |
| **ALTO** | **Muy grave** | **Anulación efectiva** de la capacidad; daño **muy grave o irreparable**; incumplimiento **grave**; perjuicio **de difícil o imposible reparación** |

**Categoría del sistema:** la del **nivel más alto** de cualquiera de sus dimensiones:

- **ALTA** si **alguna** dimensión es **ALTO**.
- **MEDIA** si alguna es **MEDIO** y **ninguna** es superior.
- **BÁSICA** si alguna es **BAJO** y ninguna es superior.

La categoría se **reevalúa anualmente** o cuando haya cambios significativos. Si un sistema trata varias informaciones y servicios, en cada dimensión toma el **nivel mayor**.

!!! example "Ejemplo de categorización"
    Un sistema de gestión de nóminas: confidencialidad **MEDIO** (datos económicos), integridad **MEDIO**, trazabilidad **BAJO**, autenticidad **MEDIO**, disponibilidad **BAJO** (puede esperar un día). Ninguna dimensión es ALTO y alguna es MEDIO → **categoría MEDIA**. Necesitará una **auditoría de certificación**, no basta la autoevaluación.

## Las medidas de seguridad (art. 28 y anexo II)

Se dividen en **tres grupos** y suman **73 medidas**:

| Grupo | Código | Qué protege | Nº de medidas |
| --- | --- | --- | --- |
| **Marco organizativo** | **org** | La **organización global** de la seguridad | **4** |
| **Marco operacional** | **op** | La **operación** del sistema como conjunto | **33** |
| **Medidas de protección** | **mp** | **Activos concretos** según su naturaleza | **36** |

**Marco organizativo [org]:** org.1 **Política de seguridad** · org.2 **Normativa de seguridad** · org.3 **Procedimientos de seguridad** · org.4 **Proceso de autorización**.

**Marco operacional [op]:**

| Familia | Medidas |
| --- | --- |
| **op.pl** Planificación | 1 Análisis de riesgos · 2 Arquitectura de seguridad · 3 Adquisición de nuevos componentes · 4 Dimensionamiento / gestión de la capacidad · 5 Componentes certificados |
| **op.acc** Control de acceso | 1 Identificación · 2 Requisitos de acceso · 3 **Segregación de funciones y tareas** · 4 Gestión de derechos de acceso · 5 Mecanismo de autenticación (usuarios **externos**) · 6 Mecanismo de autenticación (usuarios **de la organización**) |
| **op.exp** Explotación | 1 **Inventario de activos** · 2 Configuración de seguridad · 3 Gestión de la configuración · 4 Mantenimiento y actualizaciones · 5 Gestión de cambios · 6 Protección frente a **código dañino** · 7 Gestión de incidentes · 8 **Registro de la actividad** · 9 Registro de la gestión de incidentes · 10 Protección de **claves criptográficas** |
| **op.ext** Recursos externos | 1 Contratación y **acuerdos de nivel de servicio** · 2 Gestión diaria · 3 Protección de la **cadena de suministro** · 4 Interconexión de sistemas |
| **op.nub** Servicios en la nube | 1 Protección de servicios en la nube (**novedad de 2022**) |
| **op.cont** Continuidad del servicio | 1 **Análisis de impacto** · 2 **Plan de continuidad** · 3 Pruebas periódicas · 4 Medios alternativos |
| **op.mon** Monitorización | 1 **Detección de intrusión** · 2 Sistema de métricas · 3 **Vigilancia** |

**Medidas de protección [mp]:**

| Familia | Medidas |
| --- | --- |
| **mp.if** Instalaciones e infraestructuras | 1 Áreas separadas y con control de acceso · 2 Identificación de las personas · 3 Acondicionamiento de los locales · 4 Energía eléctrica · 5 Incendios · 6 Inundaciones · 7 Registro de entrada y salida de equipamiento |
| **mp.per** Gestión del personal | 1 Caracterización del puesto · 2 Deberes y obligaciones · 3 **Concienciación** · 4 **Formación** |
| **mp.eq** Protección de los equipos | 1 **Puesto de trabajo despejado** · 2 **Bloqueo** del puesto · 3 Dispositivos **portátiles** · 4 Otros dispositivos conectados a la red |
| **mp.com** Comunicaciones | 1 **Perímetro seguro** · 2 Confidencialidad · 3 Integridad y autenticidad · 4 **Separación de flujos** en la red |
| **mp.si** Soportes de información | 1 **Marcado** de soportes · 2 Criptografía · 3 Custodia · 4 Transporte · 5 **Borrado y destrucción** |
| **mp.sw** Aplicaciones informáticas | 1 Desarrollo de aplicaciones · 2 Aceptación y puesta en servicio |
| **mp.info** Información | 1 Datos personales · 2 **Calificación** de la información · 3 **Firma electrónica** · 4 **Sellos de tiempo** · 5 **Limpieza de documentos** (metadatos) · 6 **Copias de seguridad** |
| **mp.s** Servicios | 1 Protección del **correo electrónico** · 2 Servicios y **aplicaciones web** · 3 **Navegación web** · 4 Protección frente a la **denegación de servicio** |

- Cada medida se aplica según la **categoría** o el **nivel** de la dimensión, con **refuerzos** adicionales en los niveles superiores.
- **Declaración de Aplicabilidad:** documento **firmado por el responsable de la seguridad** con la relación de medidas seleccionadas. Las medidas son **mínimos** ampliables y pueden sustituirse por **medidas compensatorias** justificadas.
- **Perfiles de cumplimiento específicos (art. 30):** conjuntos de medidas adaptados a colectivos concretos (por ejemplo, para **Entidades Locales** o **universidades**) que publica el CCN.

## Auditoría y conformidad (arts. 31 y 38)

- **Auditoría regular ordinaria:** **al menos cada 2 años** (prorrogable **3 meses** por fuerza mayor). **Extraordinaria** cuando haya **modificaciones sustanciales**, y entonces reinicia el cómputo de los 2 años.
- El **informe de auditoría** se presenta al **responsable del sistema** y al **responsable de la seguridad**; este lo analiza y propone medidas correctoras al responsable del sistema. En categoría **ALTA**, el responsable del sistema puede **suspender** el servicio hasta subsanar las deficiencias graves.
- **Conformidad (art. 38 y anexo III):**

| Categoría | Cómo se acredita la conformidad |
| --- | --- |
| **BÁSICA** | **Autoevaluación** → **Declaración de Conformidad** |
| **MEDIA** y **ALTA** | **Auditoría formal** por una **entidad de certificación acreditada** → **Certificación de Conformidad** |

Las declaraciones y certificaciones, con su **distintivo de conformidad**, se **publican** en los portales o sedes.

## Incidentes de seguridad (arts. 25, 33 y 34)

- Cada entidad dispone de **procedimientos de gestión de incidentes**: mecanismos de **detección**, criterios de **clasificación**, análisis y resolución, comunicación y **registro**.
- **CCN-CERT:** la capacidad de respuesta a incidentes del **Centro Criptológico Nacional** (adscrito al **CNI**), que coordina la respuesta técnica de los **CSIRT** del sector público. Las entidades públicas le **notifican** los incidentes de **impacto significativo**.
- Tras un incidente, el **CCN-CERT** determina el **riesgo de reconexión**, y la **Secretaría General de Administración Digital** autoriza la reconexión a los medios y servicios comunes.
- **Servicios del CCN-CERT:** soporte y coordinación ante vulnerabilidades e incidentes, **guías CCN-STIC**, formación e **información sobre vulnerabilidades y alertas**.
- Otros CSIRT de referencia: **INCIBE-CERT** (ciudadanos y **sector privado**; a él notifican los **proveedores privados** del sector público) y **ESPDEF-CERT** (Defensa, **Mando Conjunto del Ciberespacio**).
- **Operadores de servicios esenciales y proveedores de servicios digitales:** se rigen además por el **RDL 12/2018** (que transpuso la Directiva **NIS**) y el **RD 43/2021**.
- **Informe del Estado de la Seguridad (art. 32):** lo elabora la **Comisión Sectorial de Administración Electrónica** con la herramienta **INES** del CCN.

## Otros elementos del ENS

- **Guías CCN-STIC:** las series **800** desarrollan el ENS (p. ej., la **CCN-STIC 803** de valoración de sistemas, la **804** de guía de implantación, la **808** de verificación del cumplimiento).
- **Instrucciones Técnicas de Seguridad (ITS)** (DA 2ª): las aprueba el Ministerio competente a propuesta de la Comisión Sectorial y del CCN; por ejemplo, la de **Informe del Estado de la Seguridad**, **Conformidad con el ENS**, **Auditoría**, **Notificación de incidentes** o **Requisitos de seguridad en entornos externalizados**.
- **Formación (DA 1ª):** las Administraciones forman a su personal en seguridad.
- **Herramientas del CCN:** **PILAR** (análisis de riesgos), **INES** (estado de seguridad), **LUCÍA** (gestión de incidentes), **CLARA** y **microCLAUDIA** (cumplimiento y protección frente a código dañino), entre otras.

## ENS frente a ENI y RGPD

| | **ENS** | **ENI** | **RGPD** |
| --- | --- | --- | --- |
| Norma | RD 311/2022 | RD 4/2010 | Reglamento (UE) 2016/679 |
| Base | Art. 156.2 Ley 40/2015 | Art. 156.1 Ley 40/2015 | Art. 18.4 CE |
| Objetivo | **Seguridad** de la información y los servicios | **Interoperabilidad** entre sistemas | **Protección de los datos personales** |
| Desarrollo técnico | Guías **CCN-STIC** e **ITS** | **Normas Técnicas de Interoperabilidad** | Guías de la **AEPD** y del CEPD |
| Pieza clave | Categoría del sistema y Declaración de Aplicabilidad | Estándares abiertos, metadatos, Red SARA | Responsabilidad proactiva, EIPD, DPD |

## Resumen de cifras

| Qué | Dato |
| --- | --- |
| Norma | RD 311/2022, de 3 de mayo (deroga el RD 3/2010) |
| Principios básicos | 7 |
| Requisitos mínimos | 15 |
| Dimensiones | 5 (C, I, T, A, D) |
| Niveles por dimensión | 3 (BAJO, MEDIO, ALTO) |
| Categorías de sistema | 3 (BÁSICA, MEDIA, ALTA) |
| Responsables | 4 (información, servicio, seguridad, sistema) |
| Medidas del anexo II | 73 (org 4, op 33, mp 36) |
| Auditoría ordinaria | Al menos cada 2 años (+3 meses por fuerza mayor) |
| Reevaluación de la categoría | Anual |
| Conformidad BÁSICA | Autoevaluación (declaración) |
| Conformidad MEDIA y ALTA | Auditoría (certificación) |
| Adecuación de sistemas existentes | 24 meses |
