# Las skills de Instagram para Claude

Trece skills de Claude para manejar una cuenta de Instagram, en español. Gratis,
MIT, sin registro, sin API key y sin nada que conectar.

Versión en español de **Aldush Media**, para creadores y negocios de
Latinoamérica que viven de Instagram.

Una te escribe los Reels con 26 fórmulas de gancho y califica el gancho antes
de que gastes una toma en él. Otra va y encuentra los reels que de verdad están
funcionando en tu nicho y los ordena por cuánto superó cada uno a su propia
cuenta. Otra escribe el caption y te enseña exactamente lo que muestra el feed
antes del "... más". Otra califica tu perfil sobre 100 y reescribe lo que
perdió puntos. Otra planea la semana.

Y una es el humanizador, que es la razón por la que las demás sirven. Le quita
a un borrador las rayas largas, el vocabulario de relleno y los caracteres
invisibles de marca de agua, y luego califica lo que queda con un panel de
cinco revisiones antes de que lo veas. Reconoce el relleno de IA en inglés y en
español.

**No se publica nada hasta que digas que sí.** Estas skills escriben. Tú
publicas.

## Instalación

En Claude Code:

```
/plugin marketplace add aldushmedia/skills
/plugin install instagram-agent-skill@aldushmedia
```

O copia las carpetas `plugins/instagram-agent-skill/skills/ig-*` del repo
`aldushmedia/skills` en `~/.claude/skills/`. Después abre una sesión nueva de
Claude Code.

Para un solo proyecto en vez de global, copia las mismas carpetas en
`.claude/skills/` de tu repo. ¿No usas Claude Code? Pega cualquier `SKILL.md`
al principio de un chat y funciona como un modo. Pierdes las herramientas de
Python, que son buena parte del valor de `/ig-reel` y `/ig-human`, pero lo demás
funciona.

Luego dedícale diez minutos a `templates/voice.md`. Cópialo a
`~/.claude/instagram/voice.md` y llénalo, o mándale a Claude tres de tus
propios reels y dile "escribe mi voice.md con estos". Todas las skills leen ese
archivo. Aquí importa más que en otras plataformas, porque tienes que decir las
palabras en voz alta.

## Las trece

| comando | qué hace |
| --- | --- |
| `/ig-reel` | Una idea a un Reel. Tres ganchos de [26 fórmulas](skills/ig-reel/hooks.json), calificados, luego el guion, el texto en pantalla y un guion cronometrado por bloques. |
| `/ig-viral` | Va y encuentra lo que funciona en tu nicho, lo ordena por múltiplo sobre la mediana de cada cuenta, nombra la fórmula y escribe el swipe file. |
| `/ig-caption` | El caption, revisado. Te enseña los 125 caracteres que de verdad muestra el feed antes del toque. |
| `/ig-carousel` | Publicaciones para deslizar. La portada que se gana el deslizar, el texto de cada lámina y los archivos de 1080x1350. |
| `/ig-story` | La secuencia diaria de historias, qué sticker hace qué trabajo y el embudo a DM que empieza cuando ellos se mueven primero. |
| `/ig-profile` | Califica tu perfil con una [rúbrica de 12 partes](skills/ig-profile/rubric.json) sobre 100 y luego reescribe de lo más urgente a lo menos. |
| `/ig-plan` | La semana. Qué publicar, en qué formato, cuándo y las 10 cuentas con las que interactuar. |
| `/ig-human` | El humanizador. Dos scripts que funcionan de verdad. Ver abajo. |
| `/ig-comment` | Comentarios en publicaciones de otros. Nueve tipos, elegidos según lo que de verdad es la publicación. Nunca "🔥🔥🔥". |
| `/ig-reply` | Los comentarios debajo de tu propia publicación. Los ordena en palabra clave / cliente / aporte / pregunta / apoyo / ruido y luego escribe en ese orden. |
| `/ig-dm` | La entrega por palabra clave, el primer mensaje, la propuesta de colaboración y los dos seguimientos. Dos. |
| `/ig-repurpose` | Un video, podcast o newsletter a una semana de reels y carruseles que se sostienen solos. |
| `/ig-audit` | Análisis de lo que ya publicaste. Ordena por múltiplo atípico y envíos por alcance, no por vistas. |

## Las cinco herramientas que funcionan de verdad

Sin dependencias, sin red, sin subir nada. Corren en tu máquina, con tu texto.
Los scripts son los del original y no se tocaron: imprimen sus etiquetas en
inglés (STRONG, PASS, READY...). Las salidas de ejemplo de abajo son del
original, en inglés.

### Ganchos

```bash
python3 hookscore.py hooks.txt              # ordena tus opciones
python3 beats.py script.txt --target 30     # cronométralo antes de grabar
```

```
HOOK RANKING
==============================================================================
->  85.6 STRONG  Nobody tells you that your first 30 reels are supposed to f...
        weakest: SPECIFICITY (75)
    81.4 STRONG  I lost $18,000 because of one missing contract.
        weakest: ADDRESS (70)
    54.4 OK      Stop scrolling if you want to grow on Instagram in 2026 🔥
        weakest: STAKES (70)
        dealbreaker: Opens with "stop scrolling". Asking for attention proves
                     you have not earned it.
     9.6 WEAK    Hey guys, today I wanted to talk about content strategy
        weakest: FRONTLOAD (0)
        dealbreaker: Greeting. Nobody came to the feed to be greeted.
```

`beats.py` calcula cuánto tarda en decirse cada línea, las acomoda en tiempos
y marca las cuatro cosas que matan un Reel en la edición: un gancho de más de
tres segundos, un bloque tan largo que quien mira se va, una racha de líneas
sin nada concreto y que la última línea no regrese a la primera.

```
BEAT SHEET  ·  73 words  ·  ~26.6s at 165 wpm  ·  target 30.0s
========================================================================
  0:00.0   2.9s  HOOK    I lost $18,000 because of one missing contract.
  0:02.9  14.6s  MID     Here is the exact clause I now put in every single...
                         ^ 14.6s on one beat
  0:17.4   2.9s          Section 4. Payment on delivery, not on approval.
  0:20.4   2.9s          Approval is a feeling. Delivery is a date.
  0:23.3   3.3s  CTA     That one word change is worth $18,000 to me.
------------------------------------------------------------------------
  - Beat 2 runs past 4s. Either split the line or change what is on screen
    inside it. A static frame is where people leave.
  - Loops: the last beat repeats "$18,000" from the hook. Second watches are
    free reach.
  - 3.5s under target. Either add 9 words or shoot it short. Short is usually
    right.
```

### El caption

```bash
python3 caption.py caption.txt --keywords "client contracts,freelance pricing"
```

Instagram le da a un caption unos 125 caracteres en el feed y esconde el resto
detrás de un toque. Casi todos los captions que fallan, fallan ahí. Así que lo
primero que imprime es esa ventana, en una caja, como la lee un desconocido
que va haciendo scroll:

```
  WHAT THE FEED SHOWS
  +------------------------------------------------------+
  | I lost $18,000 because of one missing clause in a    |
  | contract, and the worst part is that I had read the  |
  | thing twice before I si                              |
  +-------------------------------------------- ... more +

  PASS  LENGTH            389 / 2200 characters
  WARN  FIRST LINE        133 characters, so it gets cut at 125 mid-thought
  PASS  HOOK IS CONCRETE  2 numbers or names in the visible window
  PASS  HASHTAGS          3 tags: #freelance #contracts #agencyowner
  PASS  ONE ASK           one call to action: comment a keyword
  WARN  SEARCH TERMS      1/2 present. Missing: client contracts
```

Aplica el límite actual de hashtags, que es de **cinco por publicación**, no
treinta. Instagram lo recortó el 18 de diciembre de 2025.

### El humanizador

```bash
python3 humanize.py draft.txt --report      # límpialo y muestra cada cambio
python3 detect.py draft.txt                  # califícalo, cinco revisiones
python3 detect.py before.txt after.txt       # demuestra la diferencia
```

**Lo que sale solo:**

- **Caracteres invisibles.** Espacios y uniones de ancho cero, unidores de
  palabra, guiones suaves, marcas de orden de bytes, caracteres de etiqueta
  Unicode, separadores invisibles, espacios de no separación y espacios
  angostos. Tu teclado no los produce. Sobreviven al copiar y pegar y son
  invisibles en cualquier editor que tengas.
- **Tipografía.** Raya larga a coma, raya corta a guion, comillas curvas a
  rectas, puntos suspensivos de un carácter a tres puntos, y la puntuación
  suelta que eso deja.
- **El léxico.** 154 palabras y frases de relleno en inglés con reemplazos en
  inglés sencillo, más 128 en español con reemplazos en español natural:
  «sumérgete», «en el mundo de hoy», «desbloquea tu potencial», «potencia tu
  contenido», «es importante destacar que», y el bloque de Instagram: «deja de
  hacer scroll», «en el video de hoy», «sígueme para más», «etiqueta a alguien
  que necesite esto», «el algoritmo ama». Vive en
  [`slop.json`](skills/ig-human/slop.json) y está hecho para editarse.

**Lo que se marca en vez de arreglarse:** «No es X, es Y», «No solo X, sino
también Y», «No se trata de X. Se trata de Y.», tríadas de tres, el preámbulo
de video, listas con emojis como viñetas, tres palabras en mayúsculas
seguidas, muros de hashtags, cebo de «sígueme» por reflejo, oraciones todas
del mismo largo (en inglés y en español). Cambiar la forma de una oración
necesita criterio, así que esas regresan para reescribirse en vez de que una
regex las destroce.

Corrido contra un caption escrito para ser lo peor posible (en inglés, en el
original):

```
  BURSTINESS    ###################.....  78.4
  SPECIFICITY   #############...........  53.6    3.4 concrete markers per 100 words
  SLOP DENSITY  ........................   0.0    20 stock terms, 23.0 per 100 words
  FINGERPRINT   ################........  68.7    1 em dash
  VOICE         #################.......  70.0    9 structural tells
  ------------------------------------------------------------
  HUMAN SCORE   ########................  32.5   FLAGGED
```

Después de `humanize.py`, con las estructuras marcadas todavía sin reescribir:

```
  HUMAN SCORE   ###################.....  79.7   PASS    (+47.2)
```

### El swipe file

```bash
python3 swipe.py captured.tsv --out ~/.claude/instagram/swipe.md
```

Las vistas a secas no son evidencia. Una cuenta de 2,000,000 de seguidores que
hace 400,000 vistas tuvo un martes tranquilo. Una cuenta de 4,000 seguidores
que hace 400,000 vistas encontró algo. `swipe.py` ordena por el múltiplo sobre
la mediana de cada cuenta, nombra la fórmula de gancho (en inglés o en
español) e imprime lo que separa al tercio de arriba del de abajo.

```
SWIPE FILE  ·  4 reels  ·  4 accounts  ·  baseline: account median
==============================================================================
    60.0x  hook  57  #9  The Steal              @c                 180,000
           "steal this four line follow up it took me two years"
    37.5x  hook  86  #3  Nobody Tells You       @a                 412,000
           "nobody tells you that your first 30 reels are supposed to flop"
     1.3x  hook  13  -   unclassified           @b               1,200,000
           "in this video I am going to show you my morning routine"
```

En esta versión los nombres de las fórmulas salen en español («#9 Róbate esto»,
«#3 Nadie te dice»), porque el script los lee de `hooks.json`.

## Con contenido en español

- **Fórmulas de gancho:** cada una de las 26 regex de `hooks.json` reconoce
  ganchos en inglés y en español. Los patrones originales siguen intactos y los
  de español se agregaron al final. Cada fórmula trae un ejemplo en español que
  el clasificador reconoce, y las pruebas lo comprueban.
- **Léxico de relleno:** 128 palabras y frases típicas de IA en español con su
  reemplazo, y 12 estructuras delatoras en español, en `slop.json`.
- **Lo que sigue pensado para inglés:** la lógica de los scripts no se tocó.
  `hookscore.py` y `beats.py` cuentan palabras sin acentos y buscan palabras de
  tensión y aperturas débiles en inglés; `caption.py` solo reconoce peticiones
  en inglés («comment», «save this»); `detect.py` mide contracciones y
  pronombres del inglés. Con texto en español, esos puntajes son una
  orientación. Cada SKILL.md dice qué revisar a mano.
- **Unas pocas palabras existen igual en los dos idiomas** (`crucial`, `vital`,
  `arsenal`, `hack`) y `humanize.py` las cambia por su reemplazo en inglés.
  Revisa el texto limpio.

## Lo que se midió en el original, que es la parte que vale la pena leer

El autor original no quiso publicar un calificador de ganchos solo porque se
sentía bien, así que lo probó. El corpus son **74 ganchos reales de videos
cortos**: los primeros tres segundos de los subtítulos automáticos de los ocho
shorts con mejor y peor desempeño de cada uno de cinco canales, con vistas de
931 a 550,000. Son ganchos en inglés.

Son YouTube Shorts y no Reels, porque Instagram no te da vistas que puedas
juntar sin entrar a la cuenta de alguien, y hacer scraping violaría las
Condiciones que este repo te pide no violar. La gramática del gancho es la
misma y la fuente es pública. Es una limitación real y se dice aquí en vez de
esconderla.

**Tres resultados, dos de ellos incómodos:**

**1. Atrapa bien los ganchos malos.** Contra diez ganchos escritos mal a
propósito, AUC de 0.83, y nueve de los diez quedaron debajo de la mediana del
corpus real. Si tu gancho empieza con un saludo, un preámbulo o nada concreto,
esto te lo dice.

**2. No elige ganadores.** Separar los éxitos de un buen creador de los
fracasos de ese mismo creador: **AUC de 0.56, donde 0.50 es lanzar una moneda.** De las
cinco revisiones, solo SPECIFICITY separó los grupos de forma clara, por 60
puntos de mediana. STAKES y ADDRESS tuvieron la misma mediana en los dos
grupos, o sea que en este corpus no midieron nada.

Así que el uso honesto es: mata los ganchos obviamente débiles antes de
grabarlos y luego confía en tu propia gráfica de retención. Nada que lea texto
puede decirte cuál de dos ganchos decentes va a viajar, porque eso lo deciden
tu cara, tu edición, tu audio y a quién se lo muestra Instagram.

**3. El clasificador de fórmulas estaba roto y la prueba fue lo que lo
detectó.** Las regex `match` de `hooks.json` se escribieron primero a partir de
las plantillas y nombraban al **8%** de los ganchos reales. La gente no habla
en plantillas. Reescribirlas contra habla real transcrita lo subió al **49%**,
y entraron cuatro fórmulas porque aparecían una y otra vez y no estaban: El
dicho al revés, La estadística, La revelación y El resultado de otro, más El
superlativo. En el otro 51% se abstiene, y está bien: mucho del video corto son
clips de podcast que no tienen ninguna fórmula de gancho.

Un error arreglado que vale la pena mencionar: `SPECIFICITY` solo contaba
dígitos, así que "zero dollars" y "three marketing books" salían sin nada
concreto. Los ganchos hablados dicen sus números en voz alta.

Las regex en español de esta versión no se midieron contra un corpus real: se
escribieron a partir de las plantillas y de ganchos típicos en español. Si las usas
con ganchos reales y ves un patrón que falla seguido, agrégalo a `hooks.json`. El método para juntar ganchos de Shorts está en
[`/ig-viral`](skills/ig-viral/SKILL.md).

## La letra chica, que es la parte honesta

**Estas skills no publican en Instagram.** Existe una API real de publicación
de contenido para cuentas profesionales, y necesita una app de desarrollador
de Meta, una página vinculada, un token de larga duración y revisión de la app,
que no es algo que una skill te pueda dar. Todo lo demás que la gente usa para
automatizar publicaciones, comentarios, follows o DMs es automatización del
navegador o una herramienta de terceros, y las dos violan las
[Condiciones de uso de Instagram](https://help.instagram.com/581066165581870) y
hacen que bloqueen acciones de las cuentas. Así que cada skill termina igual:
un bloque listo para copiar, y tú lo publicas. No es una limitación que se
agregó después, es el diseño, y es la razón por la que el filtro de aprobación
es real y no un ajuste.

La única excepción son las respuestas automáticas a palabras clave en DMs, que
Instagram permite con sus propias herramientas y socios aprobados, y que solo
se disparan después de que alguien comenta primero. `/ig-dm` dice dónde está
esa línea.

**`/ig-viral` lee, no hace scraping.** Diez cuentas, una docena de reels cada
una, a velocidad humana, contigo manejando tu propio navegador. Nunca te pide
tu contraseña ni entra como tú. Recolectar en automático y en volumen es lo que
hace que restrinjan cuentas, y esto no es un crawler.

**Las cinco revisiones de detección son heurísticas locales, no API de
detectores.** Se basan en las señales que usan los detectores públicos y
corren completas en tu máquina. No son GPTZero, Originality, Copyleaks, Winston
ni Turnitin, no llaman a esos servicios y no pueden prometer sus veredictos.
Arreglar lo que miden suele mover esos números, porque miden las mismas cosas
de fondo. Eso es todo lo que se afirma. Nadie te puede vender con honestidad
algo "indetectable", y quien lo hace te está vendiendo algo.

**La pasada de caracteres invisibles es real y es acotada.** Quita los
caracteres de ancho cero y de formato que terminan en el texto generado y
sobreviven a un copiar y pegar. Es una huella real que se puede comprobar. No
es una afirmación de vencer un esquema criptográfico de marca de agua, y este
repo no la hace.

**Aquí no se inventa nada.** Ni métricas, ni clientes, ni resultados con tu
nombre. Si a un borrador le falta un número que no diste, regresa con
`{{tu número}}` adentro y un aviso, siempre.

**Los números de la plataforma caducan.** El límite de hashtags pasó de 30 a 5
en diciembre de 2025 mientras se escribía el original. Si algo de aquí
contradice lo que hace Instagram cuando lo leas, Instagram tiene la razón.

## Archivos

```
skills/ig-reel/hooks.json          26 fórmulas de gancho: plantilla, ejemplo, línea en pantalla,
                                   para qué sirve, cómo se arruina y una regex match (inglés y español)
skills/ig-reel/hookscore.py        el panel de cinco propiedades del gancho
skills/ig-reel/beats.py            del guion al guion cronometrado por bloques
skills/ig-caption/caption.py       la vista del corte y la revisión del caption
skills/ig-human/slop.json          el léxico: 282 términos, 18 clases invisibles, 28 estructuras delatoras
skills/ig-human/humanize.py        las tres pasadas de limpieza
skills/ig-human/detect.py          el panel de cinco revisiones
skills/ig-viral/swipe.py           orden por múltiplo atípico y clasificación de fórmulas
skills/ig-profile/rubric.json      la calificación del perfil sobre 100
templates/voice.md                 tu perfil de voz. Llénalo primero.
tests/                             pruebas de los datos (JSON válido, regex, ganchos y léxico en español)
```

Corre las pruebas con `python3 -m unittest discover -s tests`.

## Crédito

Basada en instagram-agent-skill (licencia MIT). Traducción y adaptación al
español de Aldush Media.

## Licencia

MIT. Tómala, cámbiala, úsala. Ver `LICENSE`.
