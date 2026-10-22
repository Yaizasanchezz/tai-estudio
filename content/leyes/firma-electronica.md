---
title: Firma electrónica y servicios de confianza · Reglamento eIDAS y Ley 6/2020
description: Tipos de firma y sus efectos, sellos, sellos de tiempo, certificados, prestadores cualificados, eIDAS 2 y la Cartera Europea de Identidad Digital, la Ley 6/2020 y cómo funciona técnicamente la firma.
order: 13
---

!!! tip "Jurídico y técnico a la vez"
    En el examen te pueden preguntar qué **efectos** tiene una firma cualificada (jurídico) o qué **clave** se usa para firmar y cuál para verificar (técnico). Aquí tienes las dos caras.

## Las normas

| Norma | Qué es |
| --- | --- |
| **Reglamento (UE) n.º 910/2014**, de **23 de julio de 2014** (**eIDAS**) | Identificación electrónica y servicios de confianza para las transacciones electrónicas en el mercado interior. **Directamente aplicable** (la mayor parte desde el **1 de julio de 2016**). Deroga la **Directiva 1999/93/CE** de firma electrónica |
| **Reglamento (UE) 2024/1183**, de 11 de abril de 2024 (**eIDAS 2**) | Modifica el anterior y crea el **Marco Europeo de Identidad Digital** y la **Cartera Europea de Identidad Digital** |
| **Ley 6/2020, de 11 de noviembre**, reguladora de determinados aspectos de los **servicios electrónicos de confianza** | **Complementa** el eIDAS en España. **Deroga la Ley 59/2003 de firma electrónica**. En vigor desde el **13 de noviembre de 2020** |
| **Leyes 39/2015 y 40/2015** y **RD 203/2021** | Sistemas de identificación y firma **de los interesados y de las Administraciones** (ver [Administración electrónica]({{base}}leyes/administracion-electronica/)) |

## 1. Reglamento eIDAS

### Las dos partes del reglamento

1. **Identificación electrónica (eID):** **reconocimiento mutuo** entre Estados de los **sistemas de identificación electrónica notificados** a la Comisión. España ha notificado el **DNIe** y **Cl@ve**. Los sistemas tienen **niveles de seguridad**: **bajo**, **sustancial** y **alto**; el reconocimiento es obligatorio para los de nivel **sustancial o alto** cuando un servicio público en línea exige ese nivel.
2. **Servicios de confianza:** firmas, sellos, sellos de tiempo, entrega electrónica certificada y autenticación de sitios web, con sus **prestadores**.

### Conceptos básicos (art. 3)

| Concepto | Definición |
| --- | --- |
| **Firmante** | **Persona física** que crea una firma electrónica |
| **Firma electrónica** | **Datos en formato electrónico** anejos a otros datos electrónicos o **asociados de manera lógica** con ellos, que **utiliza el firmante para firmar** |
| **Creador de un sello** | **Persona jurídica** que crea un sello electrónico |
| **Sello electrónico** | Datos en formato electrónico anejos o asociados a otros para **garantizar su origen y su integridad** (la «firma» de una persona jurídica u órgano) |
| **Sello cualificado de tiempo electrónico** | Vincula datos con un **instante concreto**, aportando prueba de que existían en ese momento |
| **Certificado** | Declaración electrónica que **vincula los datos de validación** de una firma o sello con una persona y **confirma** su nombre o seudónimo |
| **Datos de creación de firma** | Datos únicos (la **clave privada**) que usa el firmante para crear la firma |
| **Dispositivo cualificado de creación de firma (QSCD)** | Hardware o software que cumple los requisitos del anexo II (tarjeta criptográfica, chip del DNIe, **HSM** de firma en la nube) |
| **Servicio de confianza** | Servicio electrónico, normalmente **remunerado**, de creación, verificación y validación de **firmas, sellos, sellos de tiempo, entregas certificadas** y sus certificados; de **autenticación de sitios web**; y de **preservación** de firmas y sellos |
| **Prestador cualificado** | Prestador al que el **organismo de supervisión** ha concedido la **cualificación** y figura en la **lista de confianza** |

### Los tres tipos de firma

| Tipo | Requisitos | Efectos |
| --- | --- | --- |
| **Firma electrónica (simple)** | Cualquier dato electrónico que se use para firmar (un nombre al final de un correo, un clic en «acepto», una firma escaneada) | **No se le pueden negar efectos jurídicos ni admisibilidad como prueba** solo por ser electrónica o no ser cualificada (art. 25.1) |
| **Firma electrónica avanzada** (art. 26) | a) Vinculada al firmante **de manera única**; b) permite **identificarlo**; c) creada con datos que el firmante puede usar **con un alto nivel de confianza bajo su control exclusivo**; d) vinculada a los datos firmados de modo que **cualquier modificación ulterior sea detectable** | Los anteriores; su valor probatorio se aprecia en cada caso |
| **Firma electrónica cualificada** | Firma **avanzada** creada mediante un **dispositivo cualificado de creación de firma** y basada en un **certificado cualificado** de firma | **Efecto jurídico equivalente al de una firma manuscrita** (art. 25.2) y **reconocida en todos los Estados miembros** (art. 25.3) |

!!! warning "La pregunta trampa"
    **Solo la firma cualificada** equivale **automáticamente** a la manuscrita. La avanzada **no**: tiene efectos y puede ser prueba, pero sin esa equivalencia legal. Y la simple **tampoco puede ser rechazada** solo por ser electrónica.

### Otros servicios de confianza

- **Sello electrónico** (arts. 35 a 40): para **personas jurídicas**. El **sello cualificado** goza de **presunción de integridad** de los datos y de **corrección del origen**. Las Administraciones lo usan en la **actuación automatizada** (art. 42 Ley 40/2015).
- **Sello de tiempo electrónico** (arts. 41 y 42): el **cualificado** tiene **presunción de exactitud de la fecha y hora** que indica y de **integridad** de los datos a los que se vinculan. Debe estar vinculado a una **hora UTC** exacta.
- **Servicio de entrega electrónica certificada** (arts. 43 y 44): prueba del **envío y la recepción** (como un **burofax electrónico**). El cualificado presume la integridad, el envío por el remitente identificado, la recepción por el destinatario identificado y la exactitud de la fecha y hora.
- **Autenticación de sitios web** (art. 45): **certificados cualificados de autenticación de sitio web (QWAC)**, que permiten saber que un sitio pertenece a quien dice. Lo usan las **sedes electrónicas**.
- **Validación y preservación** de firmas y sellos cualificados (arts. 32 a 34 y 39 y 40): verificar su validez y **prolongar su fiabilidad** a largo plazo.

### Prestadores y supervisión

- Cada Estado designa un **organismo de supervisión**; en España, el **Ministerio para la Transformación Digital y de la Función Pública** (a través de la Secretaría de Estado de Digitalización e Inteligencia Artificial).
- Los **prestadores cualificados** se someten a una **auditoría** de un **organismo de evaluación de la conformidad** al menos **cada 24 meses**, y figuran en la **lista de confianza** (*Trusted List*, **TSL**) que publica cada Estado. Pueden usar la **etiqueta de confianza «UE»**.
- Los **no cualificados** no necesitan autorización previa.

### eIDAS 2 · Reglamento (UE) 2024/1183

- Crea el **Marco Europeo de Identidad Digital**.
- **Cartera Europea de Identidad Digital** (*EUDI Wallet*): una **aplicación** que cada Estado debe ofrecer a sus ciudadanos, **gratuita y voluntaria**, para **identificarse**, **guardar y compartir** atributos verificados (permiso de conducir, títulos, recetas…) de forma **selectiva** y **firmar con firma cualificada**.
- **Nuevos servicios de confianza:** **declaración electrónica de atributos** (cualificada o expedida por un organismo público), **archivo electrónico**, **libros mayores electrónicos** (registros distribuidos tipo *blockchain*) y **gestión remota de dispositivos cualificados** de creación de firma.

## 2. Ley 6/2020, de servicios electrónicos de confianza

- **Objeto (art. 1):** regular **determinados aspectos** de los servicios electrónicos de confianza como **complemento del eIDAS**.
- **Ámbito (art. 2):** prestadores **públicos y privados establecidos en España** (y los de otros Estados con establecimiento permanente aquí, si no los supervisa otra autoridad de la UE).
- **Documentos electrónicos (art. 3):** los **públicos, administrativos y privados** tienen el **valor y eficacia** que corresponda a su naturaleza. En un juicio, si se usó un **servicio cualificado**, se **presume** que el documento reúne la característica cuestionada (integridad, fecha, autoría…) y **la carga de la prueba** pasa a quien lo impugne (art. 326.4 LEC, con multa de 300 a 1.200 € si la impugnación es temeraria).

### Certificados (arts. 4 a 7)

- **Extinción:** por **caducidad** al expirar su vigencia o por **revocación**.
- **Vigencia máxima de los certificados cualificados: 5 años.**
- **Causas de revocación (art. 5):** solicitud del titular; **compromiso de la clave privada** (o del prestador); **resolución judicial o administrativa**; **fallecimiento** del firmante o modificación judicial de su capacidad; extinción de la persona jurídica; pérdida del control del **dominio** (en los de sitio web); **fin de la representación**; **cese del prestador** (salvo transferencia); **falsedad** de los datos; mecanismos criptográficos **inseguros**; otras previstas en la **declaración de prácticas de certificación**.
- **Suspensión:** en algunos supuestos (solicitud, orden judicial o administrativa, criptografía insegura, o dudas sobre compromiso o falsedad), si lo prevén las prácticas de certificación. Si al terminar la suspensión no se levanta, **el certificado se extingue**.
- **Identidad del titular (art. 6):** personas físicas por **nombre, apellidos y DNI/NIE/NIF**, o mediante un **seudónimo** que conste como tal (el prestador debe conocer la identidad real). Personas jurídicas por **razón social y NIF**.
- **Comprobación de identidad (art. 7):** exige **personación** con DNI, pasaporte u otro medio admitido, **o** identificación **a distancia** por **videoidentificación** con seguridad equivalente (regulada por **Orden ETD/465/2021**). Si hay **relación previa** con el prestador en la que ya se identificó presencialmente, puede no exigirse de nuevo (si no han pasado más de **5 años**).

### Obligaciones de los prestadores (arts. 9 a 13)

- Publicar **información veraz**.
- **No almacenar ni copiar los datos de creación de firma** (la clave privada) del titular, **salvo** que los gestione **en su nombre** (firma en la nube), con sistemas fiables bajo el **control exclusivo** del titular.
- Disponer de un **servicio público de consulta del estado de validez o revocación** de los certificados (**OCSP** o **listas de revocación, CRL**).
- **Prestadores cualificados**, además:
    - **Conservar** la información de los servicios prestados durante **15 años** desde la extinción del certificado o la finalización del servicio.
    - **Seguro de responsabilidad civil** de al menos **1.500.000 €** (más **500.000 €** por cada servicio cualificado adicional), salvo los del **sector público**.
    - Comunicar el **cese** de actividad a clientes y al supervisor con **2 meses** de antelación.
    - Enviar el **informe de evaluación de la conformidad** al Ministerio y un **informe anual de actividad** antes del **1 de febrero**.
- **No cualificados (art. 12):** **sin verificación previa**, pero deben **comunicar** su actividad al Ministerio en **3 meses** desde que la inician.
- **Seguridad (art. 13):** notificar al Ministerio las **violaciones de seguridad** (además de a la AEPD si afectan a datos personales) y ampliar la información en **1 mes**.

### Supervisión y sanciones (arts. 14 a 20)

- **Órgano de supervisión:** el **Ministerio** competente en transformación digital, que inspecciona y mantiene la **lista de confianza**. El procedimiento de **cualificación** se resuelve en **6 meses** (silencio **desestimatorio**).
- **Infracciones:** **muy graves** (reincidencia en graves en 2 años; expedir certificados cualificados sin comprobar la identidad cuando afecta a la mayoría de los emitidos…), **graves** (obstruir la inspección, presentarse como cualificado sin serlo, copiar claves privadas, no conservar la información, no notificar incidentes, no revocar certificados, carecer del seguro…) y **leves** (información no veraz, no comunicar el inicio de actividad…).

| Infracción | Multa |
| --- | --- |
| **Muy grave** | **150.001 a 300.000 €** |
| **Grave** | **50.001 a 150.000 €** |
| **Leve** | **Hasta 50.000 €** |

Puede sustituirse por un **apercibimiento** (art. 19 bis). Las muy graves las impone el **Ministro** y las graves y leves la **Secretaría de Estado de Digitalización e IA**. El procedimiento dura como máximo **9 meses**.

### Disposiciones adicionales clave

- **DA 2ª:** **todos los sistemas de identificación, firma y sello** de las **Leyes 39/2015 y 40/2015** tienen **plenos efectos jurídicos** (por ejemplo, **Cl@ve** o el **CSV**).
- **DA 3ª · DNI electrónico:** permite **acreditar electrónicamente la identidad** y **firmar** documentos. **Todas las personas** y entidades deben **reconocer su eficacia**. El **Ministerio del Interior** (Dirección General de la Policía) cumple las obligaciones de un prestador cualificado.

## 3. ¿Cómo funciona una firma electrónica por dentro?

La firma basada en certificados usa **criptografía asimétrica** (de clave pública) y **funciones resumen** (*hash*):

```text
FIRMAR (emisor)
  documento ──► hash (SHA-256) ──► resumen ──► cifrar con CLAVE PRIVADA del firmante ──► FIRMA
  Se envía: documento + firma + certificado (con la CLAVE PÚBLICA)

VERIFICAR (receptor)
  firma ──► descifrar con CLAVE PÚBLICA del certificado ──► resumen A
  documento ──► hash ──► resumen B
  ¿A = B? ─► Sí: integridad y autoría correctas · No: el documento se ha alterado
  + comprobar que el certificado es válido (no caducado ni revocado: OCSP/CRL) y emitido por una CA de confianza
```

| Elemento | Papel |
| --- | --- |
| **Clave privada** | Solo la tiene el firmante (en el DNIe, la tarjeta o un HSM). Se usa para **firmar** |
| **Clave pública** | Va en el **certificado** y la conoce todo el mundo. Se usa para **verificar** |
| **Hash** | Resumen de longitud fija; un cambio mínimo en el documento cambia el hash (**integridad**) |
| **Certificado X.509** | Vincula la clave pública con una identidad; lo firma la **Autoridad de Certificación** |
| **PKI** | Infraestructura de clave pública: **Autoridad de Certificación (CA)**, **Autoridad de Registro (RA)** que comprueba la identidad, y servicios de **validación** (OCSP, CRL) |

!!! example "No lo confundas con el cifrado"
    Para **firmar** se usa la clave **privada del emisor** (y se verifica con su pública). Para **cifrar** un mensaje confidencial se usa la clave **pública del destinatario** (y solo él lo descifra con su privada).

**Formatos de firma (NTI de política de firma y estándares ETSI):**

| Formato | Para qué |
| --- | --- |
| **XAdES** | Firma en **XML** (muy usada en la Administración y en facturas electrónicas) |
| **CAdES** | Firma **CMS/PKCS#7** para cualquier fichero binario |
| **PAdES** | Firma dentro de un **PDF** (visible al abrirlo) |
| **ASiC** | **Contenedor** que agrupa ficheros y sus firmas |

Niveles: **B** (básica), **T** (con **sello de tiempo**), **LT** (con la información de **validación a largo plazo**) y **LTA** (con sellos de archivo para **preservarla** indefinidamente). Modalidades: **adjunta** (*enveloped/enveloping*, la firma va con el documento) y **separada** (*detached*).

**Prestadores y herramientas habituales en España:** **FNMT-RCM** (certificados de persona física, de representante, de empleado público y de sede, a través de **CERES**), la **Dirección General de la Policía** (DNIe; el **RD 255/2025** regula el DNI en su versión física y **digital**, que puede llevarse en el móvil con la app **MiDNI**), la **ACCV** (Comunitat Valenciana), **Camerfirma**, **Firmaprofesional**… y, en la Administración, **AutoFirma**, **@firma**, **Port@firmas**, **TS@** y **Cl@ve Firma**.

## Resumen de cifras

| Qué | Dato |
| --- | --- |
| Reglamento eIDAS | (UE) 910/2014, de 23/07/2014; aplicable desde el 1/07/2016 |
| eIDAS 2 | (UE) 2024/1183 |
| Ley española | Ley 6/2020, de 11 de noviembre (deroga la Ley 59/2003) |
| Niveles de seguridad de la eID | Bajo, sustancial y alto |
| Firma equivalente a la manuscrita | Solo la cualificada |
| Vigencia máxima de un certificado cualificado | 5 años |
| Conservación de la información por el prestador cualificado | 15 años |
| Seguro de responsabilidad civil | 1.500.000 € (+500.000 € por servicio adicional) |
| Preaviso de cese | 2 meses |
| Comunicación de un prestador no cualificado | 3 meses |
| Resolución de la cualificación | 6 meses (silencio desestimatorio) |
| Multas | Muy graves 150.001–300.000 €; graves 50.001–150.000 €; leves hasta 50.000 € |
