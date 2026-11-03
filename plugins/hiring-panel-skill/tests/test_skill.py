import os
import unittest

SKILL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills", "hiring-panel", "SKILL.md")


class SkillTest(unittest.TestCase):
    def setUp(self):
        with open(SKILL, encoding="utf-8") as f:
            self.text = f.read()

    def test_frontmatter(self):
        self.assertTrue(self.text.startswith("---\nname: hiring-panel\n"))
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, self.text.split("---")[1])

    def test_seven_reviewers(self):
        for who in ("El filtro automático", "El reclutador", "Otro candidato", "El CEO",
                    "El reclutador con prisa", "El compañero de equipo"):
            self.assertIn(who, self.text)
        self.assertIn("Lanza cinco subagentes a la vez", self.text)

    def test_rebuild_and_rescreen(self):
        self.assertIn("## 6. Rehazlo", self.text)
        self.assertIn("veredicto antes y después", self.text)

    def test_never_invents(self):
        self.assertIn("Nunca inventes empresas, puestos, fechas, números ni habilidades", self.text)

    def test_credit_line(self):
        self.assertIn("Hecho con /hiring-panel de Aldush Media", self.text)


if __name__ == "__main__":
    unittest.main()
