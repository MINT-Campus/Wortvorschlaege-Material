from util import *


def checkA(gesamtnote):
    if gesamtnote == 1/4 * 3.0 + 1/4 * 2.0 + 0.4 * 2.0 + 0.1 * 1.0:
        output.printSuccess("Deine Antwort ist korrekt! Das von dir berechnete Ergebnis ist " + str(round(gesamtnote, 2)))
    elif gesamtnote == (3.0 + 2.0 + 2.0 + 1.0) / 4:
        output.printError("Deine Antwort ist noch nicht korrekt. Überprüfe, ob die Noten der Tests tatsächlich weniger stark in die Gesamtnote einfliesen, wie die Noten Klassenarbeiten.")
    else:
        output.printError(f"Deine Antwort ist noch nicht korrekt. Das von dir berechnete Ergebnis ist {round(gesamtnote, 2)}.")


def checkE(g_1, g_2, g_3, P_ges):
    if (P_ges == g_1 * P_Uni("einfach") + g_2*P_Bi("gerne","einfach") + g_3*P_Tri("würde", "gerne","einfach") ) and np.isclose(g_1 + g_2 + g_3, 1) and (g_1 != 0) and (g_2 != 0) and (g_3 != 0):
        output.printSuccess("Deine Antwort ist korrekt! Die von die Berechnete Wahrscheinlichkeit ist " + str(round(P_ges, 3)) + ".")
    elif (P_ges == g_1 * P_Uni("einfach") + g_2*P_Bi("gerne","einfach") + g_3*P_Tri("würde", "gerne","einfach") ) and ((g_1 + g_2 + g_3 != 1) or (g_1 == 0) or (g_2 == 0) or (g_3 == 0)):
        output.printError("Deine Antwort ist noch nicht korrekt. Überprüfe, ob die Bedingungen für die Gewichte erfüllt sind.")
    elif (P_ges != g_1 * P_Uni("einfach") + g_2*P_Bi("gerne","einfach") + g_3*P_Tri("würde", "gerne","einfach") ) and np.isclose(g_1 + g_2 + g_3, 1) and (g_1 != 0) and (g_2 != 0) and (g_3 != 0):
        output.printError("Deine Antwort ist noch nicht korrekt. Verlgeiche deine Gesamtübergangswahrschenlichkeit mit der oben aufgestellten Formel.")
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Überprüfe, ob die Bedingungen für die Gewichte erfüllt sind und vergleiche deine Gesamtübergangswahrscheinlichkeit mit der oben aufgestellten Formel.")




def prompt_1b():
    questions.prompt_answer("AB3-1b", input_prompt="Bedingungen für die Gewichte", input_description = "Deine Antwort zu Aufgabe 1b:")


def prompt_1d():
    questions.prompt_answer("AB3-1d", input_prompt="Deine Antwort", input_description = "Deine Antwort zu Aufgabe 1d:")


# Aufruf mit Antwortmöglichkeiten
def select_1b():
    single_choise.show_correct_text_selection([(r"$\frac{n_1+n_2+n_3+n_4}{4}$", False, "Diese Formel berechnet den einfachen (ungewichteten) Mittelwert. Dabei wird nicht berücksichtigt, dass einzelne Werte unterschiedlich stark gewichtet werden sollen."),
            (r"$\frac{g_1\cdot n_1+g_2 \cdot n_2+g_3 \cdot n_3+g_4 \cdot n_4}{4}$", False,
             "Diese Formel teilt den gewichteten Mittelwert durch 4, was mathematisch falsch ist. Die Gewichtung sorgt bereits für die richtige Verteilung – eine zusätzliche Division verzerrt das Ergebnis."),
            (r"$g_1\cdot n_1+g_2 \cdot n_2+g_3 \cdot n_3+g_4 \cdot n_4$", True,
             "Richtig!")])


def select_1c():
    single_choise.show_correct_text_selection([(r"$P_{ges}(Wort) = g_1 \cdot P_{Uni}(Wort) + g_2 \cdot P_{Bi}(Wort) + g_3 \cdot P_{Tri}(Wort)$", True, "Richtig!"),
            (r"$P_{ges}(Wort) = g_3 \cdot P_{Uni}(Wort) + g_2 \cdot P_{Bi}(Wort) + g_1 \cdot P_{Tri}(Wort)$", False,
             "Die Formel ist strukturell richtig aufgebaut – sie kombiniert die Übergangswahrscheinlichkeiten der Uni-, Bi- und Tri-Gramm-Modelle mit Gewichtungsfaktoren. Allerdings sind hier die Gewichte $g_1$, $g_2$, $g_3$ den falschen Modellen zugeordnet."),
            (r"$P_{ges}(Wort) = \frac{g_1}{P_{Uni}(Wort)} + \frac{g_2}{P_{Bi}(Wort)} + \frac{g_3}{P_{Tri}(Wort)}$", False,
             "Hier werden die Gewichte durch die Wahrscheinlichkeiten geteilt. Das ergibt rechnerisch keinen Mittelwert, sondern hat eine völlig andere Bedeutung – diese Formel ist für eine gewichtete Kombination nicht geeignet.")])

