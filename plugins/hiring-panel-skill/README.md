# La skill del panel de contratación

Aplicas a decenas de trabajos y nunca te enteras de por qué las empresas te dicen que no. Esta skill te lo dice antes:
siete Claudes intentan rechazar tu currículum y luego te lo rehace con cada error corregido. Gratis, MIT, sin registro y
sin API key.

Versión en español de **Aldush Media**.

## El panel

1. **El filtro automático** decide si una persona siquiera va a ver tu currículum: si se puede leer, si los puestos y
   las fechas son claros y qué términos clave del puesto faltan. PASA o RECHAZADO, con las líneas de las que habla.
2. **El reclutador** decide si te dan la entrevista y dice qué lo decidió en los primeros diez segundos.
3. **Cinco lectores, cada uno por su cuenta.** Nadie ve las notas de nadie: el jefe del área (¿puedes hacer el trabajo
   desde el primer día?), otro candidato (¿en qué es más débil tu currículum que el mío?), el CEO (¿qué cambiaste y en
   cuánto?), el reclutador con prisa (30 segundos, solo el primer tercio) y un compañero de equipo (¿cómo trabajas con
   los demás?). CONTRATO, TAL VEZ o PASO cada uno.

Después junta todo en una sola lista de errores, del peor al menos grave, **rehace tu currículum con cada uno corregido**
(los mismos datos, nada inventado) y vuelve a pasar el filtro automático para mostrarte el veredicto antes y después.

Todo se guarda en `.hiring-panel/`, en la carpeta donde lo corras: `PANEL.md` y `RESUME-IMPROVED.md`.

## Instalación

En Claude Code:

```
/plugin marketplace add aldushmedia/skills
/plugin install hiring-panel-skill@aldushmedia
```

O copia `plugins/hiring-panel-skill/skills/hiring-panel` en `~/.claude/skills/`. Después abre una sesión nueva de Claude Code.

## Uso

```
/hiring-panel ~/Documents/curriculum.pdf  Diseñador de producto senior en una startup de finanzas
```

Pega la oferta de trabajo después de tu currículum para que la revisión sea más precisa. Cada uso son ocho llamadas a
subagentes y cuenta para el uso de tu plan de Claude.

## Bueno saber

- Nunca inventa empresas, puestos, fechas ni números. Donde una corrección necesita un dato que no tiene, deja
  `[AGREGAR: ...]` y te lo pregunta.
- Es una segunda opinión ordenada hecha por modelos de lenguaje. No garantiza una entrevista.
- No la hizo Anthropic.

Corre las pruebas con `python3 -m unittest discover -s tests`.
