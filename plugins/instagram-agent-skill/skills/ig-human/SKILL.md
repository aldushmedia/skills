---
name: ig-human
description: >-
  Quita la huella de máquina de cualquier borrador (rayas largas, palabras de
  relleno de IA, caracteres invisibles de marca de agua) y califícalo con un
  panel de detección de cinco revisiones antes de que salga. Úsala siempre que
  un texto tenga que sonar humano, cuando el usuario diga humaniza, "esto suena
  a IA", "quita las rayas largas", "quítale el relleno", "esto suena a
  ChatGPT", o antes de mostrarle al usuario cualquier caption, guion,
  comentario, respuesta o DM.
---

# ig-human

En esta carpeta hay dos herramientas y las dos funcionan de verdad. Úsalas. No
lo hagas a ojo.

```bash
python3 humanize.py draft.txt --report        # límpialo y muestra qué cambió
python3 detect.py draft.txt                    # califícalo, cinco revisiones
python3 detect.py before.txt after.txt         # demuestra la diferencia
```

Las dos leen `slop.json`: 154 palabras y frases de relleno en inglés con
reemplazos en inglés sencillo, más 128 en español con reemplazos en español
natural; 18 clases de caracteres invisibles, 11 sustituciones tipográficas y
28 estructuras delatoras (16 originales y 12 en español). El último bloque en
inglés de cada lista es propio de Instagram, el vocabulario que solo aparece en
captions y voces en off. Está hecho para editarse. Si el usuario tiene una
palabra que siempre usa y el léxico se la quita, sácala del archivo.

## Con textos en español

El léxico en español ya está en `slop.json` («sumérgete», «en el mundo de hoy»,
«desbloquea tu potencial», «potencia tu contenido», «sígueme para más» y
muchas más), y las estructuras «No es X, es Y», «No solo X, sino también Y» y
«No se trata de X. Se trata de Y.» se marcan. Tres cosas que debes saber:

- Unas pocas palabras de la lista original existen igual en español
  (`crucial`, `vital`, `arsenal`, `hack`) y `humanize.py` las cambia por su
  reemplazo en inglés. Revisa el texto limpio y corrígelas a mano si
  aparecen. Las frases en español más comunes con esas palabras («es
  crucial», «es vital», «un arsenal de») ya tienen reemplazo en español y se
  aplican primero.
- `detect.py` cuenta contracciones y pronombres del inglés en la revisión
  VOICE, así que un texto en español saca menos puntos ahí aunque suene
  humano. Lee esa revisión con criterio: lo que importa es que hable en
  primera y segunda persona y que no tenga estructuras delatoras.
- Las comillas «» y los signos ¿¡ no se tocan: son normales en español.

## Por qué esto importa en Instagram más de lo que parece

Los captions son cortos y los guiones se dicen en voz alta. Una línea que suena
escrita en un caption de 600 caracteres es una parte más grande del texto que
la misma línea en un ensayo, y una voz en off que nadie diría con naturalidad
se nota en la primera toma. Lo que delata aquí no es un detector que marca la
publicación. Es una persona que pasa de largo porque suena a marca, o un
creador que se traba con su propio guion.

## Lo que se arregla solo

**1. Caracteres invisibles.** Espacios y uniones de ancho cero, unidores de
palabra, guiones suaves, marcas de orden de bytes, caracteres de etiqueta
Unicode, separadores invisibles, espacios de no separación y espacios
angostos. Un teclado no los produce. Sobreviven al copiar y pegar, son
invisibles en cualquier editor y son lo más mecánico del texto generado.
`humanize.py` los borra todos, incluido cualquier otro carácter de formato
Unicode que no tenga nombrado.

**2. Tipografía.** Raya larga a coma, raya corta a guion, comillas curvas a
rectas, puntos suspensivos de un solo carácter a tres puntos, viñeta a guion.
La que importa es la de la raya larga: la convierte en coma y luego limpia la
doble puntuación y los puntos sueltos que deja.

**3. El léxico de relleno.** delve, leverage, robust, seamless, crucial,
testament to, "in today's fast-paced world", y en español «sumérgete», «en el
mundo de hoy», «desbloquea tu potencial», «es importante destacar que»; más el
bloque de Instagram: "stop scrolling", "follow for more", «deja de hacer
scroll», «en el video de hoy», «sígueme para más», «etiqueta a alguien que
necesite esto», «el algoritmo ama». Cada uno se cambia por una palabra
sencilla o se borra, respetando mayúsculas y sin tocar las URL.

## Lo que NO se arregla solo

Las estructuras delatoras se **marcan, no se reescriben**, porque cambiar la
forma de una oración necesita criterio:

- «No es X, es Y» y «No solo X, sino también Y» (y sus versiones en inglés)
- Tríadas de tres
- Líneas de pregunta retórica: «¿El resultado?»
- El preámbulo de video: «en este video te voy a enseñar»
- Listas con emojis como viñetas
- Tres o más palabras en mayúsculas seguidas
- Muros de hashtags
- Cebo por reflejo: «sígueme para más», «etiqueta a alguien que», «dale like si»

Esa lista es tu trabajo. Reescribe a mano cada línea marcada, conservando el
sentido, y vuelve a correr `detect.py`. Esta es la parte que sube el puntaje de
REVIEW a PASS, y es la parte que un script no puede hacer.

## Las cinco revisiones

`detect.py` califica cinco señales de 0 a 100; más alto es más humano:

| revisión | qué mide | cómo se ve la máquina |
| --- | --- | --- |
| BURSTINESS | variación del largo de las oraciones | todas las oraciones del mismo largo |
| SPECIFICITY | números, nombres y datos concretos por cada 100 palabras | sustantivos abstractos, sin cifras |
| SLOP DENSITY | coincidencias del léxico por cada 100 palabras | vocabulario de relleno |
| FINGERPRINT | caracteres invisibles, rayas largas y comillas curvas por cada 1,000 caracteres | tipografía perfecta |
| VOICE | contracciones, persona gramatical, estructuras delatoras | sin contracciones, revelaciones montadas |

El veredicto pesa el promedio al 60% y la **revisión más débil** al 40%, porque
basta una señal. PASS necesita 70 o más en total y ninguna revisión debajo de
55.

## Dilo con honestidad

Son cinco heurísticas locales basadas en las señales que usan los detectores
públicos. Corren completas en la máquina del usuario y no se sube nada. **No**
son GPTZero, Originality, Copyleaks, Winston ni Turnitin, no llaman a esas
API y no pueden prometer sus veredictos. Arreglar lo que miden sí suele mover
esos números, porque miden las mismas cosas de fondo. Eso es lo que se afirma.
No afirmes algo más grande por el usuario, y no le digas a nadie que su texto
es indetectable.

## Orden de los pasos

1. `humanize.py draft.txt -o clean.txt --report`
2. Lee las estructuras marcadas. Reescribe tú esas líneas.
3. `detect.py draft.txt clean.txt` para mostrar el antes y el después.
4. Si el veredicto no es PASS, arregla la revisión más débil que nombra la
   salida y vuelve a pasar. Dos rondas es normal. Cinco significa que el
   borrador se escribió con fórmula, y la solución es otro borrador, no más
   pasadas.
5. Muéstrale al usuario el texto limpio y el puntaje. Nunca el puntaje solo.
