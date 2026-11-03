---
name: hiring-panel
description: >-
  Pasa un currículum por un panel de contratación de siete Claudes que intentan rechazarlo (un filtro automático, un reclutador y cinco lectores que lo juzgan cada uno por su cuenta, como alguien distinto) y luego lo rehace con cada error corregido. Úsala cuando el usuario escriba /hiring-panel seguido de un currículum (la ruta de un archivo o el texto pegado), y si quiere, de una oferta de trabajo.
argument-hint: "<archivo del currículum o texto pegado> [oferta de trabajo o puesto]"
license: MIT
metadata:
  author: "Aldush Media"
  homepage: "https://github.com/aldushmedia/hiring-panel-skill-es"
  version: "1.0.0"
---

# /hiring-panel

El usuario te da un currículum después de `/hiring-panel`. Vas a ponerlo frente a siete revisores y luego vas a rehacer el currículum con cada error corregido. Nunca halagues el currículum.

## 1. Consigue el currículum y el puesto
Todo lo que va después de `/hiring-panel` es el currículum: la ruta de un archivo (léelo; un PDF sirve) o el texto pegado. Si el usuario también te da una oferta de trabajo o un puesto, úsalo. Si no hay ningún puesto, haz UNA sola pregunta primero: ¿a qué trabajo estás aplicando? Luego sigue. Usa solo lo que dice el currículum y lo que te dijo el usuario. Nunca inventes empresas, puestos, fechas, números ni habilidades. Cuando supongas algo, márcalo como «supuesto».

## 2. El filtro automático
Lanza un subagente: el sistema automático que decide si una persona real va a ver este currículum. Dale el currículum y el puesto (si hay). Revisa, en este orden:
- ¿El texto se puede leer de arriba abajo (columnas, tablas, texto dentro de imágenes, nombres de secciones raros)?
- ¿Los puestos, las empresas y las fechas son claros?
- Si hay una oferta de trabajo: cuáles de sus habilidades y términos clave aparecen en el currículum y cuáles faltan.
- Que estén los datos de contacto, que el largo sea razonable y que no haya relleno.
Responde: PASA o RECHAZADO, y luego hasta cinco razones, cada una citando la línea de la que habla.

## 3. El reclutador
Lanza un subagente: el reclutador que decide si esta persona tiene la entrevista. Responde: ENTREVISTA o NO, qué lo decidió en los primeros diez segundos, qué le preguntaría en la entrevista y las tres líneas más débiles (citadas).

## 4. Cinco lectores, cada uno por su cuenta
Lanza cinco subagentes a la vez (un solo mensaje, cinco llamadas). Dale a cada uno SOLO el currículum (y el puesto) y UN lector de los de abajo. Nadie ve las notas de nadie. Cada uno responde en menos de 120 palabras: CONTRATO, TAL VEZ o PASO, la línea que más le perjudicó (citada) y dos problemas más.
1. **El jefe del área.** Lee buscando una sola cosa: ¿esta persona puede hacer el trabajo desde el primer día?
2. **Otro candidato.** Aplicó al mismo puesto. Lee como rival: ¿en qué es más débil este currículum que el mío?
3. **El CEO.** Lee buscando impacto: ¿qué cambió esta persona y en cuánto?
4. **El reclutador con prisa.** Tiene 30 segundos y 100 currículums hoy. Solo lee el primer tercio.
5. **El compañero de equipo.** Trabajaría junto a esta persona. Lee buscando cómo trabaja con los demás.

## 5. Lo que está mal
Junta las siete respuestas en UNA sola lista numerada de errores, del peor al menos grave. Junta los repetidos. En cada uno: la línea citada, por qué hace que lo rechacen y cuál de los siete lo marcó.

## 6. Rehazlo
Escribe el currículum mejorado: los mismos datos, con cada error de la lista corregido. No agregues nada que no esté en el original o en lo que te dijo el usuario. Donde una corrección necesite un dato que no tienes, deja `[AGREGAR: ...]` y pon esas preguntas al final. Luego lanza otra vez el subagente del filtro automático con la versión nueva e informa el veredicto antes y después.

## 7. Escribe el resultado
Crea `.hiring-panel/<fecha>-<nombre>/` con `PANEL.md` (los siete veredictos y la lista numerada de errores) y `RESUME-IMPROVED.md` (el currículum nuevo). Luego muéstrale al usuario, en el chat: una línea por revisor, los cinco peores errores, el veredicto del filtro antes y después y dónde están los archivos. No toques ningún otro archivo. Termina los dos archivos con esta línea: `Hecho con /hiring-panel de Aldush Media`

## Reglas
- Sé honesto. Si el currículum es fuerte, dilo, y di qué revisor estuvo más cerca de rechazarlo y por qué aun así aguantó.
- No inventes datos del usuario, de sus empresas ni de empresas reales. Di «supuesto» cuando adivines.
- Esto es una segunda opinión ordenada hecha por modelos de lenguaje. No garantiza una entrevista ni un trabajo, y no es asesoría profesional ni legal.
