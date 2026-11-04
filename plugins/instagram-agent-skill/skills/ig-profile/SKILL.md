---
name: ig-profile
description: >-
  Califica un perfil de Instagram sobre 100 con una rúbrica de 12 partes y
  reescribe lo que pierde puntos: campo del nombre, bio, link, historias
  destacadas, las tres fijadas y la cuadrícula. Úsala cuando el usuario diga
  "optimiza mi perfil", "arregla mi bio", "califica mi Instagram", "por qué no
  me siguen", o pegue su perfil y pregunte cómo se lee.
---

# ig-profile

Casi todo el mundo optimiza lo que no es. El perfil no es una tienda que la
gente recorre. Es una **pantalla de decisión** a la que se llega desde un reel,
y tiene unos tres segundos para contestar una pregunta: ¿hay más de eso aquí,
y es para mí?

## Lo que necesitas

Pídele al usuario que pegue o mande captura de: el campo del nombre, el
usuario, la bio, a dónde lleva el link, los nombres de las historias
destacadas, qué está fijado y las primeras nueve portadas de la cuadrícula.
Una captura de la parte de arriba del perfil más las dos primeras filas de la
cuadrícula alcanza para una primera revisión.

No inicies sesión en Instagram por el usuario.

## Califícalo

Lee `rubric.json` en esta carpeta. Doce puntos, 100 en total, cada uno con cómo
se ve la calificación completa y cómo suele fallar. Califica cada punto,
muestra la tabla y da el total. Sé honesto. Casi todos los perfiles quedan
entre 30 y 49 en la primera revisión, y una calificación generosa no sirve.

```
CALIFICACIÓN DEL PERFIL  38/100

  campo del nombre      2/12   solo el nombre, ninguna palabra que alguien busque
  primera línea de bio  3/12   tres sustantivos y un emoji de café
  las tres fijadas      0/10   nada fijado
  destacadas            2/8    "Random", "Vida", "2023"
  cuadrícula legible    4/8    seis de nueve portadas son una cara a media frase
  ...
```

## Luego reescribe, en este orden

Arregla de más a menos puntos perdidos. No reescribas todo de golpe: el usuario
tiene que ir a cambiar cada una de estas cosas.

**1. El campo del nombre (30 caracteres).** La línea en negritas debajo de la
foto, no el usuario. Es el campo que compara el buscador de Instagram, y casi
todas las cuentas ponen ahí un nombre y nada más. Formato que funciona:
`{Nombre} | {lo que haces, con las palabras que se buscan}`. Por ejemplo,
`Ana Torres | Fotos de producto`. Da tres opciones.

**2. Primera línea de la bio.** Para quién es y qué cambia. No un puesto, no
adjetivos, no una lista de identidades separada con barras. El resto de los
150 caracteres lleva una prueba o una oferta clara.

**3. Las tres fijadas.** Tres lugares, tres trabajos distintos: la mejor
prueba, la explicación más clara de la oferta y la mejor presentación de la
persona. Es el arreglo con más impacto de todo el perfil y toma cuatro toques.
Una cuadrícula sin fijadas muestra lo último que se publicó, que es como lanzar una moneda.

**4. Historias destacadas.** De cuatro a seis, con los nombres de las preguntas
que hace un comprador: Precios, Resultados, Cómo funciona, Sobre mí. No
"Random". Borra las demás.

**5. El link.** Un solo destino que coincida con lo que la bio acaba de
prometer. Se permiten cinco; dos ya es un menú, y un menú convierte peor que
una puerta.

**6. Portadas de la cuadrícula.** Las primeras nueve, en miniatura. Las
portadas de los reels se eligen, no se dejan en el primer cuadro que haya
salido. Cuatro palabras de texto en una portada hacen que la cuadrícula se lea
de un vistazo.

## Salida

La tabla de calificación y luego las reescrituras como bloques listos para
copiar, de lo más urgente a lo menos, cada una pasada por `/ig-human`. Vuelve a
calificar al final y muestra la diferencia con honestidad. Si la reescritura
llega a 84 y no a 98, di 84, y di qué falta, que casi siempre es la
cuadrícula, el hábito de subir historias y una publicación fijada que todavía
no existe. Nada de eso es una reescritura.

Esta skill no guarda nada en Instagram. El usuario edita cada campo.
