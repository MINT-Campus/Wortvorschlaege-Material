from util import *

def checkA():
    table_procon = [
        [table.Header("Modell"), table.Header("Vorteile"), table.Header("Nachteile")],
        [table.Header("Uni-Gramm-Modell"), table.TextInput(), table.TextInput()],
        [table.Header("Bi-Gramm-Modell"), table.TextInput(), table.TextInput()],
        [table.Header("Tri-Gramm-Modell"), table.TextInput(), table.TextInput()]
    ]
    column_widths = [160, 500, 500]

    table.show_table("AB2-3", table_procon, column_widths)


def prompt_1b():
    questions.prompt_answer("AB2-1b", input_prompt="Gefundene Vorschläge", input_description = "Gefundene Vorschläge zu Aufgabe 1b:")


def prompt_1d():
    questions.prompt_answer("AB2-1d", input_prompt="Gefundene Vorschläge & Vergleich", input_description = "Gefundene Vorschläge und Vergleich zu Aufgabe 1d:")


def prompt_2():
    questions.prompt_answer("AB2-2", input_prompt="Deine Erklärung", input_description = "Deine Erklärung zu Aufgabe 2:")


def prompt_3():
    questions.prompt_answer("AB2-3", input_prompt="Deine Antwort", input_description = "Deine Antwort zu Aufgabe 3:")
