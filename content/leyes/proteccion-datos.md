---
title: Protección de datos · RGPD (Reglamento UE 2016/679) y LOPDGDD (LO 3/2018)
description: Conceptos, principios, bases de legitimación, derechos, obligaciones del responsable y del encargado, delegado de protección de datos, brechas, transferencias, AEPD, sanciones y derechos digitales.
order: 10
---

!!! tip "Es doble materia"
    La protección de datos aparece en el **bloque jurídico** (derecho fundamental del art. 18.4 CE) y en el **técnico** (seguridad, seudonimización, cifrado, EIPD, privacidad desde el diseño). Como TAI vas a tratar datos personales todos los días, así que esto es también tu día a día.

## Las dos normas y cómo encajan

| | **RGPD** | **LOPDGDD** |
| --- | --- | --- |
| Norma | **Reglamento (UE) 2016/679**, del Parlamento Europeo y del Consejo, de **27 de abril de 2016** | **Ley Orgánica 3/2018, de 5 de diciembre**, de Protección de Datos Personales y garantía de los derechos digitales |
| Vigencia | En vigor desde el **25 de mayo de 2016**; **aplicable desde el 25 de mayo de 2018** | En vigor desde el **7 de diciembre de 2018** |
| Naturaleza | **Directamente aplicable** en todos los Estados miembros, sin transposición | **Adapta y completa** el RGPD en España y añade los **derechos digitales** (Título X) |
| Estructura | **99 artículos** en **11 capítulos** y **173 considerandos** | **97 artículos** en **10 títulos** |
| Sustituye a | La Directiva 95/46/CE | La LO 15/1999 (LOPD) |

**Fundamento constitucional:** **art. 18.4 CE** («la ley limitará el uso de la informática para garantizar el honor y la intimidad…»). El TC (**STC 292/2000**) configuró la protección de datos como un **derecho fundamental autónomo**, distinto de la intimidad. También el **art. 8 de la Carta de Derechos Fundamentales de la UE**.

## Ámbito de aplicación

- **Material (RGPD art. 2):** tratamiento **total o parcialmente automatizado** de datos personales y el **no automatizado** de datos contenidos o destinados a un **fichero**.
- **Excluidos:** actividades fuera del Derecho de la UE; tratamientos de una persona física en actividades **exclusivamente personales o domésticas**; los de las autoridades para fines **penales** (los rige la **Directiva 2016/680**, en España la **LO 7/2021**); los datos de **personas fallecidas** (LOPDGDD art. 2.2.b) y las **materias clasificadas**.
- **Territorial (RGPD art. 3):** responsables o encargados **establecidos en la UE** (aunque traten fuera) y los de **fuera de la UE** que **ofrezcan bienes o servicios** a personas en la UE o **controlen su comportamiento** en la UE.

**Datos de personas fallecidas (LOPDGDD art. 3):** familiares, personas vinculadas de hecho y herederos pueden pedir acceso, rectificación o supresión, **salvo que el fallecido lo prohibiera** (los herederos pueden acceder siempre a los datos **patrimoniales**).

## Definiciones clave (RGPD art. 4)

| Concepto | Definición |
| --- | --- |
| **Dato personal** | Toda información sobre una persona física **identificada o identificable** (nombre, DNI, ubicación, identificador en línea, IP, rasgos físicos, genéticos, económicos…) |
| **Tratamiento** | **Cualquier operación** sobre datos: recogida, registro, organización, conservación, consulta, uso, comunicación, cotejo, limitación, **supresión o destrucción** |
| **Limitación del tratamiento** | **Marcado** de los datos conservados para limitar su tratamiento futuro |
| **Elaboración de perfiles** | Tratamiento automatizado para **evaluar aspectos personales** (rendimiento, situación económica, salud, preferencias, ubicación…) |
| **Seudonimización** | Tratar los datos de forma que **no puedan atribuirse a un interesado sin información adicional**, que se guarda **por separado** con medidas técnicas. **Sigue siendo dato personal** |
| **Anonimización** | (No la define el art. 4, pero es clave.) Los datos ya **no permiten identificar** a nadie de forma irreversible: **dejan de ser datos personales** y el RGPD no se aplica |
| **Fichero** | Conjunto estructurado de datos accesibles con arreglo a criterios determinados |
| **Responsable del tratamiento** | Quien **determina los fines y medios** del tratamiento |
| **Encargado del tratamiento** | Quien trata datos **por cuenta del responsable** |
| **Destinatario** | A quien se comunican los datos |
| **Tercero** | Persona distinta del interesado, responsable, encargado y personas autorizadas |
| **Consentimiento** | Manifestación de voluntad **libre, específica, informada e inequívoca**, mediante una **declaración o una clara acción afirmativa** |
| **Violación de la seguridad (brecha)** | Toda violación que ocasione la **destrucción, pérdida o alteración accidental o ilícita**, o la **comunicación o acceso no autorizados**, de datos personales |
| **Datos genéticos / biométricos / relativos a la salud** | Categorías especiales con definición propia |
| **Establecimiento principal** | Lugar de la **administración central** en la UE (determina la **autoridad de control principal**) |

!!! example "Responsable y encargado en tu día a día"
    El Ministerio que gestiona las becas es el **responsable**: decide para qué y cómo se tratan los datos. La empresa contratada para mantener el servidor donde están es la **encargada**: solo los trata siguiendo sus instrucciones, en virtud de un **contrato de encargo** (art. 28 RGPD).

## Principios (RGPD art. 5)

| Principio | Qué exige |
| --- | --- |
| **Licitud, lealtad y transparencia** | Tratar los datos de forma lícita, leal y transparente con el interesado |
| **Limitación de la finalidad** | Fines **determinados, explícitos y legítimos**; no tratarlos después de forma incompatible (el archivo de interés público, la investigación y la estadística **no se consideran incompatibles**) |
| **Minimización de datos** | Datos **adecuados, pertinentes y limitados a lo necesario** |
| **Exactitud** | Datos **exactos y actualizados**; suprimir o rectificar sin dilación los inexactos |
| **Limitación del plazo de conservación** | Mantenerlos de forma que se identifique al interesado **solo el tiempo necesario** |
| **Integridad y confidencialidad** | **Seguridad adecuada** frente al tratamiento no autorizado, la pérdida o el daño, con medidas técnicas y organizativas |
| **Responsabilidad proactiva** (*accountability*) | El responsable **cumple y debe poder demostrar** que cumple |

**LOPDGDD:** la **exactitud** no es imputable al responsable si los datos los aportó el propio interesado o vienen de un registro público (art. 4). **Deber de confidencialidad** (art. 5) de todos los que intervienen en el tratamiento, que **se mantiene aunque termine la relación**.

## Licitud del tratamiento: las 6 bases (RGPD art. 6)

1. **Consentimiento** del interesado para uno o varios fines específicos.
2. Ejecución de un **contrato** o medidas precontractuales a petición del interesado.
3. Cumplimiento de una **obligación legal** del responsable.
4. Protección de **intereses vitales** del interesado o de otra persona.
5. Cumplimiento de una **misión de interés público** o ejercicio de **poderes públicos**.
6. **Interés legítimo** del responsable o de un tercero, si no prevalecen los derechos del interesado. **No se aplica a las autoridades públicas en el ejercicio de sus funciones.**

!!! warning "Para la Administración"
    Las Administraciones tratan datos casi siempre por **obligación legal** (letra c) o **misión de interés público / poderes públicos** (letra e), y la **LOPDGDD (art. 8)** exige que estas bases estén previstas en una **norma con rango de ley** (o de la UE). No pueden usar el **interés legítimo** para sus funciones públicas.

**Consentimiento (RGPD art. 7 y LOPDGDD arts. 6 y 7):**

- El responsable debe poder **demostrarlo**. Puede **retirarse en cualquier momento**, y retirarlo debe ser **tan fácil como darlo**.
- El **silencio, las casillas premarcadas o la inacción no son consentimiento** (considerando 32).
- Si es para varias finalidades, debe constar **para todas ellas**. No se puede condicionar un contrato a consentir tratamientos no relacionados con él.
- **Menores:** el RGPD fija **16 años** para los servicios de la sociedad de la información y permite bajarlo hasta **13**. **En España: 14 años** (LOPDGDD art. 7). Por debajo, consentimiento del titular de la **patria potestad o tutela**.

## Categorías especiales y datos penales

**Categorías especiales (RGPD art. 9):** datos que revelen **origen étnico o racial**, **opiniones políticas**, **convicciones religiosas o filosóficas**, **afiliación sindical**, **datos genéticos**, **datos biométricos** dirigidos a identificar unívocamente a una persona, datos de **salud** y datos sobre **vida sexual u orientación sexual**.

- **Regla:** tratamiento **prohibido**, salvo excepciones (consentimiento **explícito**, obligaciones en materia laboral y de Seguridad Social, intereses vitales, datos hechos **manifiestamente públicos** por el interesado, reclamaciones judiciales, interés público esencial, medicina preventiva o laboral, salud pública, archivo e investigación…).
- **LOPDGDD art. 9:** el **solo consentimiento no basta** para tratar datos cuya finalidad principal sea identificar la **ideología, afiliación sindical, religión, orientación sexual, creencias u origen racial o étnico** (para evitar discriminación).

**Datos penales (RGPD art. 10 y LOPDGDD art. 10):** solo bajo control de una autoridad pública o si lo autoriza el Derecho de la UE o una norma con rango de ley.

## Derechos de los interesados (RGPD arts. 12 a 22 y LOPDGDD arts. 11 a 18)

**Reglas comunes (RGPD art. 12 y LOPDGDD art. 12):**

- Información **concisa, transparente, inteligible y de fácil acceso**, con lenguaje claro.
- **Plazo de respuesta: 1 mes** desde la solicitud, prorrogable **2 meses más** si es complejo o hay muchas solicitudes (informando al interesado en el primer mes).
- **Gratuito**, salvo solicitudes **manifiestamente infundadas o excesivas** (canon razonable o negativa). En España, pedir el **acceso más de una vez en 6 meses** puede considerarse **repetitivo** sin causa legítima (LOPDGDD art. 13.3).
- Pueden ejercerse **directamente o por representante**. Los titulares de la patria potestad ejercen los de los **menores de 14 años**.
- La carga de probar que se respondió recae en el **responsable**.

| Derecho | Contenido |
| --- | --- |
| **Información** (arts. 13 y 14) | Identidad del responsable, datos del **DPD**, fines y base jurídica, destinatarios, transferencias, **plazo de conservación**, derechos, derecho a reclamar ante la autoridad, existencia de decisiones automatizadas. Si los datos no se obtuvieron del interesado, en **1 mes** como máximo. **España: información por capas** (LOPDGDD art. 11): una **información básica** (responsable, finalidad, derechos) y un enlace a la restante |
| **Acceso** (art. 15) | Saber si se tratan sus datos y obtener **copia** y la información del tratamiento. Se entiende otorgado si se da un **acceso remoto, directo y seguro** |
| **Rectificación** (art. 16) | Corregir datos **inexactos** y completar los incompletos |
| **Supresión o «derecho al olvido»** (art. 17) | Cuando los datos ya no son necesarios, se retira el consentimiento, hay oposición, tratamiento ilícito, obligación legal o datos de menores en servicios de la sociedad de la información. Excepciones: libertad de expresión, obligación legal, interés público, salud pública, archivo, reclamaciones |
| **Limitación** (art. 18) | «Congelar» el tratamiento mientras se comprueba la exactitud o la oposición, si el tratamiento es ilícito y el interesado prefiere no suprimir, o si los necesita para reclamaciones. Debe **constar claramente** en los sistemas (LOPDGDD) |
| **Notificación** (art. 19) | El responsable comunica a los destinatarios las rectificaciones, supresiones o limitaciones |
| **Portabilidad** (art. 20) | Recibir sus datos en un **formato estructurado, de uso común y lectura mecánica** y transmitirlos a otro responsable. Solo si el tratamiento se basa en **consentimiento o contrato** y es **automatizado**. **No se aplica** a tratamientos de interés público o poderes públicos |
| **Oposición** (art. 21) | Oponerse por su situación particular a tratamientos basados en interés público o interés legítimo; y **siempre** a la **mercadotecnia directa** |
| **No ser objeto de decisiones automatizadas** (art. 22) | Derecho a no ser objeto de una decisión basada **únicamente en el tratamiento automatizado**, incluida la elaboración de perfiles, que produzca efectos jurídicos o le afecte significativamente, salvo contrato, ley o consentimiento explícito; con derecho a **intervención humana**, a expresar su punto de vista y a impugnar |

!!! tip "Para recordarlos"
    Los clásicos eran los derechos **ARCO** (Acceso, Rectificación, Cancelación, Oposición). Con el RGPD se habla de **ARSULIPO** u **ARCO-POL**: Acceso, Rectificación, Supresión, Limitación, Portabilidad, Oposición y no ser objeto de decisiones automatizadas.

**Bloqueo (LOPDGDD art. 32):** al **rectificar o suprimir**, el responsable debe **bloquear** los datos: identificarlos y reservarlos impidiendo su tratamiento, salvo para ponerlos a disposición de **jueces, Ministerio Fiscal o Administraciones** (incluidas las autoridades de protección de datos) durante el **plazo de prescripción** de las responsabilidades. Después, **destruirlos**.

## Responsable y encargado (RGPD arts. 24 a 31)

- **Responsabilidad del responsable (art. 24):** aplicar medidas técnicas y organizativas apropiadas **según el riesgo** y poder demostrarlo.
- **Protección de datos desde el diseño y por defecto (art. 25):**
    - **Desde el diseño** (*privacy by design*): integrar la protección **desde la concepción** del sistema (seudonimización, minimización…).
    - **Por defecto** (*privacy by default*): por defecto solo se tratan los datos **necesarios** para cada fin (cantidad, extensión, plazo y accesibilidad).
- **Corresponsables (art. 26):** dos o más responsables que determinan conjuntamente fines y medios; deben fijar sus responsabilidades en un **acuerdo**.
- **Representante (art. 27):** lo designan los responsables o encargados **no establecidos en la UE**.
- **Encargado (art. 28):** solo pueden elegirse encargados que ofrezcan **garantías suficientes**. La relación se rige por un **contrato u otro acto jurídico** que fija objeto, duración, naturaleza, finalidad, tipo de datos y obligaciones (tratar solo **siguiendo instrucciones documentadas**, confidencialidad, seguridad, **subencargados solo con autorización**, devolver o suprimir los datos al terminar…).
- **Registro de las actividades de tratamiento (art. 30):** sustituye a la antigua **inscripción de ficheros** en la AEPD. Recoge fines, categorías de interesados y datos, destinatarios, transferencias, plazos de supresión y medidas de seguridad. **Excepción:** organizaciones de **menos de 250 empleados**, salvo que el tratamiento suponga riesgo, no sea ocasional o incluya categorías especiales o datos penales.
- **Inventario público (LOPDGDD art. 31.2):** las Administraciones y demás sujetos del art. 77.1 **publican por medios electrónicos** un **inventario de sus actividades de tratamiento** con su base legal.

## Seguridad y brechas (RGPD arts. 32 a 34)

- **Seguridad del tratamiento (art. 32):** medidas apropiadas al riesgo, como la **seudonimización y el cifrado**, la capacidad de garantizar la **confidencialidad, integridad, disponibilidad y resiliencia** permanentes, la capacidad de **restaurar** la disponibilidad tras un incidente y un proceso de **verificación y evaluación** periódica. En el sector público, las medidas se corresponden con las del **Esquema Nacional de Seguridad** (LOPDGDD DA 1ª).
- **Notificación de la brecha a la autoridad (art. 33):** **sin dilación indebida** y, si es posible, **en las 72 horas** siguientes a tener constancia, **salvo que sea improbable** que constituya un riesgo para los derechos de las personas. Si se hace más tarde, hay que justificar el retraso. El **encargado** debe notificar al responsable **sin dilación**. Hay que **documentar** todas las brechas.
- **Comunicación al interesado (art. 34):** **sin dilación** cuando sea probable que la brecha entrañe un **alto riesgo** para sus derechos. No hace falta si los datos estaban **cifrados** (ininteligibles), si se han tomado medidas que eliminan el alto riesgo o si supone un esfuerzo desproporcionado (en ese caso, comunicación pública).

## Evaluación de impacto (EIPD) y consulta previa (RGPD arts. 35 y 36)

- **EIPD:** obligatoria cuando sea probable que un tratamiento entrañe un **alto riesgo**, en particular en:
    - **Evaluación sistemática y exhaustiva** de aspectos personales basada en tratamiento automatizado (perfiles) con efectos jurídicos.
    - Tratamiento **a gran escala** de **categorías especiales** o datos penales.
    - **Observación sistemática a gran escala** de una zona de acceso público (videovigilancia masiva).
- La AEPD publica listas de tratamientos que requieren EIPD. El responsable debe recabar el asesoramiento del **DPD**.
- **Consulta previa (art. 36):** si la EIPD muestra un alto riesgo que el responsable **no puede mitigar**, debe consultar a la autoridad de control antes de tratar.

## Delegado de protección de datos (DPD o DPO)

**Obligatorio (RGPD art. 37)** cuando:

1. El tratamiento lo lleva a cabo una **autoridad u organismo público** (excepto tribunales en su función judicial). **Todas las Administraciones deben tener DPD.**
2. Las actividades principales consisten en **observación habitual y sistemática a gran escala**.
3. Las actividades principales consisten en tratar **a gran escala categorías especiales** o datos penales.

**La LOPDGDD (art. 34) añade** una lista de entidades obligadas: colegios profesionales, **centros docentes y Universidades**, operadores de telecomunicaciones, prestadores de servicios de la sociedad de la información que hagan perfiles a gran escala, **entidades de crédito**, aseguradoras, empresas de inversión, distribuidoras de energía, ficheros de solvencia, publicidad con perfiles, **centros sanitarios** con historias clínicas (no los profesionales individuales), informes comerciales, **juego online**, **seguridad privada** y federaciones deportivas que traten datos de menores.

- **Designación:** puede ser **interno o externo**, persona física o jurídica, por sus **conocimientos especializados** del Derecho y la práctica en protección de datos (puede acreditarse con **certificación**). Un **grupo empresarial** o varias autoridades pueden designar **uno solo**.
- La designación, nombramiento y cese se comunican a la AEPD en **10 días** (LOPDGDD art. 34.3).
- **Posición (RGPD art. 38 y LOPDGDD art. 36):** participa en todas las cuestiones de protección de datos, tiene **recursos**, **no recibe instrucciones**, **no puede ser destituido ni sancionado** por desempeñar sus funciones (salvo **dolo o negligencia grave**), rinde cuentas al **más alto nivel jerárquico** y está sujeto a **secreto**. Puede tener otras tareas si no hay **conflicto de intereses**.
- **Funciones (art. 39):** **informar y asesorar**, **supervisar** el cumplimiento, asesorar en la **EIPD**, **cooperar** con la autoridad de control y ser su **punto de contacto**.
- **Reclamaciones (LOPDGDD art. 37):** el interesado **puede** dirigirse primero al DPD, que debe responder en **2 meses**. Si reclama ante la AEPD, esta puede remitir la reclamación al DPD para que responda en **1 mes**.

## Códigos de conducta y certificación (RGPD arts. 40 a 43)

Los **códigos de conducta** (aprobados por la autoridad de control, con un organismo de supervisión) y los **mecanismos de certificación**, **sellos y marcas** sirven para **demostrar el cumplimiento**.

## Transferencias internacionales (RGPD arts. 44 a 50)

Transferir datos **fuera del Espacio Económico Europeo** solo se puede si:

1. Hay una **decisión de adecuación** de la **Comisión Europea** (art. 45): el país garantiza un nivel adecuado (p. ej., Suiza, Japón, Reino Unido, Corea del Sur o EE. UU. con el **Marco de Privacidad de Datos UE-EE. UU.** de 2023).
2. O hay **garantías adecuadas** (art. 46): **cláusulas contractuales tipo** aprobadas por la Comisión, **normas corporativas vinculantes** (BCR, art. 47), códigos de conducta, certificaciones…
3. O se da una **excepción** para situaciones específicas (art. 49): consentimiento explícito informado, ejecución de un contrato, interés público importante, reclamaciones, intereses vitales…

## Autoridades de control

- **Comité Europeo de Protección de Datos (CEPD / EDPB, art. 68):** **organismo de la Unión** con personalidad jurídica, formado por el jefe de una autoridad de cada Estado y el **Supervisor Europeo de Protección de Datos**. Garantiza la **aplicación coherente** del RGPD con directrices y dictámenes.
- **Ventanilla única (art. 56):** en tratamientos transfronterizos, la **autoridad de control principal** es la del **establecimiento principal** del responsable.

**Agencia Española de Protección de Datos (AEPD) (LOPDGDD arts. 44 a 56):**

| Aspecto | Dato |
| --- | --- |
| Naturaleza | **Autoridad administrativa independiente** de ámbito estatal (Ley 40/2015), con personalidad jurídica y **plena independencia** |
| Relación con el Gobierno | A través del **Ministerio de Justicia** |
| Representación | Es el **representante común** de las autoridades españolas en el **Comité Europeo** |
| Órganos | **Presidencia** y su **Adjunto**, asesorados por un **Consejo Consultivo** (un Diputado, un Senador, representantes del CGPJ, la AGE, las CC. AA. con autoridad propia, la FEMP, consumidores, empresarios, sindicatos, universidades, el CTBG…) |
| Nombramiento | Por el **Consejo de Ministros mediante Real Decreto**, tras convocatoria pública y **ratificación por la Comisión de Justicia del Congreso** (**3/5** en primera votación o **mayoría absoluta** en segunda) |
| Mandato | **5 años**, **renovable** una vez |
| Potestades | Investigación, **planes de auditoría**, **circulares** (normas obligatorias publicadas en el BOE), sancionadora |
| Autoridades autonómicas | **Cataluña** (APDCAT), **País Vasco** (AVPD) y **Andalucía** (Consejo de Transparencia y Protección de Datos), para los tratamientos de su sector público |

**Procedimiento ante la AEPD (LOPDGDD arts. 63 a 69):**

- Por **falta de atención a un derecho**: se resuelve en **6 meses** desde la admisión a trámite; si no, el interesado puede considerar **estimada** su reclamación.
- **Sancionador**: duración máxima de **12 meses** desde el acuerdo de inicio; después, **caducidad**.
- **Apercibimiento** con medidas correctivas: **6 meses**.
- Puede haber **actuaciones previas de investigación**.

## Régimen sancionador

**Multas del RGPD (art. 83):**

| Infracciones | Multa máxima |
| --- | --- |
| Obligaciones del responsable y encargado, certificación y organismos de supervisión (art. 83.4) | **10 millones de euros** o el **2 %** del volumen de negocio anual global (la **mayor**) |
| **Principios**, bases de licitud, consentimiento, categorías especiales, **derechos** de los interesados, **transferencias** e incumplir órdenes de la autoridad (art. 83.5 y 6) | **20 millones de euros** o el **4 %** del volumen de negocio anual global (la **mayor**) |

**Clasificación y prescripción en España (LOPDGDD arts. 72 a 78):**

| | Muy graves | Graves | Leves |
| --- | --- | --- | --- |
| Correspondencia | Art. 83.5 RGPD (vulneración sustancial) | Art. 83.4 RGPD (vulneración sustancial) | Restantes, de carácter **formal** |
| **Prescripción de la infracción** | **3 años** | **2 años** | **1 año** |

**Prescripción de las sanciones (art. 78), según el importe:** hasta **40.000 €**, **1 año**; de **40.001 a 300.000 €**, **2 años**; más de **300.000 €**, **3 años**.

Las sanciones de más de **1 millón de euros** a personas jurídicas impuestas por la AEPD se **publican en el BOE**.

!!! warning "Las Administraciones no pagan multas (art. 77 LOPDGDD)"
    A los **órganos constitucionales**, **tribunales**, **AGE, CC. AA. y Entidades Locales**, organismos públicos, autoridades independientes, **Banco de España**, corporaciones de Derecho público, fundaciones del sector público, **Universidades públicas**, consorcios y grupos parlamentarios y políticos **no se les imponen multas**: la autoridad dicta una resolución que **declara la infracción** y fija medidas correctoras, puede proponer **actuaciones disciplinarias** y, si hay responsabilidad de autoridades o directivos que ignoraron informes técnicos, una **amonestación** publicada en el boletín oficial. Las resoluciones se comunican al **Defensor del Pueblo** y se publican en la web de la AEPD.

## Tratamientos concretos de la LOPDGDD (Título IV)

- **Datos de contacto** de empresarios individuales y profesionales (art. 19): presunción de interés legítimo.
- **Sistemas de información crediticia** («ficheros de morosos», art. 20): deudas **ciertas, vencidas y exigibles** no reclamadas, informando al deudor de la posible inclusión, mientras persista el impago y con un máximo de **5 años** desde el vencimiento.
- **Videovigilancia (art. 22):** para la seguridad de personas, bienes e instalaciones; la vía pública solo en lo **imprescindible**; las imágenes se **suprimen en 1 mes** (salvo que acrediten un delito, en cuyo caso se entregan a la autoridad en **72 horas**); información con un **cartel** visible (responsable y derechos). El interior del propio domicilio queda **excluido**.
- **Sistemas de exclusión publicitaria** (art. 23, como la **Lista Robinson**).
- **Sistemas internos de denuncias** (art. 24, hoy regulados por la **Ley 2/2023** de protección del informante).
- **Función estadística pública**, **archivo** de interés público e **infracciones administrativas** (arts. 25 a 27).

**Identificación en las publicaciones (DA 7ª):**

| Caso | Cómo se identifica al interesado |
| --- | --- |
| **Publicación de un acto** administrativo | **Nombre y apellidos + 4 cifras numéricas aleatorias** del DNI, NIE o pasaporte (alternando las cifras si son varios) |
| **Notificación por anuncios** (art. 44 Ley 39/2015) | **Solo el número completo** del documento |
| Si no tiene documento | Solo **nombre y apellidos** |
| **Nunca** | Nombre y apellidos **junto con** el número completo |

## Título X · Garantía de los derechos digitales (arts. 79 a 97)

| Derecho | Contenido |
| --- | --- |
| **Neutralidad de Internet** (art. 80) | Los proveedores ofrecen una oferta transparente sin discriminación técnica o económica |
| **Acceso universal a Internet** (art. 81) | Asequible, de calidad y no discriminatorio; superar las **brechas de género, generacional y territorial** |
| **Seguridad digital** (art. 82) | Seguridad de las comunicaciones que se transmiten y reciben |
| **Educación digital** (art. 83) | El sistema educativo garantiza la competencia digital y el uso seguro de Internet |
| **Protección de los menores** en Internet (arts. 84 y 92) | Padres y centros velan por un uso equilibrado; el Ministerio Fiscal interviene si se difunden imágenes o datos de menores que vulneren sus derechos |
| **Rectificación en Internet** (art. 85) y **actualización** en medios digitales (art. 86) | Protocolos para rectificar y añadir avisos de actualización |
| **Intimidad en el uso de dispositivos digitales en el trabajo** (art. 87) | El empleador puede acceder solo para **controlar el cumplimiento** de obligaciones y la **integridad** de los dispositivos, con **criterios de uso** en cuya elaboración participan los representantes |
| **Desconexión digital** (art. 88) | **Trabajadores y empleados públicos** tienen derecho a no conectarse fuera de su horario, en descansos, permisos y vacaciones. El empleador elabora una **política interna** que evite la **fatiga informática**, también en el **teletrabajo** |
| **Videovigilancia y grabación de sonidos en el trabajo** (art. 89) | Para el control laboral, informando **previamente** y de forma expresa; nunca en vestuarios, aseos, comedores o zonas de descanso |
| **Geolocalización en el trabajo** (art. 90) | Informando previamente |
| **Derechos digitales en la negociación colectiva** (art. 91) | Los convenios pueden establecer garantías adicionales |
| **Derecho al olvido en buscadores** (art. 93) | Que los **motores de búsqueda** eliminen de los resultados por su **nombre** los enlaces con información **inadecuada, inexacta, no pertinente, no actualizada o excesiva** (doctrina del caso **Google Spain, TJUE 2014**) |
| **Derecho al olvido en redes sociales** (art. 94) | Supresión, **a simple solicitud**, de los datos que uno mismo facilitó; y si los publicaron siendo **menor**, sin más requisitos |
| **Portabilidad en redes sociales** (art. 95) | Recibir y transmitir los contenidos facilitados |
| **Testamento digital** (art. 96) | Familiares, herederos, el **albacea** o la persona designada pueden acceder a los contenidos de un fallecido y decidir sobre sus perfiles, salvo prohibición expresa |

!!! example "Caso práctico"
    Tu unidad publica en la sede electrónica la lista de admitidos de un proceso con nombre, apellidos y DNI completo. Error: debería publicarse con **nombre, apellidos y 4 cifras aleatorias del DNI** (DA 7ª). Si además se ha filtrado un Excel con datos de salud de los aspirantes, hay una **brecha**: el responsable debe notificarla a la **AEPD en 72 horas** y, por ser datos de salud (**alto riesgo**), comunicarla también a los afectados.

## Resumen de cifras

| Qué | Dato |
| --- | --- |
| RGPD | Reglamento (UE) 2016/679, de 27/04/2016; aplicable desde el 25/05/2018 |
| LOPDGDD | LO 3/2018, de 5 de diciembre |
| Edad para consentir en España | 14 años (RGPD: 16, rebajable a 13) |
| Responder a un derecho | 1 mes (+2 meses) |
| Acceso repetitivo | Más de una vez en 6 meses |
| Notificar una brecha a la AEPD | 72 horas |
| Registro de actividades: exención | Menos de 250 empleados (con excepciones) |
| Comunicar el DPD a la AEPD | 10 días |
| Respuesta del DPD a una reclamación | 2 meses (1 mes si la remite la AEPD) |
| Mandato de la Presidencia de la AEPD | 5 años, renovable |
| Procedimiento sancionador de la AEPD | 12 meses |
| Procedimiento por derechos | 6 meses |
| Multas máximas | 10 M€ / 2 % o 20 M€ / 4 % |
| Prescripción de infracciones | 3 / 2 / 1 años |
| Prescripción de sanciones | ≤ 40.000 €: 1 año; ≤ 300.000 €: 2 años; > 300.000 €: 3 años |
| Videovigilancia | Supresión en 1 mes; entrega a la autoridad en 72 horas |
| Ficheros de morosos | Máximo 5 años desde el vencimiento |
| Publicación de actos | Nombre y apellidos + 4 cifras aleatorias del DNI |
