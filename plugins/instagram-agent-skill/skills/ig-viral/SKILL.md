---
name: ig-viral
description: >-
  Busca los reels que de verdad están funcionando ahora en el nicho del
  usuario, ordénalos por cuánto superó cada uno a su propia cuenta, nombra la
  fórmula de gancho que usó cada uno y conviértelo en un archivo de referencias
  (swipe file) del que pueda grabar. Úsala cuando el usuario diga "busca videos
  virales", "qué está funcionando ahora", "qué publica la gente de mi nicho",
  "haz ingeniería inversa de esta cuenta", "ármame un swipe file", "por qué
  este reel está pegando", o pregunte qué hacer después sin evidencia para
  contestarlo.
---

# ig-viral

La skill de investigación. Todo lo demás de este paquete escribe; esta va y
mira. Córrela cada mes, no cada día. Las fórmulas duran una temporada.

En esta carpeta hay una herramienta y funciona:

```bash
python3 swipe.py captured.tsv --out ~/.claude/instagram/swipe.md
```

## La idea que hace que valga la pena

**Las vistas a secas no son evidencia.** Una cuenta con dos millones de
seguidores que hace 400,000 vistas tuvo un martes tranquilo. Una cuenta con
cuatro mil seguidores que hace 400,000 vistas encontró algo, y ese algo se
puede copiar.

Así que aquí todo se ordena por el **múltiplo atípico**: las vistas divididas
entre la mediana reciente de esa misma cuenta. Más de 3x es una señal. Menos de
1.5x es un día normal de esa cuenta y no te enseña nada, por grande que se vea
el número.

Junta cuentas **de hasta unas 10 veces el tamaño del usuario**. Una fórmula que
funciona con 2M de seguidores muchas veces funciona porque tiene 2M de
seguidores.

## Paso 1: elige las cuentas

Pídele al usuario de 6 a 12 cuentas, o propónselas y que las apruebe:

- **4 directas:** mismo nicho, misma oferta, un poco más adelante.
- **4 vecinas:** otro nicho, la misma audiencia. De aquí se toman los formatos
  antes de que alguien del nicho los tenga.
- **De 2 a 4 enormes:** cuentas mucho más grandes, solo por el formato, nunca
  por la frecuencia ni el tono.

Pídele también que abra su propia colección de **Guardados**. Es el corpus más
rápido y relevante que existe, y ya viene filtrado por su gusto.

## Paso 2: ve y mira

Usa la herramienta de navegación que de verdad tenga esta sesión: un navegador
dentro de la app, una extensión conectada al Chrome del propio usuario, o una
herramienta de uso de computadora. No hay API para esto y no hace falta,
porque el volumen es tan chico que se puede leer.

**Reglas que no se negocian:**

- **Nunca inicies sesión en Instagram por el usuario ni le pidas su
  contraseña.** Si una página pide iniciar sesión, el que ya tiene la sesión
  abierta es el usuario. Maneja su navegador con él presente, o pídele que
  pegue la información.
- **Esto es leer, no hacer scraping.** Diez cuentas, una docena de reels cada
  una, a velocidad humana. Recolectar en automático y en volumen viola las
  Condiciones de uso de Instagram y hace que bloqueen acciones de la cuenta.
  No armes un crawler, no uses un servicio de scraping y no lo dejes corriendo
  en segundo plano.
- **Copia la fórmula, nunca el video.** La forma del gancho, la estructura, la
  duración, el patrón de cortes. No su guion, no su voz, no su edición.
  Atribuye cada fila del swipe file a la cuenta de donde salió.

**Qué capturar de cada reel**, con las palabras del propio creador:

| campo | notas |
| --- | --- |
| account | usuario |
| followers | del perfil |
| median | mira por encima los últimos 12 reels y toma las vistas del de en medio |
| views | este reel |
| hook | la primera línea, hablada o en pantalla, tal cual, con todo y errores |
| on-screen | la primera tarjeta de texto, si es distinta |
| length | segundos |
| cta | qué pidió al final |

La mediana es la importante. Sin ella vuelves a ordenar por número de
seguidores, que es justo lo que esta skill existe para evitar.

**Cuando Instagram no te deja ver suficiente:** la misma gramática de ganchos
funciona en YouTube Shorts, donde las vistas y las transcripciones son
públicas y no hay que iniciar sesión. Es un segundo corpus legítimo, y el
gancho hablado es más fácil de conseguir:

```bash
# vistas de los shorts de un canal
python3 -m yt_dlp --flat-playlist --playlist-end 40 -J \
  "https://www.youtube.com/@HANDLE/shorts" > channel.json

# la primera línea hablada de un short, de sus subtítulos automáticos
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs "en.*" \
  --sub-format json3 -o hook "https://www.youtube.com/watch?v=VIDEO_ID"
```

Para Shorts en español, cambia `"en.*"` por `"es.*"`. Toma cada palabra de los
subtítulos con marca de tiempo menor a 3.0 segundos. Ese es el gancho como se
dijo, no como se escribió.

## Paso 3: ordénalo

Llena un archivo separado por tabuladores, con una fila de encabezado, y corre
el script. Los encabezados se quedan en inglés porque el script los lee así:

```
account	followers	median	views	hook
@alguien	48000	11000	412000	nadie te dice que tus primeros 30 reels tienen que fracasar
```

```bash
python3 swipe.py captured.tsv --out ~/.claude/instagram/swipe.md
```

Calcula el múltiplo atípico, nombra la fórmula de gancho con las mismas 26
fórmulas con las que escribe `/ig-reel` (reconoce ganchos en inglés y en
español), califica cada gancho con `hookscore.py` e imprime lo que separa al
tercio de arriba del tercio de abajo. El script imprime sus etiquetas en
inglés; los nombres de las fórmulas salen en español porque los lee de
`hooks.json`. El puntaje de gancho está calibrado para inglés: con ganchos en
español tómalo como orientación.

## Paso 4: di qué significa, con cuidado

Reporta tres cosas y nada más:

1. **Qué fórmulas sobresalen** en el tercio de arriba, con conteos. Dos
   fórmulas que aparecen cuatro veces cada una en seis cuentas es un hallazgo.
   Una que aparece dos veces no lo es.
2. **Qué tiene en común el tercio de arriba en estructura** que el de abajo no
   tiene: largo del gancho, si la recompensa es visual, si el primer cuadro se
   mueve, dónde va la petición.
3. **Las filas sin clasificar.** Cada gancho que el clasificador no pudo
   nombrar es ruido o una fórmula que todavía no está en `hooks.json`. Léelos
   a mano. Es la columna más valiosa de la salida y es la razón por la que el
   script imprime el conteo.

Luego di el tamaño de la muestra y la confianza en palabras simples. Cuarenta
reels de seis cuentas sostienen una afirmación. Doce no, y decirlo es la
diferencia entre investigar y leer el horóscopo.

## Paso 5: conviértelo en algo para grabar

Para las tres fórmulas de arriba, escribe **la versión del usuario**: su propia
historia, su propio número, con la forma que está funcionando. Pásale cada una
a `/ig-reel` con el número de fórmula ya elegido.

Nunca entregues "haz un reel como este". Entrega una frase de gancho que
podría decir mañana.

## Salida

```
SWIPE  ·  38 reels  ·  7 cuentas  ·  base: mediana de la cuenta

ATÍPICOS (más de 3x)
  38.4x  gancho 86  #3  Nadie te dice   @cuenta_a    412,000  (mediana 10,700)
  11.2x  gancho 79  #9  Róbate esto     @cuenta_c    180,000  (mediana 16,100)
  ...

LO QUE SOBRESALE
  #3 Nadie te dice        x5 en el tercio de arriba, 0 en el de abajo
  #2 La orden negativa    x4
  largo mediano del gancho  8 palabras arriba, 19 abajo

SIN CLASIFICAR (6)
  Dos tienen la misma forma y no está en hooks.json: un gancho que
  empieza leyendo en voz alta el comentario de otra persona. Vale la pena agregarla.

TU VERSIÓN
  #3  "Nadie te dice que las primeras 20 propuestas se van a perder."
  ...
```

Escribe el swipe file en `~/.claude/instagram/swipe.md`. `/ig-reel` y `/ig-plan`
lo leen, y esa es la idea: después de correr esto una vez, el resto del
paquete trabaja con la evidencia del propio usuario en vez de con valores por
defecto.

Esta skill no publica, no sigue, no da like ni manda mensajes. Solo lee.
