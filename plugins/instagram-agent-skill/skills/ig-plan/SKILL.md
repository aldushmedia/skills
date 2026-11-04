---
name: ig-plan
description: >-
  Arma la semana en Instagram: qué publicar, en qué formato, cuándo y con
  quién interactuar. Úsala cuando el usuario diga "planea mi semana", "qué
  publico", "calendario de contenido", "no tengo nada que publicar", o quiera
  un horario de publicación y una lista de cuentas con las que interactuar.
---

# ig-plan

La sala de control. Todo lo demás de este paquete ejecuta; esta decide qué se
ejecuta. Córrela una vez a la semana, el mismo día.

## Lo que necesitas

Si existen `~/.claude/instagram/voice.md`, `swipe.md` y `log.md`, léelos. El
swipe file es la evidencia del propio usuario, sacada con `/ig-viral`, de qué
fórmulas están pegando en su nicho ahora mismo, y pesa más que cualquier cosa
de este archivo. El log evita que el plan repita un tema de las últimas dos
semanas.

Si no existen, pide cuatro cosas y anótalas:

1. Qué vende el usuario y a quién.
2. Los tres o cuatro temas por los que quiere que lo conozcan.
3. Qué pasó de verdad esta semana: una llamada con un cliente, un número, un
   error, algo que construyó, una discusión que tuvo. De ahí salen las
   publicaciones.
4. Diez cuentas en las que vale la pena que lo vean.

## Qué publicar

De cuatro a cinco publicaciones por semana, y al menos tres de ellas Reels.
Los Reels son el único formato de Instagram que llega de forma confiable a
gente que no sigue la cuenta. Los carruseles profundizan con la gente que ya
la sigue. Las historias son diarias y se planean aparte.

Mezcla durante la semana, nunca dos del mismo tipo seguidas:

| tipo | cuántas | trabajo |
| --- | --- | --- |
| **Prueba** | 1 por semana | algo que pasó, con un número. Reel. |
| **Enseñar** | 1 a 2 por semana | una cosa que quien mira puede hacer hoy. Reel o carrusel. |
| **Opinión** | 1 por semana | una postura que te podría costar seguidores. Reel. |
| **Historia** | 1 cada dos semanas | una escena con un costo. Reel. |
| **Oferta** | 1 cada dos semanas | lo que vendes, dicho sin rodeos y sin disculparte. Carrusel o historias. |

Para cada lugar da: el tema, el ángulo concreto sacado de lo que pasó esta
semana, el formato y el número de fórmula de gancho de `ig-reel/hooks.json`. No
un tema, un ángulo. "IA" no es un plan. "La propuesta que perdimos porque el
borrador tenía una raya larga" es un Reel.

## Cuándo publicar

Publica cuando la audiencia del usuario está despierta y no está trabajando.
Para la mayoría de las audiencias de consumo eso es temprano en la noche, hora
local; para una audiencia de negocios, temprano en la mañana.

Pero dilo claro: **la hora importa mucho menos que los primeros dos
segundos.** Instagram sigue mostrando un Reel durante días si funciona, y
entierra uno bien programado que no funciona. Si el usuario está optimizando
horarios antes de que sus ganchos funcionen, está puliendo lo que no es, y se
lo tienes que decir.

Usa la zona horaria de la audiencia, no la del usuario, si son distintas. Con
audiencia en varios países de Latinoamérica, elige la del país donde está la
mayoría y dilo.

## La ronda de interacción, que no es opcional

20 minutos al día, antes de publicar, no después. Arma una lista de 10:

- **5 de alcance:** cuentas con una audiencia que el usuario quiere, donde un
  buen comentario se ve. Comenta temprano, antes de que haya 200 comentarios.
- **3 pares:** mismo tamaño, mismo campo. Es el grupo que devuelve la
  interacción.
- **2 compradores:** gente que de verdad podría comprar. Comenta durante
  semanas antes de cualquier DM, y nunca vendas en un comentario.

Pásale la lista a `/ig-comment`.

## Salida

```
SEMANA DEL 15 DE SEPTIEMBRE

LUN  solo interacción  (20 min, lista abajo)
MAR  7:30pm  REEL      PRUEBA    #5  El tiempo comprimido   - propuesta de 5 h a 20 min
MIÉ  solo historias + interacción
JUE  7:00pm  CARRUSEL  ENSEÑAR   caption Trabajo B          - la cláusula explicada en 4 láminas
VIE  7:30pm  REEL      OPINIÓN   #2  La orden negativa      - deja de hacer llamadas de diagnóstico
SÁB  -
DOM  6:00pm  REEL      HISTORIA  #21 A media frase          - el correo del reembolso

HISTORIAS  todos los días, de 3 a 5 cuadros, caja de preguntas el jueves.

INTERACCIÓN  (5 de alcance / 3 pares / 2 compradores)
  ...

Di "escribe el martes" y lo redacto.
```

Escribe el plan en `~/.claude/instagram/plan.md` para que las otras skills lo
puedan leer. No se programa ni se publica nada en ningún lado. Esto es un plan
y lo ejecuta el usuario.
