---
title: Bloque III · Desarrollo de sistemas
description: Modelado de datos, programación, SQL, POO y UML, Java y .NET, arquitecturas, web, accesibilidad y metodologías.
order: 4
---

## III.1 Modelado de datos y diseño de bases de datos

- **Fases del diseño:** conceptual (modelo entidad-relación, independiente del SGBD), lógico (modelo relacional: tablas) y físico (índices, particiones, almacenamiento en un SGBD concreto).
- **Modelo E/R (Chen):** entidades (fuertes y débiles), atributos (simples, compuestos, multivaluados, derivados), relaciones y **cardinalidades** 1:1, 1:N y N:M. Generalización/especialización (jerarquías con restricciones de totalidad y exclusividad).
- **Paso a tablas:** cada entidad es una tabla; una relación 1:N añade la clave del lado "1" como clave foránea en el lado "N"; una relación **N:M crea una tabla intermedia** con las dos claves.
- **Claves:** superclave, candidata, **primaria** (no nula y única), alternativa y **foránea** (referencia a la primaria de otra tabla).
- **Integridad:** de entidad (la clave primaria no puede ser nula) y referencial (toda clave foránea apunta a una fila existente o es nula). Acciones ON DELETE / ON UPDATE: CASCADE, SET NULL, RESTRICT.
- **Álgebra relacional:** selección (σ, filas), proyección (π, columnas), producto cartesiano, unión, diferencia, intersección y *join*.

**Normalización:**

| Forma | Condición |
| --- | --- |
| 1FN | Valores atómicos: sin grupos repetitivos ni atributos multivaluados |
| 2FN | 1FN + todo atributo no clave depende de la clave completa (sin dependencias parciales) |
| 3FN | 2FN + sin dependencias transitivas entre atributos no clave |
| FNBC | Todo determinante es clave candidata |
| 4FN y 5FN | Sin dependencias multivaluadas ni de reunión |

Ejemplo resuelto: la tabla PEDIDO(num_pedido, cod_producto, nombre_producto, cantidad, dni_cliente, nombre_cliente) con clave (num_pedido, cod_producto) no está en 2FN, porque nombre_producto depende solo de cod_producto. Se descompone en PRODUCTO(cod_producto, nombre_producto), PEDIDO(num_pedido, dni_cliente) y LINEA_PEDIDO(num_pedido, cod_producto, cantidad). Para llegar a 3FN, nombre_cliente sale a CLIENTE(dni_cliente, nombre_cliente), porque depende de dni_cliente y no de la clave del pedido.

## III.2 Lenguajes de programación

- **Clasificación:** por nivel (máquina, ensamblador, alto nivel); por paradigma (imperativo/estructurado como C, orientado a objetos como Java y C#, funcional como Haskell, lógico como Prolog, declarativo como SQL); por ejecución (compilados como C, interpretados como Python o JavaScript, o híbridos con bytecode y máquina virtual como Java y C#).
- **Tipos de datos:** primitivos (entero, real, carácter, booleano) y compuestos (array, registro/struct, cadena). Tipado estático (Java) o dinámico (Python, JS); fuerte o débil.
- **Operadores:** aritméticos, relacionales, lógicos (AND, OR, NOT, con evaluación en cortocircuito), de asignación y a nivel de bit. Precedencia: los aritméticos antes que los relacionales, y estos antes que los lógicos.
- **Estructuras de control (teorema de Böhm-Jacopini):** secuencia, selección (if/else, switch) e iteración (while, do-while, for).
- **Subprogramas:** procedimientos y funciones. Paso de parámetros **por valor** (se copia; los cambios no salen) o **por referencia** (se pasa la dirección; los cambios sí salen). Ámbito local y global. **Recursividad**: una función que se llama a sí misma, con caso base.
- **Excepciones:** try/catch/finally. En Java hay excepciones comprobadas (checked) y no comprobadas (RuntimeException).

Ejemplo resuelto (Java):

```java
int f(int n) {
    if (n <= 1) return 1;        // caso base
    return n * f(n - 1);         // llamada recursiva
}
// f(4) = 4 * 3 * 2 * 1 = 24
```

Pregunta típica: ¿qué imprime `int x = 7 / 2; System.out.println(x % 2);`? La división entera da 3 y 3 % 2 = **1**.

## III.3 SQL, procedimientos almacenados y disparadores

| Sublenguaje | Sentencias |
| --- | --- |
| DDL (definición) | CREATE, ALTER, DROP, TRUNCATE, RENAME |
| DML (manipulación) | SELECT, INSERT, UPDATE, DELETE, MERGE |
| DCL (control) | GRANT, REVOKE |
| TCL (transacciones) | COMMIT, ROLLBACK, SAVEPOINT |

- **Orden lógico de un SELECT:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. Por eso WHERE filtra filas antes de agrupar y HAVING filtra grupos.
- **JOIN:** INNER (solo coincidencias), LEFT/RIGHT OUTER (todas las de un lado y nulos en el otro), FULL OUTER, CROSS (producto cartesiano) y SELF JOIN.
- **Funciones de agregado:** COUNT, SUM, AVG, MIN, MAX. `COUNT(*)` cuenta filas; `COUNT(columna)` ignora los NULL.
- **Operadores:** LIKE ('%' cualquier cadena, '_' un carácter), IN, BETWEEN (incluye extremos), IS NULL (nunca `= NULL`), EXISTS, UNION (sin duplicados) frente a UNION ALL.
- **Otros objetos:** vistas (consultas almacenadas), índices (aceleran búsquedas y penalizan escrituras), secuencias, restricciones (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL, DEFAULT).
- **Procedimientos almacenados y funciones:** código en el servidor (PL/SQL en Oracle, T-SQL en SQL Server, PL/pgSQL en PostgreSQL). Una función devuelve un valor; un procedimiento no necesariamente.
- **Disparadores (triggers):** se ejecutan automáticamente ante INSERT, UPDATE o DELETE, BEFORE o AFTER, a nivel de fila o de sentencia. Se usan para auditoría y reglas de negocio.
- **Acceso desde programas:** JDBC (Java), ODBC, ADO.NET; ORM como JPA/Hibernate o Entity Framework.
- **DELETE vs TRUNCATE vs DROP:** DELETE borra filas (admite WHERE y ROLLBACK); TRUNCATE vacía la tabla entera (DDL, rápido); DROP elimina la tabla y su estructura.

Ejemplo resuelto. Tablas EMPLEADO(id, nombre, salario, id_dpto) y DEPARTAMENTO(id_dpto, nombre). Departamentos con salario medio superior a 2.000 €, ordenados de mayor a menor:

```sql
SELECT d.nombre, AVG(e.salario) AS media
FROM EMPLEADO e
INNER JOIN DEPARTAMENTO d ON e.id_dpto = d.id_dpto
GROUP BY d.nombre
HAVING AVG(e.salario) > 2000
ORDER BY media DESC;
```

Trigger de auditoría (sintaxis de Oracle):

```sql
CREATE OR REPLACE TRIGGER trg_audit_salario
AFTER UPDATE OF salario ON EMPLEADO
FOR EACH ROW
BEGIN
  INSERT INTO AUDITORIA(id_emp, salario_old, salario_new, fecha)
  VALUES (:OLD.id, :OLD.salario, :NEW.salario, SYSDATE);
END;
```

## III.4 Programación orientada a objetos, patrones y UML

- **Conceptos:** clase (plantilla), objeto (instancia), atributos y métodos, constructor, **encapsulación** (ocultar el estado; modificadores private, protected, public), **herencia** (una subclase extiende una superclase; Java solo permite herencia simple de clases y múltiple de interfaces), **polimorfismo** (sobrecarga en compilación y sobrescritura en ejecución) y **abstracción** (clases abstractas e interfaces).
- **Relaciones entre clases:** asociación, **agregación** (el todo y las partes existen por separado; rombo vacío), **composición** (las partes mueren con el todo; rombo relleno), herencia/generalización (triángulo vacío), dependencia y realización (interfaz).
- **Principios SOLID:** responsabilidad única, abierto/cerrado, sustitución de Liskov, segregación de interfaces e inversión de dependencias.
- **Patrones GoF (23):** creacionales (**Singleton**, Factory Method, Abstract Factory, Builder, Prototype), estructurales (Adapter, Bridge, Composite, **Decorator**, **Facade**, Flyweight, Proxy) y de comportamiento (**Observer**, **Strategy**, Command, Iterator, State, Template Method, Chain of Responsibility, Mediator, Memento, Visitor, Interpreter).
- **Patrones de arquitectura:** MVC (modelo, vista y controlador), MVVM, capas, DAO, inyección de dependencias.
- **UML 2.5 (14 diagramas):** de estructura (clases, objetos, componentes, despliegue, paquetes, estructura compuesta, perfiles) y de comportamiento (casos de uso, actividad, máquina de estados) e interacción (secuencia, comunicación, tiempos, visión global).
- **Casos de uso:** actores, casos de uso, relaciones «include» (siempre se ejecuta) y «extend» (opcional, bajo condición).

Ejemplo práctico: en una aplicación de expedientes, "Tramitar expediente" siempre incluye "Autenticarse con Cl@ve" («include»), y puede extenderse con "Solicitar subsanación" si falta documentación («extend»). Para que solo exista una conexión al servicio de notificaciones en toda la aplicación, se usa el patrón Singleton; para avisar a varios módulos cuando cambia el estado del expediente, Observer.

## III.5 Plataformas Java (Jakarta EE) y .NET

|  | Java / Jakarta EE | .NET |
| --- | --- | --- |
| Compilación | Código fuente → bytecode (.class) → JVM con compilador JIT | C#, VB.NET o F# → CIL → CLR con JIT |
| Kits | JDK (desarrollo) incluye JRE (ejecución) | .NET SDK y runtime; .NET 8/9 multiplataforma |
| Web | Servlets, JSP, JSF, JAX-RS (REST), Spring Boot | ASP.NET Core (MVC, Razor Pages, Web API, Blazor) |
| Persistencia | JPA (Hibernate), JDBC | Entity Framework Core, ADO.NET |
| Componentes | EJB, CDI (inyección de dependencias), JMS (mensajería) | Inyección de dependencias integrada |
| Empaquetado | JAR, WAR, EAR; servidores Tomcat, WildFly, WebLogic | DLL / ensamblados; servidor Kestrel, IIS |
| Construcción | Maven (pom.xml), Gradle | NuGet, MSBuild |

Nota: Java EE pasó a la Fundación Eclipse con el nombre de **Jakarta EE** y los paquetes `javax.*` cambiaron a `jakarta.*`. El recolector de basura (garbage collector) libera memoria automáticamente en ambas plataformas.

## III.6 Arquitecturas cliente/servidor, multicapa y servicios web

- **Cliente/servidor:** cliente ligero (solo presentación) o pesado (parte de la lógica). **Tres capas:** presentación, lógica de negocio y datos.
- **SOA:** servicios reutilizables con un bus de servicios (ESB). **Microservicios:** servicios pequeños, desplegables por separado, cada uno con sus propios datos, comunicados por API o mensajería; requieren API Gateway, descubrimiento de servicios y observabilidad.
- **SOAP:** protocolo con mensajes XML (sobre, cabecera y cuerpo), contrato **WSDL**, estándares WS-* (WS-Security). **REST:** estilo de arquitectura sobre HTTP con recursos identificados por URI, sin estado, normalmente con JSON, documentado con OpenAPI/Swagger.
- **Métodos HTTP en REST:** GET (leer, seguro e idempotente), POST (crear, no idempotente), PUT (reemplazar, idempotente), PATCH (modificar parcialmente), DELETE (borrar, idempotente).
- **Otros:** GraphQL, gRPC (HTTP/2 + Protocol Buffers), WebSockets (comunicación bidireccional), colas de mensajes (RabbitMQ, Kafka). Autenticación con OAuth 2.0, OpenID Connect y tokens JWT.

Ejemplo práctico: una API REST de expedientes. `GET /expedientes/123` devuelve 200 con el JSON; `POST /expedientes` crea uno y devuelve 201 Created; `DELETE /expedientes/123` devuelve 204 No Content; si no existe, 404.

## III.7 Aplicaciones web: front-end y servidor

- **HTML5:** etiquetas semánticas (header, nav, main, article, section, aside, footer), formularios con validación (required, type="email"), audio y vídeo nativos, canvas, almacenamiento local (localStorage, sessionStorage).
- **CSS3:** selectores, **cascada y especificidad** (inline > id > clase/atributo/pseudoclase > elemento; `!important` lo sobrescribe todo), modelo de caja (content, padding, border, margin), Flexbox, Grid, media queries (diseño adaptable o *responsive*).
- **JavaScript:** DOM, eventos, `let`/`const` frente a `var`, funciones flecha, promesas y `async`/`await`, `fetch` y AJAX, JSON. TypeScript añade tipado estático. Frameworks: Angular, React y Vue.
- **XML:** documento bien formado (sintaxis correcta) frente a válido (cumple una DTD o un XSD); XPath (consultas), XSLT (transformaciones), espacios de nombres.
- **Servidor:** PHP, Java (Servlets, Spring), C# (ASP.NET), Python (Django, Flask), Node.js (Express). Sesiones y cookies (atributos HttpOnly, Secure, SameSite).
- **Otros conceptos:** SPA frente a aplicación multipágina, renderizado en servidor (SSR), PWA, CORS, CDN.

Ejemplo práctico: `<p id="aviso" class="rojo">` con las reglas `#aviso { color: blue }` y `.rojo { color: red }` se ve azul, porque el selector de id es más específico que el de clase.

## III.8 Accesibilidad, usabilidad y seguridad en el desarrollo

- **Normativa:** RD 1112/2018 sobre accesibilidad de sitios web y aplicaciones móviles del sector público (transpone la Directiva (UE) 2016/2102). Norma **UNE-EN 301 549**, que remite a las **WCAG 2.1 nivel AA**. Las WCAG 2.2 (2023) añaden criterios.
- **Principios WCAG (POUR):** Perceptible, Operable, Comprensible y Robusto. Niveles A, AA y AAA (la Administración debe cumplir AA).
- **Obligaciones:** declaración de accesibilidad en cada web, mecanismo de comunicación y quejas, revisiones periódicas. El Observatorio de Accesibilidad Web (OAW) supervisa la AGE.
- **Buenas prácticas:** texto alternativo en imágenes (atributo `alt`), contraste mínimo de 4,5:1 en texto normal (AA), navegación completa con teclado, etiquetas `<label>` en formularios, no transmitir información solo con el color, subtítulos en vídeos, atributos ARIA solo cuando el HTML no basta.
- **Usabilidad:** las 10 heurísticas de Nielsen (visibilidad del estado del sistema, prevención de errores, consistencia, control del usuario…), ISO 9241-11 (eficacia, eficiencia y satisfacción), diseño centrado en el usuario, pruebas con usuarios.
- **Seguridad (OWASP Top 10):** control de acceso roto, fallos criptográficos, **inyección** (SQL, comandos), diseño inseguro, configuración incorrecta, componentes vulnerables, fallos de autenticación, fallos de integridad, fallos de registro y monitorización, SSRF. Defensas: consultas parametrizadas, validación de entradas, codificación de salidas (contra XSS), tokens anti-CSRF, contraseñas con hash y *salt* (bcrypt, Argon2), principio de mínimo privilegio.

Ejemplo práctico de inyección SQL. El código vulnerable `"SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"` permite entrar escribiendo `' OR '1'='1`. La solución es una consulta parametrizada:

```java
PreparedStatement ps = con.prepareStatement(
    "SELECT * FROM usuarios WHERE nombre = ?");
ps.setString(1, nombre);
```

## III.9 Metodologías, pruebas, control de versiones y documentación

- **Ciclos de vida:** cascada, en V (cada fase de desarrollo tiene su fase de prueba), incremental, iterativo, espiral (Boehm, centrado en riesgos) y prototipado.
- **Métrica v3** (metodología de la Administración española). Procesos: PSI (Planificación de Sistemas de Información), desarrollo con EVS (Estudio de Viabilidad), ASI (Análisis), DSI (Diseño), CSI (Construcción) e IAS (Implantación y Aceptación), y MSI (Mantenimiento). Interfaces: gestión de proyectos, seguridad, gestión de la configuración y aseguramiento de la calidad.
- **Scrum:** roles (Product Owner, Scrum Master, Developers); eventos (Sprint de hasta 1 mes, Sprint Planning, **Daily de 15 minutos**, Sprint Review y Retrospectiva); artefactos (Product Backlog, Sprint Backlog e Incremento, con Definition of Done).
- **Otras ágiles:** Kanban (tablero, límite de trabajo en curso o WIP), XP (programación en parejas, TDD, integración continua), Lean. DevOps: integración y entrega continuas (CI/CD) con Jenkins, GitLab CI o GitHub Actions.
- **Pruebas:** por nivel, unitarias (JUnit, NUnit), de integración, de sistema y de aceptación; caja blanca (estructura interna, cobertura de código) y caja negra (entradas y salidas; partición de equivalencia y valores límite); de regresión, de rendimiento y carga (JMeter), de seguridad, de usabilidad. TDD: primero el test, luego el código.
- **Mantenimiento:** correctivo, adaptativo, perfectivo y preventivo.
- **Control de versiones (Git):** `git init`, `clone`, `add`, `commit`, `push`, `pull`, `branch`, `checkout` / `switch`, `merge`, `rebase`, `stash`, `tag`. Flujos de trabajo GitFlow (main, develop, feature, release, hotfix) y trunk-based. Plataformas: GitHub, GitLab. Antes se usaban CVS y Subversion (centralizados).
- **Repositorios de artefactos y generación de código:** Maven Central, Nexus, Artifactory, npm; generadores (Swagger Codegen, scaffolding de frameworks).
- **Documentación:** Javadoc, comentarios, manuales de usuario y técnico, README, OpenAPI. Calidad del código: SonarQube, deuda técnica.

Ejemplo práctico: un campo admite edades de 18 a 65. Por la técnica de valores límite, se prueban 17, 18, 65 y 66. Por partición de equivalencia, un valor válido (40) y uno de cada clase no válida (10 y 80).
