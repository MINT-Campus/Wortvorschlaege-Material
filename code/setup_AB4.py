from util import *


def single_choise_1a():
    options = [("$P(Wort~1,Wort~2,...,Wort~n)=P_{ges}(Wort~1)+P_{ges}(Wort~2)+...+P_{ges}(Wort~n)$", False, "Das ist nicht korrekt. Schaue dir nochmal den Tipp zum Logarithmusgesetz an"),
           (r"$P(Wort~1,Wort~2,...,Wort~n)=P_{ges}(Wort~1)\cdot P_{ges}(Wort~2)\cdot ...\cdot P_{ges}(Wort~n)$", True, r"Korrekt! Das Auftreten jedes Wortes im Text kann als ein einzelnes Ereignis angesehen und die Übergangswahrscheinlichkeit als eine Wahrscheinlichkeit im Baumdiagramm dargestellt werden. Die Gesamtwahrscheinlichkeit ergibt sich gemäß der 1. Pfadregel oder auch Produktregel für mehrstufige Zufallsexperimente aus dem Produkt der einzelnen Übergangswahrscheinlichkeiten. Die Kreuzentropie ergibt sich damit zu $K=−\frac{1}{n} \cdot log(P_{ges}(Wort~1)\cdot  P_{ges}(Wort~2)\cdot  ...\cdot  P_{ges}(Wort~n))$."),
           (r"$P(Wort~1,Wort~2,...,Wort~n)= \frac{1}{n} \cdot P_{ges}(Wort~1)+ \frac{1}{n} \cdot P_{ges}(Wort~2)+...+\frac{1}{n}\cdot P_{ges}(Wort~n)$", False, "Deine Antwort ist noch nicht korrekt! Schaue dir die Tipps an!"),]
    single_choise.show_correct_text_selection(options)


def single_choise_1c():
    options = [("$log(P_{ges}(w_1)⋅P_{ges}(w_2)⋅...⋅P_{ges}(w_n))=P_{ges}(w_1)+P_{ges}(w_2)+...+P_{ges}(w_n)$", False, "Das ist nicht korrekt. Schaue dir nochmal den Tipp zum Logarithmusgesetz an"),
           ("$log(P_{ges}(w_1)⋅P_{ges}(w_2)⋅...⋅P_{ges}(w_n))=log(P_{ges}(w_1)+P_{ges}(w_2)+...+P_{ges}(w_n))$", False, "Das ist nicht korrekt. Schaue dir nochmal den Tipp zum Logarithmusgesetz an"),
           ("$log(P_{ges}(w_1)⋅P_{ges}(w_2)⋅...⋅P_{ges}(w_n))=log(P_{ges}(w_1))+log(P_{ges}(w_2))+...+log(P_{ges}(w_n))$", True, "Korrekt! Somit ergibt sich die Kreuzentropie zu $K=−1N⋅[log(P_{ges}(w_1))+log(P_{ges}(w_2))+...+log(P_{ges}(w_n))]$"),]
    single_choise.show_correct_text_selection(options)

def checkE(w_1_2, data_test):
    if w_1_2 == data_test[1][2]:
        output.printSuccess("Deine Antwort ist korrekt! Ausgabe: " + str(w_1_2))
    else:
        output.printError("Deine Antwort ist noch nicht korrekt.")


def checkF(P_1_2, data_test, P_uni, P_bi, P_tri):
    P_1_2_solution = 1/6 * P_uni(data_test[1][2]) + 2/6 * P_bi(data_test[1][1], data_test[1][2]) + 3/6 * P_tri(data_test[1][0], data_test[1][1], data_test[1][2])
    if np.isclose(P_1_2, P_1_2_solution):
        output.printSuccess("Deine Antwort ist korrekt! Die Wahrscheinlichkeit ist " + str(round(P_1_2, 4)) + ".")
        return
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Überprüfe die Gewichte und die Reihenfolge, in der du die Position des Satzes und die Position der Wörter angegeben hast.")


def checkG(P_i_j, data_test, P_uni, P_bi, P_tri):
    # Testdaten
    data_test = [
        ["Das", "ist", "ein", "Test"],
        ["Ein", "weiterer", "Satz", "hier"]
    ]
    failed = False

    # Beispieltest 1
    result_1 = P_i_j(0, 3, data_test)
    expected_1 = (1/6 * P_uni("Test") +
                  2/6 * P_bi("ein", "Test") +
                  3/6 * P_tri("ist", "ein", "Test"))

    if not( abs(result_1 - expected_1) < 1e-6):
        failed = True

    # Beispieltest 2
    result_2 = P_i_j(1, 2, data_test)
    expected_2 = (1/6 * P_uni("Satz") +
                  2/6 * P_bi("weiterer", "Satz") +
                  3/6 * P_tri("Ein", "weiterer", "Satz"))

    if not( abs(result_2 - expected_2) < 1e-6):
        failed = True
    if failed:
        output.printError("Leider ist deine Definition von P_i_j noch nicht korrekt.")
    else:
        output.printSuccess("Du hast P_i_j korrekt implementiert")


# Achtung Lösung ist hardcoded auf den Datensatz
def checkH(P_Mod):
    if np.isclose(P_Mod, -109822.99041079674, rtol=1e-9):
        output.printSuccess("Deine Antwort ist korrekt! Die Wahrscheinlichkeit ist -inf.")
    elif np.isclose(P_Mod, -0.6909345426262036, rtol=1e-9):
        output.printError("Deine Antwort ist noch nicht korrekt. Vermutlich überschreibst du P_Mod in jedem Schritt, anstatt den Logarithmus der neuen Übergangswahrscheinlichkeit zu addieren.")
    else:
        output.printError("Deine Antwort ist noch nicht korrekt.")


def check_J(P_g):
    if np.isclose(P_g,1/75000, rtol=1e-9):
        output.printSuccess("Du hast die Glättungswahrscheinlichkeit mit 1/75000 korrekt bestimmt")
    else:
        output.printError("Deine Glättungswahrscheinlichkeit passt leider noch nicht")


def checkK(P_Mod):
    if np.isclose(P_Mod, -125133.99942625922, rtol=1e-9):
        output.printSuccess("P_Mod: " + str(round(P_Mod,4)) + " Dies entspricht einer Modellwahrscheinlichkeit nahe "+ str(np.exp(P_Mod)) + ".")
    else:
        output.printError("Dein Ergebniss passt leider noch nicht.")


def checkL(K, n, P_Mod):
    K_solution = -1/n*P_Mod
    if np.isclose(K, K_solution, rtol=1e-9):
        output.printSuccess(f"Du hast die Kreuzentropie mit {str(K)} korrekt berechnet")
    else:
        output.printError("leider passt deine Berechung noch nicht")


def check_2A(P_random):
    if np.isclose(P_random,1/75000, rtol=1e-9):
        output.printSuccess("Du hast die Wahrscheinlichkeit für ein rein zufälligees Wort mit 1/75000 korrekt bestimmt")
    else:
        output.printError("Deine Wahrscheinlichkeit für ein rein zufälligees Wort passt leider noch nicht")


def check2B(K_Z):
    K_Z_solution = np.log(75000)
    if K_Z == K_Z_solution:
        output.printSuccess("Korrekt! Die Kreutzentropie für eine zufällige Auswahl beträgt " + str(K_Z) + ".")
    else:
        output.printSuccess("Deine Berechung für die Kreutzentropie ist noch nicht korrekt.")


def prompt_1b():
    questions.prompt_answer("AB4-1b", input_prompt="Deine Begründung", input_description = "Deine Begründung zu Aufgabe 1d:")


def prompt_1i():
    questions.prompt_answer("AB4-1i", input_prompt="Deine Begründung", input_description = "Deine Begründung zu Aufgabe 1i:")


def prompt_2d():
    questions.prompt_answer("AB4-1d", input_prompt="Deine Begründung", input_description = "Deine Begründung zu Aufgabe 1i:")