import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import re
import pandas as pd
from collections import Counter
import inspect
import sys
import os
from IPython.display import HTML, display, clear_output
import ipywidgets as widgets

# Interne Imports
import template.output as output
import template.questions as questions
import template.text_order_widget as text_order_widget
import template.table_widget as table
import template.text_multiple_choice_widget as multiple_choice
import template.text_single_choice_widget as single_choise
import modell


def check_functional_equivalence(student_func, reference_func, test_cases):
    success = True
    failed = []

    # Temporäres Überschreiben von output.printSuccess, output.printError und output.html
    original_success = output.printSuccess
    original_wrong = output.printError
    original_html = output.html
    
    def no_op(*args, **kwargs):
        pass  # Keine Ausgabe erzeugen
    
    # Überschreibe output-Funktionen, sodass sie nichts tun
    output.printSuccess = no_op
    output.printError = no_op
    output.html = no_op

    for case in test_cases:
        try:
           # Überprüfung der Anzahl der Argumente und Aufruf der Funktionen
            ref_result = reference_func(*case)
            student_result = student_func(*case)

            if student_result != ref_result:
                success = False
                failed.append(case)
        except Exception as e:
            success = False
            failed.append((case, str(e)))
            
    # Wiederherstellen der Originalfunktionen 
    output.printSuccess = original_success
    output.printError = original_wrong
    output.html = original_html

    if success:
        return None
    else:
        return failed


cur_modell = None


def init_modell(zusatzblatt=False):
    global cur_modell
    if cur_modell is None:
        cur_modell = modell.modell_Wortvorschlaege()
        cur_modell.load_data(zusatzblatt)
    return cur_modell


def get_possible_words():
    global cur_modell
    return cur_modell.possible_words


def get_test():
    global cur_modell
    return cur_modell.data_dicts["T_Test_dict"]


def bestesWort_Uni(history):
    # history wird nicht verwendet. Dient zu Demozwecken.
    return cur_modell.predict_uni()


def bestesWort_Bi(history):
    prediction = cur_modell.predict_bi(history)
    if prediction is None:
        print("Es gibt leider keine Vorhersage für dieses Wort. Wähle eine andere Wortvorgeschichte.")
    else:
        return prediction


def bestesWort_Tri(history):
    if len(history.split(" ")) < 2:
        print("Es gibt leider keine Vorhersage für dieses Wort. Wähle eine Wortvorgeschichte die mindestens zwei Wörter umfasst.")
        return
    prediction = cur_modell.predict_tri(history)
    if prediction is None:
        print("Es gibt leider keine Vorhersage für dieses Wort. Wähle eine andere Wortvorgeschichte.")
    else:
        return prediction


def P_Uni(f, goethe=False):
    probability = cur_modell.P_uni(f, goethe)
    if probability is None:
        return 0
    else:
        return probability


def P_Bi(history, f, goethe=False):
    probability = cur_modell.P_bi(history, f, goethe)
    if probability is None:
        return 0
    else:
        return probability


def P_Tri(w_2, w_1, f, goethe=False):
    probability = cur_modell.P_tri(w_2 + " " + w_1, f, goethe)
    if probability is None:
        return 0
    else:
        return probability


def bestesWort_MW(history, g_1, g_2, g_3, goethe=False):
    if None in (history, g_1, g_2, g_3):
        output.printError("Ersetze alle None im Befehl")
        return

    possible_words = cur_modell.possible_words
    top3 = []  # Liste für (Wort, Wahrscheinlichkeit)

    for word in possible_words:
        P_ges = (
            g_1 * P_Uni(word, goethe)
            + g_2 * P_Bi(history, word, goethe)
            + g_3 * cur_modell.P_tri(history, word, goethe)
        )

        if len(top3) < 3:
            top3.append((word, P_ges))
            top3.sort(key=lambda x: x[1], reverse=True)
        elif P_ges > top3[-1][1]:
            top3[-1] = (word, P_ges)
            top3.sort(key=lambda x: x[1], reverse=True)

    return [word for word, _ in top3]


def bestesWort_rueckfallZ(history):
    # Bedingungsabfragen und Anweisungen
    tri_predictions = cur_modell.predict_tri(history) or []  # Falls None, wird es zu einer leeren Liste
    bi_predictions = cur_modell.predict_bi(history) or []    # Falls None, wird es zu einer leeren Liste

    elements_from_Tri = len(tri_predictions)
    elements_from_Bi = min(3 - len(tri_predictions), len(bi_predictions))
    element_from_Uni = max(3 - (len(tri_predictions) + len(bi_predictions)), 0)  # Sicherstellen, dass es nicht negativ wird
    return tri_predictions[:elements_from_Tri] + bi_predictions[:elements_from_Bi] + cur_modell.predict_uni()[:element_from_Uni]


def KE(g_0, g_1, g_2, g_3, goethe=False):
    if None in (g_0, g_1, g_2, g_3):
        output.printError("Ersetze alle None im Befehl.")
        return
    P_Mod = 0  # Variable for storing the logarithmic model probability
    N = 0

    if g_0 + g_1 + g_2 + g_3 > 1 + 0.00001 or g_0 + g_1 + g_2 + g_3 < 1 - 0.00001 or g_0 < 0 or g_1 < 0 or g_2 < 0 or g_3 < 0:
        print("Die Gewichte sind außerhalb des zulässigen Bereiches.")
    else:
        # Loop through all sentences in the test dataset 'data_test'
        for i in range(len(cur_modell.data_dicts["T_Test_dict"])):
            # Loop through all words in each sentence
            for j in range(len(cur_modell.data_dicts["T_Test_dict"][i])):
                N += 1  # Count total number of words
                f = cur_modell.data_dicts["T_Test_dict"][i][j]  # Current word

                # Retrieve previous words (w_1 and w_2) based on their positions
                w_1 = cur_modell.data_dicts["T_Test_dict"][i][j-1] if j-1 >= 0 else ""
                w_2 = cur_modell.data_dicts["T_Test_dict"][i][j-2] if j-2 >= 0 else ""

                # Calculate transition probability of the words
                P_i_j = (
                    g_0 * 1 / 75000 +
                    g_1 * P_Uni(f, goethe) +
                    g_2 * P_Bi(w_1, f, goethe) +
                    g_3 * P_Tri(w_2, w_1, f, goethe)
                )

                # Update the logarithmic model probability
                P_Mod += np.log(P_i_j)

        # Return the negative average log-probability
        return -1 / N * P_Mod