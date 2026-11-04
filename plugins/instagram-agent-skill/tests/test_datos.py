"""Pruebas de los datos de la skill (solo json, re y unittest).

No importan ni ejecutan ningún script de la skill: leen los .json como datos.
"""

import glob
import json
import os
import re
import unittest

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HOOKS = os.path.join(RAIZ, "skills", "ig-reel", "hooks.json")
SLOP = os.path.join(RAIZ, "skills", "ig-human", "slop.json")
RUBRIC = os.path.join(RAIZ, "skills", "ig-profile", "rubric.json")

SKILLS = ["ig-audit", "ig-caption", "ig-carousel", "ig-comment", "ig-dm", "ig-human",
          "ig-plan", "ig-profile", "ig-reel", "ig-reply", "ig-repurpose", "ig-story",
          "ig-viral"]


def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def patron_lexico(find):
    # La misma forma de patrón con la que el humanizador busca cada término.
    return re.compile(r"\b" + re.escape(find).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)


# Ganchos en español de más, uno o varios por fórmula: {id: [ganchos]}.
GANCHOS_ES = {
    1: ["Perdí 40,000 pesos por no leer una sola línea del contrato."],
    2: ["Deja de mandar tu catálogo en PDF por DM."],
    3: ["Nadie te habla de lo que pasa cuando subes tus precios."],
    4: ["Esta plantilla de $0 sustituyó al diseñador que me cobraba $300 por carrusel."],
    5: ["Ahora me toma 10 minutos contestar todos los DMs del día."],
    6: ["Contesté cada comentario durante 30 días. Aquí están mis números."],
    7: ["El error más común al poner precios en Instagram."],
    8: ["Trabajé 8 años en una agencia de publicidad en Bogotá. Esto nunca lo decíamos."],
    9: ["Roba esta plantilla de mensaje para cerrar ventas por DM."],
    10: ["Si vendes por Instagram y nadie te pregunta precios, mira esto."],
    11: ["3 errores que matan tus historias. El número 2 lo comete todo el mundo."],
    12: ["\"Está muy caro.\" Perfecto. Esto es lo que le contesto."],
    13: ["Antes de cambiar la portada tenía 200 vistas, y después 9,000."],
    14: ["Nutriólogas que venden por WhatsApp: esto es para ustedes."],
    15: ["Mis primeras 20 publicaciones no vendieron nada."],
    16: ["¿Cuántos hashtags pongo en un reel?"],
    17: ["Reels vs carruseles: cuál vende más para una tienda en línea."],
    18: ["Déjame mostrarte cómo contesto un DM de precio en 10 segundos."],
    19: ["Haz esto antes de que cambie el algoritmo otra vez."],
    20: ["No te hace falta una cámara cara para vender por Instagram."],
    21: ["Y entonces fue cuando el cliente me dejó en visto."],
    22: ["Más vale tarde que nunca es la peor regla para tu negocio."],
    23: ["El 70 por ciento de mis ventas vienen de las historias."],
    24: ["Este es mi nuevo micrófono y cambió cómo suenan mis reels."],
    25: ["Una alumna que conozco pasó de 0 a 50 ventas en un mes."],
    26: ["La manera más fácil de conseguir clientes es contestar cada comentario."],
}

# Frases de IA en español que se agregaron a slop.json, con su reemplazo.
FRASES_ES = {
    "sumérgete": "entra",
    "sumérgete en": "mira",
    "en el mundo de hoy": "hoy",
    "en el mundo actual": "hoy",
    "en la era digital": "hoy",
    "desbloquea tu potencial": "mejora",
    "desbloquea todo tu potencial": "mejora",
    "potencia tu contenido": "mejora tu contenido",
    "potencia tu marca": "mejora tu marca",
    "lleva tu negocio al siguiente nivel": "haz crecer tu negocio",
    "al siguiente nivel": "más lejos",
    "es importante destacar que": "",
    "cabe destacar que": "",
    "sin lugar a dudas": "",
    "en pocas palabras": "",
    "al final del día": "",
    "un sinfín de": "muchos",
    "es crucial": "importa",
    "es vital": "importa",
    "un arsenal de": "varias",
    "deja de hacer scroll": "",
    "en este video te voy a enseñar": "",
    "en el video de hoy": "",
    "sígueme para más": "",
    "etiqueta a alguien que necesite esto": "",
    "el algoritmo ama": "Instagram empuja",
    "esto lo cambió todo": "esto funcionó",
    "nadie está hablando de esto": "pocos hacen esto",
}

# Estructuras en español que se marcan: {id: texto que la tiene}.
ESTRUCTURAS_ES = {
    "no-es-es": "No es solo una cuenta, es tu tienda.",
    "no-solo-sino": "No solo vendes más, sino también trabajas menos.",
    "no-se-trata": "No se trata de publicar más. Se trata de publicar mejor.",
    "el-resultado": "¿El resultado?",
    "lo-que-aprendi": "Esto es lo que aprendí después de 100 reels.",
    "triada-es": "Es rápido, fácil y barato.",
    "como-ia": "Como IA no tengo opiniones.",
    "en-resumen": "En resumen, publica todos los días.",
    "cebo-interaccion": "Publicar diario funciona. ¿Qué opinas?",
    "deja-scroll": "Deja de hacer scroll y mira esto.",
    "en-este-video": "En este video te voy a enseñar a vender.",
    "cebo-seguir": "Sígueme para más tips de ventas.",
}


class JsonValidoTest(unittest.TestCase):
    def test_cada_json_es_valido(self):
        rutas = glob.glob(os.path.join(RAIZ, "**", "*.json"), recursive=True)
        rutas += glob.glob(os.path.join(RAIZ, ".claude-plugin", "*.json"))
        self.assertGreaterEqual(len(rutas), 4)
        for ruta in rutas:
            with self.subTest(ruta=os.path.relpath(ruta, RAIZ)):
                cargar(ruta)

    def test_plugin(self):
        p = cargar(os.path.join(RAIZ, ".claude-plugin", "plugin.json"))
        self.assertEqual(p["name"], "instagram-agent-skill")
        self.assertEqual(p["author"]["name"], "Aldush Media")
        self.assertEqual(p["homepage"], "https://github.com/aldushmedia/skills")
        self.assertEqual(p["repository"], "https://github.com/aldushmedia/skills")


class SkillsTest(unittest.TestCase):
    def test_trece_skills_con_su_nombre(self):
        for skill in SKILLS:
            with self.subTest(skill=skill):
                with open(os.path.join(RAIZ, "skills", skill, "SKILL.md"), encoding="utf-8") as f:
                    texto = f.read()
                self.assertTrue(texto.startswith("---\nname: " + skill + "\n"))
                self.assertIn("description:", texto.split("---")[1])

    def test_sin_raya_larga_en_textos_y_datos(self):
        rutas = [r for patron in ("**/*.md", "**/*.json")
                 for r in glob.glob(os.path.join(RAIZ, patron), recursive=True)]
        rutas += glob.glob(os.path.join(RAIZ, ".claude-plugin", "*.json"))
        for ruta in rutas:
            with open(ruta, encoding="utf-8") as f:
                self.assertNotIn("\u2014", f.read(), os.path.relpath(ruta, RAIZ))


class GanchosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datos = cargar(HOOKS)
        cls.por_id = {h["id"]: h for h in cls.datos["hooks"]}

    def clasificar(self, gancho):
        for i in self.datos["classify_order"]:
            if re.search(self.por_id[i]["match"], gancho, re.IGNORECASE):
                return i
        return None

    def test_26_formulas_con_sus_campos(self):
        self.assertEqual(sorted(self.por_id), list(range(1, 27)))
        self.assertEqual(sorted(self.datos["classify_order"]), list(range(1, 27)))
        for h in self.datos["hooks"]:
            for campo in ("name", "template", "example", "on_screen", "best_for", "trap", "match"):
                self.assertTrue(h[campo], (h["id"], campo))

    def test_cada_regex_compila(self):
        for h in self.datos["hooks"]:
            with self.subTest(formula=h["id"]):
                re.compile(h["match"], re.IGNORECASE)

    def test_ejemplo_en_espanol_coincide_con_su_formula(self):
        for h in self.datos["hooks"]:
            with self.subTest(formula=h["id"], ejemplo=h["example"]):
                self.assertRegex(h["example"], re.compile(h["match"], re.IGNORECASE))

    def test_ejemplo_en_espanol_se_clasifica_en_su_formula(self):
        for h in self.datos["hooks"]:
            with self.subTest(formula=h["id"]):
                self.assertEqual(self.clasificar(h["example"]), h["id"])

    def test_ganchos_en_espanol_de_mas(self):
        for fid, ganchos in GANCHOS_ES.items():
            for gancho in ganchos:
                with self.subTest(formula=fid, gancho=gancho):
                    self.assertRegex(gancho, re.compile(self.por_id[fid]["match"], re.IGNORECASE))

    def test_los_patrones_en_ingles_siguen_funcionando(self):
        ingles = {
            1: "$18,000 is what one missing clause cost me.",
            3: "Nobody tells you that your first 30 reels are supposed to flop.",
            5: "Proposals used to take me five hours. They take twenty minutes now.",
            9: "Steal this four-line follow-up.",
            15: "My first 47 reels averaged 300 views.",
            18: "Watch what happens when I paste a competitor's caption into this.",
            20: "You do not need a niche.",
            23: "33% of high school graduates never read another book.",
        }
        for fid, gancho in ingles.items():
            with self.subTest(formula=fid):
                self.assertEqual(self.clasificar(gancho), fid)


class LexicoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datos = cargar(SLOP)
        cls.terminos = {e["find"]: e for e in cls.datos["words"] + cls.datos["phrases"]}

    def test_formato_de_cada_entrada(self):
        for e in self.datos["words"] + self.datos["phrases"]:
            self.assertEqual(set(e), {"find", "replace", "family"}, e)
            self.assertTrue(e["find"].strip())
        for s in self.datos["structures"]:
            self.assertEqual(set(s), {"id", "regex", "name", "fix"}, s)

    def test_sin_terminos_repetidos(self):
        vistos = [e["find"].lower() for e in self.datos["words"] + self.datos["phrases"]]
        self.assertEqual(len(vistos), len(set(vistos)))
        ids = [s["id"] for s in self.datos["structures"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_cada_regex_compila(self):
        for s in self.datos["structures"]:
            with self.subTest(estructura=s["id"]):
                re.compile(s["regex"], re.MULTILINE)
        for find in self.terminos:
            patron_lexico(find)

    def test_frases_en_espanol_con_su_reemplazo(self):
        for find, replace in FRASES_ES.items():
            with self.subTest(frase=find):
                self.assertIn(find, self.terminos)
                self.assertEqual(self.terminos[find]["replace"], replace)

    def test_frases_en_espanol_se_encuentran_en_un_texto(self):
        for find in FRASES_ES:
            with self.subTest(frase=find):
                texto = "Hola. " + find.capitalize() + " y listo."
                self.assertTrue(patron_lexico(find).search(texto))

    def test_estructuras_en_espanol(self):
        por_id = {s["id"]: s for s in self.datos["structures"]}
        for sid, texto in ESTRUCTURAS_ES.items():
            with self.subTest(estructura=sid):
                self.assertIn(sid, por_id)
                self.assertTrue(re.compile(por_id[sid]["regex"], re.MULTILINE).search(texto))

    def test_raya_larga_sigue_en_la_tipografia(self):
        desde = [t["from"] for t in self.datos["typographic"]]
        self.assertIn("\u2014", desde)


class RubricaTest(unittest.TestCase):
    def test_doce_puntos_suman_100(self):
        r = cargar(RUBRIC)
        self.assertEqual(len(r["items"]), 12)
        self.assertEqual(sum(i["points"] for i in r["items"]), r["total"])
        self.assertEqual(r["total"], 100)


if __name__ == "__main__":
    unittest.main()
