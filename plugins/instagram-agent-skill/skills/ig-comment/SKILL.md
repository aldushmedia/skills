---
name: ig-comment
description: >-
  Escribe comentarios en publicaciones y reels de otras personas en Instagram
  que se lean como una persona con opinión, no como un bot. Úsala cuando el
  usuario pegue una publicación o un reel y quiera un comentario, diga
  "comenta esto", "interactúa con esto", "qué le pongo aquí", o quiera un
  lote para su ronda diaria de interacción.
---

# ig-comment

Comentar son los veinte minutos con más impacto en Instagram y los más fáciles
de hacer mal. Un comentario cerca de arriba en un reel con 40,000 vistas lo ve
más gente que la mayoría de las publicaciones de muchas cuentas, y es el único
lugar donde un desconocido puede tocar y llegar directo a un perfil.

Un comentario genérico es peor que ninguno. Cuesta un toque que no lleva a
ningún lado y marca la cuenta como de grupo de interacción ante la única
persona cuya opinión importaba, que es el creador.

## Lo que necesitas

El usuario pega el texto de la publicación o del reel, o una captura, con el
nombre de la cuenta. Si da una URL que no puedes abrir, pídele que la pegue.
No uses un navegador para hacer scraping del feed y no publiques nada.

## Los nueve tipos de comentario

Elige según lo que de verdad es la publicación. Nunca te quedes por defecto en
el tipo 1.

| # | tipo | cuándo | forma |
| --- | --- | --- | --- |
| 1 | **Suma un dato** | la publicación afirma algo que puedes respaldar con un número | "Igual con nosotros: el 40% de..." |
| 2 | **Suma el caso que falta** | la publicación tiene razón pero está incompleta | "Esto se cumple hasta que {condición}." |
| 3 | **Desacuerdo con respeto** | de verdad crees que está mal | primero di en qué estás de acuerdo, luego dónde te separas |
| 4 | **Extiende una línea** | hay una línea que es la buena | cítala y construye sobre ella |
| 5 | **Haz la pregunta de verdad** | la publicación se saltó la parte difícil | una pregunta, concreta |
| 6 | **El comprobante** | ya hiciste lo que describen | qué pasó, en dos oraciones |
| 7 | **La corrección** | hay un error de hecho | ten razón, sé breve, sé amable, ten certeza |
| 8 | **El otro ángulo** | los hechos están bien, el marco no | "Otra forma de verlo:" |
| 9 | **La frase corta** | la publicación no necesita nada y quieres estar presente | menos de 10 palabras, tiene que ser graciosa o cierta |

## Reglas

- **De una a tres oraciones.** Los comentarios de Instagram se leen en una
  columna angosta debajo de un video. Un párrafo se esconde detrás de "más" y
  nadie lo toca.
- **Nunca empieces con** "Gran post", "Me encanta", "Muy cierto", "Esto 👏",
  "Lo necesitaba hoy", o el nombre del creador con signos de admiración. Todos
  son invisibles.
- **Nada de comentarios de puro emoji** ni un emoji como primer carácter.
- **Nunca repitas el reel.** Todos los que están viendo acaban de verlo.
- **Una idea.** Un comentario con dos puntos se lee como secuestro de la
  conversación.
- **Di lo concreto.** Si el comentario podría ir debajo de cualquier
  publicación del tema, no es un comentario, es ruido.
- **Nunca vendas, jamás.** Ni la oferta, ni el link, ni "pásate por mi
  perfil". Es la forma más rápida de que te bloquee justo la persona a la que
  querías llegar.
- **Aquí llegar temprano importa más que en cualquier otro lado.** Un
  comentario en la primera hora de un reel que luego despega viaja con él.

## Salida

Da **dos opciones de tipos distintos**, con su etiqueta, más una línea sobre
cuál publicarías y por qué. Pasa las dos por `/ig-human` primero: los
comentarios son cortos, así que una raya larga o una frase hecha pesa más que
en un caption.

```
OPCIONES DE COMENTARIO  (en el reel de @cuenta sobre precios)

[6 · Comprobante]
Subimos nuestros precios 40% en marzo pasado y perdimos exactamente un
cliente, el que ocupaba la mitad del inbox. Tardé ocho meses en dejar de
tenerle miedo.

[3 · Desacuerdo con respeto]
De acuerdo con lo del ancla. Donde no estoy de acuerdo es en hacerlo a mitad
del proyecto. Lo intentamos y nos costó una renovación que iba bien.

Publica el primero. Concede algo y trae un número.
```

## Modo lote

Para una ronda de interacción, pide las 5 a 10 publicaciones como texto pegado
en un solo mensaje, devuelve un comentario para cada una en un solo bloque y
lleva una nota en `~/.claude/instagram/log.md` de a quién comentaste esta
semana. Comentar en las mismas tres cuentas todos los días se nota, y parece
exactamente lo que es.

## Nunca

No publiques en automático, no automatices comentarios y no uses un navegador
para publicar por el usuario. La interacción automatizada viola las
Condiciones de uso de Instagram y hace que bloqueen acciones de la cuenta.
Esta skill escribe el comentario. El usuario lo publica.
