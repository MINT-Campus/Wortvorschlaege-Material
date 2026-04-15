from util_Z import *

cur_modell = init_modell(zusatzblatt = True)

#---------------------- Musterlösungen der Funktionen --------------------------------------------------------------------------------------

def rueckfallstrategie_correct(T_Tri, T_Bi, cur_modell):
    if "würde gerne" in find(T_Tri):
        Vorschlag = bestesWort_Tri("würde gerne")
    elif "gerne" in find(T_Bi): 
        Vorschlag = bestesWort_Bi("gerne")
    else:
        Vorschlag = bestesWort_Uni("")

    # No changes here
    return Vorschlag

#-------------------------- Test Fälle --------------------------------------------------------------------------------------------------
test_cases_A0 = [
    ("T_Tri_dict", "T_Bi_dict", cur_modell),
    ("", "T_Bi_dict", cur_modell),
    ("", "", cur_modell)
]
    
#------------------------- Check Functions -----------------------------------------------------------------------------------------------


def checkA0(student_rueckfallstrategie):
    failed_tests = check_functional_equivalence(student_rueckfallstrategie, rueckfallstrategie_correct, test_cases_A0)
    if failed_tests is None:
        output.printSuccess("Du hast die Rückfallstrategie richtig implementiert")
    else:
        output.printError("Du hast noch bei folgenden Fällen fehler gemacht")
        print(failed_tests)


def checkA1(student_code_def):
    student_code = inspect.getsource(student_code_def)
    # Die Musterlösung als Vergleich
    correct_code = {
        "if_condition": 'w_second_to_last + " " + w_last in find(T_Tri)',
        "if_assignment": "Vorschlag = bestesWort_Tri(historyStr)",
        "elif_condition": "w_last in find(T_Bi)",
        "elif_assignment": "Vorschlag = bestesWort_Bi(historyStr)",
        "else_assignment": "Vorschlag = bestesWort_Uni(historyStr)"
    }

    # Flags zum Überprüfen, ob die Bedingungen und Zuweisungen korrekt sind
    if_correct = correct_code["if_condition"] in student_code and correct_code["if_assignment"] in student_code
    elif_correct = correct_code["elif_condition"] in student_code and correct_code["elif_assignment"] in student_code
    else_correct = correct_code["else_assignment"] in student_code

    # Ergebnis zurückgeben
    if if_correct and elif_correct and else_correct:
        output.printSuccess("Der Code ist korrekt implementiert.")
    else:
        errors = []
        if not if_correct:
            errors.append("Die if-Bedingung oder Zuweisung ist falsch.")
        if not elif_correct:
            errors.append("Die elif-Bedingung oder Zuweisung ist falsch.")
        if not else_correct:
            errors.append("Die else-Zuweisung ist falsch.")
        output.printError("Du hast noch folgende Fehler gemacht: " + "\n".join(errors))


def find(dict):
    return cur_modell.find(dict)



def prompt_1a():
    questions.prompt_answer("Z3-1a", input_prompt="Deine Strategie", input_description = "Deine Strategie zu Aufgabe 1a:")