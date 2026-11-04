---
name: ig-reel
description: >-
  Escribe un Reel de Instagram a partir de una idea en bruto: opciones de
  gancho con 26 fórmulas, el guion hablado, el texto en pantalla y un guion
  cronometrado por bloques, con la voz del usuario y calificado antes de
  grabar. Úsala cuando el usuario quiera un Reel, un guion de video corto, un
  gancho, una voz en off, "hazme un reel sobre X", "qué digo en este video", o
  esté por grabar y todavía no tenga la primera línea.
---

# ig-reel

Convierte una idea en bruto en un Reel que la gente termina de ver.

En esta carpeta hay dos herramientas y las dos funcionan de verdad. Úsalas. No
calcules el gancho a ojo ni adivines la duración.

```bash
python3 hookscore.py hooks.txt              # ordena tus opciones de gancho
python3 hookscore.py --hook "one line"      # califica uno solo
python3 beats.py script.txt --target 30     # guion cronometrado antes de grabar
```

**Con ganchos en español:** los scripts calculan a partir del texto con reglas
pensadas para inglés (palabras de tensión, aperturas débiles, cómo se dirige a
quien mira, y letras sin acento al contar palabras). Con un gancho en español
el puntaje sirve como orientación, no como veredicto: STAKES, FRONTLOAD y
ADDRESS suelen salir más bajos de lo que merecen. Revisa tú esas tres a mano
con la misma idea (algo en juego, lo interesante al principio, hablarle a una
persona) y dilo en el resumen.

## Antes de escribir

1. Lee `~/.claude/instagram/voice.md` si existe. Es el perfil de voz del
   usuario: cómo habla a cámara, qué nunca dice, a quién le habla. Si no
   existe, pide **tres de sus propios reels**, transcríbelos o léelos, deduce
   la voz y escribe el archivo. Un guion con la voz equivocada no sirve, porque
   lo tiene que decir en voz alta.
2. Lee `hooks.json` en esta carpeta. 26 fórmulas, cada una con plantilla,
   ejemplo lleno, versión en pantalla, para qué sirve y cómo se arruina. Cuatro
   de ellas están ahí porque aparecían una y otra vez en ganchos reales, no
   porque completaran un patrón.
3. Si la idea es flaca, no la rellenes. Haz una sola pregunta con todo junto:
   qué pasó, a quién, y cuánto costó o cuánto dejó. Un Reel necesita una cosa
   concreta y cierta. Consíguela antes de escribir.
4. Si existe `~/.claude/instagram/swipe.md`, léelo. `/ig-viral` escribe ese
   archivo, y es la evidencia del propio usuario sobre qué fórmulas están
   funcionando en su nicho ahora mismo. Pesa más que lo que dice este archivo.

## La forma

Un Reel se decide en los primeros dos segundos y se sostiene en los cinco
siguientes.

```
0:00 - 0:02   GANCHO        la afirmación. Frase hablada y frase en pantalla,
                            escritas por separado. Movimiento en el primer
                            cuadro, no una cara quieta.
0:02 - 0:07   LO QUE ESTÁ   por qué le importa a quien está mirando. Una línea.
              EN JUEGO
0:07 - ...    EL CUERPO     una idea por bloque, y el cuadro cambia en cada uno.
ÚLTIMOS 3s    LA RECOMPENSA cumple lo que prometió el gancho y luego la única
                            petición.
ÚLTIMA LÍNEA  EL LOOP       repite una palabra del gancho para que la
                            repetición entre limpia.
```

Duración: de 15 a 45 segundos es el rango que funciona. Los Reels pueden durar
hasta 3 minutos y casi nadie debería usarlos. Por debajo de 7 segundos se
inflan las repeticiones y nada más.

## El ciclo

**1. Elige tres ganchos, no uno.** Pasa la idea por `hooks.json`, escoge tres
fórmulas que de verdad le queden y escribe la frase hablada y la de pantalla
de cada una. Fórmulas distintas, no tres versiones de la misma.

**2. Califícalos.** Pon las tres frases habladas en un archivo, una por línea,
y corre `hookscore.py`. Muéstrale al usuario el orden. Si el primero queda
debajo de 50, todavía no tienes el gancho, y ninguna edición lo arregla.

**3. Escribe el guion** con el gancho ganador. Lenguaje hablado y sencillo,
como de verdad habla el usuario. Frases cortas. Ninguna oración que tenga que
ensayar.

**4. Cronométralo.** Corre `beats.py script.txt --target {length}`. Arregla
cada aviso: un gancho de más de 3 segundos, cualquier bloque de más de 4
segundos, una racha de bloques sin nada concreto, falta de loop. Vuelve a
correrlo hasta que quede limpio.

**5. Humanízalo.** Pasa el guion por `/ig-human` antes de mostrarlo. Una línea
que suena escrita se nota en cuanto alguien la dice en voz alta.

**6. Imprime el bloque.** El guion en un bloque de código, el texto en
pantalla como una lista aparte con tiempos, y luego:

```
REEL LISTO
gancho:       #3 Nadie te dice, calificado 86 STRONG
duración:     28.4s en 9 bloques a 165 ppm
en pantalla:  6 tarjetas
humanizador:  4 rastros quitados, puntaje humano 81 PASS
caption:      corre /ig-caption después

Responde "sí" para registrarlo, o dime qué cambio.
```

**7. Nunca publiques.** Esta skill produce un guion. El usuario lo graba y lo
publica. Con un "sí", agrega a `~/.claude/instagram/log.md` la fecha, la
fórmula de gancho usada y la primera línea, para que `/ig-audit` tenga
historial después.

## El texto en pantalla es otro guion

Escríbelo por separado, siempre. Se lee antes de que se escuche.

- **Seis palabras o menos por tarjeta.** Lo lee, con el brazo estirado,
  alguien que todavía no está escuchando.
- **La tarjeta del gancho está desde el cuadro 1**, no después de un silencio.
- **Mantenlo dentro de la zona segura.** En un cuadro de 1080x1920, nada arriba
  de y=230 ni abajo de y=1440, y deja libres los 230 píxeles de la derecha. La
  interfaz queda encima de todo lo que está fuera de esa caja: el caption, la
  barra de botones, la franja del audio.
- **Nunca pongas el gancho donde va el caption.** Es la parte de abajo del
  cuadro y queda tapada.
- **Pon subtítulos fijos en el cuerpo.** Casi todos ven primero sin sonido.

## Reglas que hacen la diferencia

- **Una idea por Reel.** Si el guion tiene dos, tienes dos Reels. Dilo.
- **Números en lugar de adjetivos.** "$4,200" le gana a "un montón". Si el
  usuario no dio un número, pídelo en vez de escribir alrededor del hueco.
- **Corta la intro.** Sin saludo, sin "en este video", sin nombre, sin logo
  animado. El video empieza en la frase a la que normalmente llegarías en el
  segundo seis.
- **Cambia el cuadro en cada bloque.** Una toma fija de 8 segundos es donde la
  gente se va, y `beats.py` lo va a marcar.
- **Una sola petición al final.** Comenta una palabra clave, guárdalo o sígueme.
  Una.
- **Nunca inventes.** Ni métricas, ni clientes, ni ingresos, ni resultados con
  el nombre del usuario, ni siquiera de relleno. Si hace falta un número y no
  lo sabes, deja `{{tu número}}` en el guion y márcalo.
- **No escribas un guion alrededor de un audio en tendencia que el usuario no
  puede usar.** Si la idea necesita la voz del usuario, dilo.

## Ejemplo

```
/ig-reel bajamos el tiempo de cada propuesta de 5 horas a 20 minutos con una plantilla
```

```
GANCHOS  (calificados)
  86  STRONG  #5  El tiempo comprimido   "Las propuestas me tomaban cinco horas. Ahora, veinte minutos."
                                         en pantalla: 5 HORAS -> 20 MIN
  71  STRONG  #1  La confesión del costo "Cobré cuatro horas a la semana solo por dar formato. Durante dos años."
                                         en pantalla: 2 AÑOS PERDIDOS
  54  OK      #9  Róbate esto            "Róbate la plantilla de propuesta que lo logró."
                                         en pantalla: RÓBATE ESTO

Grabamos el #5: la proporción es creíble, se entiende de un vistazo en
pantalla y el número es tuyo.
```
