---
name: ig-repurpose
description: >-
  Convierte una pieza larga (un video de YouTube, un podcast, un en vivo, un
  newsletter, un artículo de blog o una llamada con un cliente) en una semana
  de reels y carruseles. Úsala cuando el usuario diga "reutiliza esto",
  "conviértelo en reels", "tengo un video/podcast/transcripción", "córtalo", o
  pegue algo largo y lo quiera en Instagram.
---

# ig-repurpose

Una buena pieza larga trae de cuatro a seis publicaciones. Casi todos sacan
una y tiran el resto.

## Lo que necesitas

Una transcripción, un artículo, un newsletter, un guion, el resumen de una
llamada, un en vivo. Si el usuario da una URL y esta sesión tiene una
herramienta de transcripción, úsala; si no, pídele que lo pegue. Lee todo
antes de sacar cualquier cosa.

Si la fuente es un video del propio usuario, pide también el archivo. Un Reel
hecho con su propio material le gana a uno hecho con sus palabras leídas otra
vez.

## Extrae, no resumas

El resumen de un video no es un Reel. Nadie quiere el resumen. Recorre la
pieza y saca lo que se sostiene solo:

| sacar | qué es |
| --- | --- |
| **Afirmaciones** | cada oración que empezaría una discusión |
| **Números** | cada cifra, costo, duración, porcentaje |
| **Historias** | cada momento con una persona, una escena y un costo |
| **Mecanismos** | cada "así es como funciona de verdad..." |
| **Errores** | cada vez que admite algo que salió mal |
| **Frases** | cada oración que ya se puede citar tal cual |

Haz la lista de lo que encontraste, con conteos, antes de escribir nada. Si la
pieza da menos de cuatro cosas, es flaca, y cuatro publicaciones sacadas de
ahí también van a ser flacas. Dilo.

## Luego elige el formato de cada extracto

No todo es un Reel.

- **Afirmación, error, historia:** a Reel. Necesitan una voz y una cara.
- **Mecanismo, lista numerada:** a carrusel. Hay que releerlos.
- **Una frase citable:** a un cuadro de historia, no a una publicación.

## Luego arma la semana

Cada extracto se vuelve una publicación y cada publicación se sostiene
completamente sola. Quien mira no vio la fuente y nunca la va a ver. Nunca
escribas "como dije en mi último video". La publicación es la cosa.

Asígnale a cada una una fórmula de gancho de `ig-reel/hooks.json` y varíalas.
Cinco publicaciones de una misma fuente con la misma forma de gancho se leen
como fábrica de contenido, porque lo son.

Si la fuente es un video del propio usuario, **usa el material real**. El clip
donde dijo la cosa, con la reacción real, le gana a volver a grabar, siempre.
Corta en la frase, no en la respiración.

Ordénalas en la semana para que la afirmación más fuerte vaya primero, la
historia caiga a media semana y el mecanismo vaya al final, cuando la gente a
la que le gustaron las primeras está esperándolo.

## Salida

```
FUENTE: "Por qué matamos las llamadas de diagnóstico" (podcast de 42 min, 8,900 palabras)

ENCONTRÉ  5 afirmaciones, 9 números, 3 historias, 4 mecanismos, 2 errores, 7 frases citables

SEMANA
MAR  REEL      #2  La orden negativa     Deja de hacer llamadas de diagnóstico
                                         usa el clip del 14:20, se ríe al final
MIÉ  CARRUSEL  caption Trabajo B         El formulario de 4 preguntas que reemplazó la llamada
VIE  REEL      #21 A media frase         "...y nueve días después pidió un reembolso"
DOM  REEL      #5  El tiempo comprimido  Seis horas a la semana de vuelta, un link borrado

Di "escribe el martes" y lo redacto.
```

Luego redacta cuando te lo pidan, una a la vez, cada una con `/ig-reel` y
`/ig-human`. No sueltes cuatro guiones terminados de golpe. Van a sonar igual y
el usuario no va a grabar ninguno.
