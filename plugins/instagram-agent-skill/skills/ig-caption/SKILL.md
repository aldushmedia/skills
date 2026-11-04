---
name: ig-caption
description: >-
  Escribe el caption de Instagram (la línea que sobrevive al corte de "... más",
  el cuerpo, la única petición, los términos de búsqueda y los tres hashtags)
  y revísalo antes de que salga. Úsala cuando el usuario diga "escribe el
  caption", "ponle caption a esto", "qué pongo en la descripción", tenga un
  reel o un carrusel listo y le falte el texto, o pregunte por hashtags.
---

# ig-caption

En esta carpeta hay una herramienta y funciona:

```bash
python3 caption.py caption.txt
python3 caption.py caption.txt --keywords "client proposals,agency pricing"
```

Imprime el caption como lo muestra el feed: los primeros 125 caracteres en una
caja y todo lo demás detrás del toque. Lee esa caja antes que cualquier otra
cosa que hayas escrito.

**Con captions en español:** el script cuenta caracteres, hashtags, links y
emojis igual en cualquier idioma. Lo que solo reconoce en inglés es la
petición (`comment`, `save this`, `link in bio`...), así que con un caption en
español la revisión ONE ASK puede decir que no hay petición aunque sí la haya.
Cuenta tú las peticiones a mano y dilo en el resumen. En `--keywords` pon los
términos en español tal como la gente los busca:
`--keywords "propuestas para clientes,precios de agencia"`.

## Primero, decide qué trabajo tiene este caption

Esta es la decisión que arruina captions cuando te la saltas.

**Trabajo A: el video ya los enganchó.** Un Reel trae su propio gancho en los
primeros dos segundos, hablado y en pantalla. El caption no es un segundo
gancho, y competir con el video es la forma de perder los dos. Su trabajo es
la petición, el contexto que hace que la petición tenga sentido y las palabras
que la gente busca.

**Trabajo B: el caption es el contenido.** Una foto, una sola imagen, la
portada de un carrusel que abre una intriga. Aquí la primera línea es el
gancho y funciona igual que el de un Reel: concreto, corto y cortado en un
punto de suspenso, no a media frase.

Pregunta cuál vas a escribir. Si el usuario tiene un Reel con un gancho fuerte,
escribe el A y di por qué.

## La forma

```
Línea 1     125 caracteres visibles. Trabajo A: la petición, sin rodeos.
            Trabajo B: el gancho.
            Nunca un saludo, nunca un hashtag, nunca un emoji como primer
            carácter.
Cuerpo      párrafos cortos, con una línea en blanco entre cada uno. De dos a
            seis. Aquí van los términos de búsqueda.
Petición    una. Comenta una palabra clave, guárdalo o mándame DM. Una.
Hashtags    hasta cinco, en su propia línea al final, o ninguno.
```

El límite es de 2,200 caracteres y casi nada necesita 2,200. Un caption que se
gana el toque y luego entrega 600 caracteres le gana a uno que entrega 1,800.

## Hashtags, con honestidad

Los hashtags ya no son una palanca de alcance, y la plataforma ya lo dijo con
un cambio de producto. **Instagram limitó los hashtags a cinco por publicación
el 18 de diciembre de 2025**, antes eran treinta, y les dijo a los creadores
que "usar menos hashtags (hasta 5) y más específicos, en lugar de muchos
genéricos" funciona mejor. Adam Mosseri ya había dicho en febrero de 2025 que
los hashtags no sirven para aumentar el alcance y que son una etiqueta, no una
palanca de distribución.

Así que: hasta cinco, específicos, como etiquetas de tema. Si el usuario tiene
un bloque de veinte guardado en sus notas, ese bloque ya es peso muerto y la
revisión lo va a reprobar.

`#viral`, `#fyp`, `#explorepage`, `#foryou` no describen nada. Quítalos.

## Ahora los términos de búsqueda importan más que los hashtags

El buscador de Instagram lee el texto del caption. Así que la frase por la que
el usuario quiere que lo encuentren va en el caption como frase que una
persona escribiría, en una oración que se lea normal. "Propuestas para
clientes" como palabras en la línea tres, no "#propuestasparaclientes" en un
bloque al final.

Pide dos o tres de esos términos y pásaselos a la revisión:

```bash
python3 caption.py draft.txt --keywords "client proposals,agency pricing"
```

## Reglas

- **Nada de links en el caption.** Los captions no son clicables. Una URL en el
  cuerpo es texto muerto que dice "no uso esta plataforma". Bio o DM.
- **Una petición.** Dos peticiones es lo mismo que ninguna. `caption.py` las
  cuenta (las que están en inglés).
- **La petición con palabra clave necesita una palabra que se pueda escribir.**
  Una palabra, sin espacios, sin emoji, y dila en voz alta en el video también.
  `Comenta CONTRATO` funciona. `Comenta "la guía del contrato"` no.
- **Escribe aparte el primer comentario** si hay un link. Dilo en el resumen.
- **Emoji como puntuación, no como decoración.** La revisión marca más de 4 por
  cada 100 caracteres.
- **El texto alternativo vale 20 segundos.** En carruseles y fotos, escríbelo.
  Lo leen los lectores de pantalla y lo lee Instagram.

## El ciclo

1. Decide Trabajo A o Trabajo B y di cuál.
2. Escribe el borrador.
3. Pásalo por `/ig-human`. Los captions son cortos, así que el relleno se nota
   más aquí que en cualquier otra parte del paquete.
4. Corre `caption.py` con los términos de búsqueda del usuario. Arregla cada
   FAIL. Decide cada WARN en voz alta, no en silencio.
5. Imprime el bloque listo para copiar y luego el resumen:

```
CAPTION LISTO
trabajo:     A, el reel lleva el gancho
visible:     118 de 125 caracteres usados antes del corte
petición:    una, comenta CONTRATO
hashtags:    3
búsqueda:    "propuestas para clientes" en la línea 3, "precios de agencia" en la 5
revisión:    READY
```

No se publica nada. El usuario lo pega.
