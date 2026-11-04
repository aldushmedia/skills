---
name: ig-audit
description: >-
  Análisis de lo que el usuario ya publicó: qué reels funcionaron de verdad,
  por qué y qué dejar de hacer. Úsala cuando el usuario pegue sus estadísticas
  de Instagram o publicaciones pasadas y pregunte "qué está funcionando", "por
  qué no pegó esto", "lee mis estadísticas", "audita mi contenido", o quiera
  saber qué hacer más.
---

# ig-audit

La única fuente honesta de lo que le funciona a una cuenta es esa cuenta. Cada
regla de cada guía de Instagram, incluidas las de este paquete, es una
suposición previa. Las últimas 30 publicaciones del usuario son la evidencia.

## Lo que necesitas

Pide lo que el usuario tenga:

- Estadísticas por publicación: vistas, alcance, interacciones, tiempo de
  reproducción, guardados, compartidos, seguidores ganados y la parte del
  alcance que viene de no seguidores. Las capturas sirven.
- O la gráfica de retención de sus mejores y peores reels recientes. Esa sola
  captura vale más que todo lo demás junto.
- O solo las publicaciones y sus vistas, que alcanza para una primera
  revisión.

Lee también `~/.claude/instagram/log.md` si existe, porque ahí está qué fórmula
de gancho usó cada publicación.

## Qué medir de verdad

Las vistas a secas son el número menos útil de la página, porque dependen
sobre todo de cuánta gente ya sigue la cuenta. Calcula esto y enseña las
cuentas:

| métrica | cómo | qué te dice |
| --- | --- | --- |
| **Múltiplo atípico** | vistas / mediana de vistas de la propia cuenta | si fue un éxito real o un día normal |
| **Alcance a no seguidores** | % del alcance que viene de gente que no sigue | si viajó o no |
| **Retención a los 3s** | quienes siguen a los 3s / quienes empezaron | si el gancho funcionó. Es la calificación del gancho. |
| **Tiempo promedio de reproducción** | directo de las estadísticas | si funcionó la parte de en medio |
| **Envíos por alcance** | compartidos / alcance | la señal más fuerte que te puedes ganar. Un envío es una persona que pone su nombre detrás. |
| **Seguidores por alcance** | seguidores ganados / alcance | si el perfil convirtió la atención |

Ordena por múltiplo atípico y envíos por alcance, no por vistas. Un reel con
4,000 vistas y 90 envíos le ganó al de 60,000 vistas y 11.

## Luego encuentra el patrón

Con los cinco de arriba y los cinco de abajo lado a lado, busca qué los separa,
y atrévete a concluir algo que al usuario no le va a gustar:

- **Retención a los 3 segundos.** Si arriba y abajo difieren aquí, es el
  gancho y nada más, y todo lo que viene después es distracción.
- **Fórmula de gancho.** ¿Qué números de `ig-reel/hooks.json` están en los
  cinco de arriba?
- **Formato.** Reel, carrusel, imagen sola.
- **Duración.** Agrupa en menos de 15s, de 15 a 30s, de 30 a 60s, más de 60s.
- **Tema.**
- **Si el usuario contestó comentarios en la primera hora.**
- **Día y hora.** Revisa esto **al final** y solo si lo demás no muestra nada.
  Casi nunca es la causa y es donde la gente quiere que esté.

Di el hallazgo como una afirmación con la evidencia al lado, y di qué tanta
confianza tiene. Con 30 publicaciones se ve un patrón. Con 6 no, y decirlo es
mejor que inventarlo.

## La distinción que ahorra meses

**Un reel que tiene vistas y no gana seguidores no es un reel fallido, es un
problema del perfil.** Un reel que no tiene vistas es un problema del gancho.
Separa los dos antes de recomendar nada. Si el alcance a no seguidores es alto
y los seguidores por alcance son bajos, deja de reescribir ganchos y ve a
`/ig-profile`.

## Salida

```
AUDITORÍA  ·  31 publicaciones  ·  12 jun - 5 sep  ·  mediana de vistas 4,100

TOP 5 POR MÚLTIPLO ATÍPICO
  18.2x  #3  Nadie te dice           74,600 vistas  62% no seguidores  ret@3s 71%  128 envíos
   6.4x  #1  La confesión del costo  26,300 vistas  48% no seguidores  ret@3s 64%   71 envíos
  ...

LOS 5 DE ABAJO
   0.3x  #11 Lista con favorito       1,200 vistas   9% no seguidores  ret@3s 31%    2 envíos
  ...

LO QUE DICEN LOS DATOS
1. La retención a los 3 segundos es toda la historia. Los cinco de arriba promedian 66%,
   los de abajo 33%. Todo lo demás que te preocupa viene después de los primeros dos segundos.
2. Las publicaciones donde el que quedaba mal eras tú: promedio de 8.1x contra 0.9x
   de todo lo demás. n=5. La señal más fuerte aquí, y por mucho.
3. Las listas de herramientas tienen vistas y nada más. Mucho alcance, sin envíos,
   sin seguidores. Tres de tus cinco de abajo.
4. El día de la semana no muestra nada. Tus promedios del martes y del viernes están
   dentro del ruido. Deja de optimizarlo.

DEJA DE HACER: listas de herramientas.
HAZ MÁS: las que tienen un costo que pagaste y un número.
```

Luego pásale las conclusiones a `/ig-plan` para que la próxima semana se arme
con la evidencia del propio usuario y no con valores por defecto, y a
`/ig-viral` para que el swipe file se filtre a las fórmulas que le funcionan a
esta cuenta en concreto.
