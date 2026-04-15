from util import *

from scipy.optimize import minimize, Bounds
import numpy as np

def opt():
    # Zielfunktion: KE mit g_3 = 1 - g_0 - g_1 - g_2
    def objective(weights):
        g_0, g_1, g_2 = weights
        g_3 = 1.0 - g_0 - g_1 - g_2
        return KE(g_0, g_1, g_2, g_3)

    # Nebenbedingungen
    constraints = [
        {'type': 'ineq', 'fun': lambda x: x[0] - 0.001},        # g_0 >= 0.001
        {'type': 'ineq', 'fun': lambda x: x[1]},                # g_1 >= 0
        {'type': 'ineq', 'fun': lambda x: x[2]},                # g_2 >= 0
        {'type': 'ineq', 'fun': lambda x: 1.0 - sum(x)},        # g_3 = 1 - sum >= 0
    ]

    # Bounds für g_0, g_1, g_2
    bounds = Bounds([0.001, 0.0, 0.0], [1.0, 1.0, 1.0])

    # Startwerte
    x0 = [0.1, 0.1, 0.1]

    # Optimierung starten
    result = minimize(objective, x0, method='SLSQP', constraints=constraints, bounds=bounds)

    if result.success:
        g_0, g_1, g_2 = result.x
        g_3 = 1.0 - g_0 - g_1 - g_2
        print("Optimierung erfolgreich.\n")
        print(f"g_0 = {g_0:.4f}, g_1 = {g_1:.4f}, g_2 = {g_2:.4f}, g_3 = {g_3:.4f}")
        print(f"Kreuzentropie: {KE(g_0, g_1, g_2, g_3):.6f}")
    else:
        print("Optimierung fehlgeschlagen:", result.message)


def nebenbedingung():
    multiple_choice.show_multiple_choice_with_feedback([
        ("$g_0>0, g_1>0, g_2>0, g_3>0$", True),
        ("$g_0<0, g_1<0, g_2<0, g_3<0$", False),
        ("$g_0>1, g_1>1, g_2>1, g_3>1$", False),
        ("$g_0 + g_1 = 1, g_2 + g_3 = 1$", False),
        ("$g_0 + g_1 + g_2 + g_3 = 1$", True)
    ], feedback_messages = {
        "success": "Korrekt!<br>Das Optimierungsproblem lautet: <br><br>Minimiere $K(g_0, g_1, g_2, g_3)$ <br> unter den Nebenbedingungen $g_0>0, g_1>0, g_2>0, g_3>0$ und $g_0+g_1+g_2+g_3=1$.",
        "wrong": "Deine Antwort ist noch nicht korrekt. Es kann helfen, dir deine Überlegungen zu den Gewichten auf Aufgabenblatt 3 Aufgabe 1 d) erneut anzusehen.",
        "missing": "Deine Antwort ist noch nicht korrekt. Es kann helfen, dir deine Überlegungen zu den Gewichten auf Aufgabenblatt 3 Aufgabe 1 d) erneut anzusehen.",
        "nothing_selected": "Bitte wähle mindestens eine Option aus."
    })
        
def prompt_1b():
    questions.prompt_answer("AB5-1b", input_prompt="Deine Antwort", input_description = "Deine Antwort zu Aufgabe 1b:")