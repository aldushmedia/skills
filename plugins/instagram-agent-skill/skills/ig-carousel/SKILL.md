---
name: ig-carousel
description: >-
  Arma un carrusel de Instagram: la portada que se gana el deslizar, el texto
  lámina por lámina y los archivos de 1080x1350 para subir. Úsala cuando el
  usuario diga "carrusel", "láminas", "slides", "post para deslizar", "haz un
  carrusel con esto", o tenga una idea en forma de lista o de pasos que se
  moriría como una sola imagen.
---

# ig-carousel

Los carruseles son el formato de la cuadrícula donde la gente se queda más
tiempo, porque deslizar es una interacción y hacer scroll no. También tienen
una segunda oportunidad: Instagram puede volver a mostrar un carrusel desde
una lámina posterior a alguien que no interactuó la primera vez, así que la
lámina dos también tiene que sostenerse sola.

El formato premia una idea partida en pasos. Castiga un caption cortado en
pedazos.

## Cuándo usarlo en lugar de un Reel

Usa un carrusel cuando la idea tiene **secuencia y hay que releerla**: pasos,
un marco con partes, un antes y después, una lista que vale una captura. Usa
un Reel cuando la idea tiene movimiento, una cara o una recompensa que hay que
ver suceder.

Si la idea es una sola afirmación, no es ninguno de los dos. Pásasela a
`/ig-reel` y dilo.

## Estructura

De 6 a 10 láminas. El máximo es 20, y 20 casi siempre es un libro que nadie
termina. Con menos de 5 el deslizar nunca arranca.

```
1         PORTADA   el gancho. 6 palabras o menos, de un tamaño que se lea en
                    la miniatura de la cuadrícula. Una línea de promesa debajo.
2         LO QUE    por qué importa, en una oración. Esta lámina también es una
          ESTÁ EN   segunda portada, así que no puede ser preámbulo.
          JUEGO
3 a N     UNA IDEA POR LÁMINA. Un título de 3 a 7 palabras, máximo 25
                    palabras debajo. Si una lámina necesita un párrafo, son dos
                    láminas.
N+1       RESUMEN   todo junto como lista. Esta es la lámina de la captura.
ÚLTIMA    CTA       una acción. Guardar, comentar una palabra clave o seguir.
                    Una.
```

## Reglas del texto de las láminas

- **La portada es el 80% del resultado.** Seis palabras. Grandes. Nada del
  resto salva una portada que nadie desliza.
- **Diseña para el recorte de la cuadrícula.** La cuadrícula del perfil recorta
  a un rectángulo vertical más alto que ancho, y la proporción exacta ya
  cambió más de una vez. Arma a 1080x1350 y deja el texto de la portada bien
  al centro, lejos de los 120 píxeles de cada borde, y el recorte deja de
  importar.
- **Numera las láminas** (3/8). La gente termina más cuando ve el final.
- **Ninguna lámina es un párrafo.** Si no se puede decir en 25 palabras,
  pártela.
- **La lámina de resumen es la que la gente captura y manda.** Los envíos son
  la señal más fuerte que te puedes ganar. Hazla independiente y que se lea
  sin contexto.
- **Tu usuario en cada lámina**, chico, en una esquina de abajo. Las capturas
  viajan sin ti.
- **Texto alternativo al menos en la portada.** Lo leen los lectores de
  pantalla y lo lee Instagram.

## Armar los archivos

Instagram pide 1080x1350 (4:5), JPEG o PNG, hasta 20 elementos. Ármalo como
HTML e imprime cada lámina:

```bash
# una <section> por lámina, 1080x1350, page-break-after: always
# luego Chrome headless --print-to-pdf, o la conversión de HTML a imagen que ya uses
```

Escribe el HTML con `width:1080px; height:1350px`, un solo color de acento y
letra de no menos de 32px, porque se lee en un celular a un tercio de su
tamaño real. Si el proyecto tiene una skill de marca o un sistema de diseño,
úsalo y no inventes una paleta.

## Salida

Primero el texto lámina por lámina, como una lista numerada que el usuario
pueda leer en diez segundos y editar antes de que se renderice nada. Luego el
**caption**, que para un carrusel es el Trabajo B de `/ig-caption`: aquí el
caption sí trabaja, porque la portada ya usó sus seis palabras.

Pasa los dos por `/ig-human`. Arma los archivos solo cuando el usuario apruebe
el texto.

```
CARRUSEL  ·  8 láminas

1  PORTADA  LA CLÁUSULA DE $18,000
            Una línea que ahora pongo en cada contrato.
2  EN JUEGO Aprobé el trabajo. Nueve días después me pidieron el dinero de vuelta.
3           QUÉ DICE
            Pago contra entrega, no contra aprobación.
...
7  RESUMEN  Las cuatro líneas, en orden.
8  CTA      Comenta CONTRATO y te mando la cláusula completa.

Caption: Trabajo B, gancho en la línea 1, una petición, 3 hashtags.
```

No se sube nada. El usuario lo publica.
