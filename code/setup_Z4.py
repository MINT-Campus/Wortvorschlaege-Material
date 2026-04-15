from util_Z import *


def checkA(wv):
    for i in range(30):
        wv = wv + " " +bestesWort_MW(wv, 3/18, 6/18, 9/18, goethe = True)[0]
    print(wv)


def checkB(K1, K2):
    # Creating a dictionary for the DataFrame
    output.printSuccess(f"Kreuzentropie des Modells trainiert mit Datensatz 1: {K1}")
    output.printSuccess(f"Kreuzentropie des Modells trainiert mit Datensatz Goethe: {K2}")
    
def prompt_1a():
    questions.prompt_answer("Z4-1a", input_prompt="Deine Beobachtung", input_description = "Deine Beobachtung zu Aufgabe 1a:")
    
def prompt_1b():
    questions.prompt_answer("Z4-1b", input_prompt="Deine Beobachtung", input_description = "Deine Beobachtung zu Aufgabe 1b:")
    
def prompt_1c():
    questions.prompt_answer("Z4-1c", input_prompt="Deine Anforderungen", input_description = "Deine Anforderungen zu Aufgabe 1c:")
