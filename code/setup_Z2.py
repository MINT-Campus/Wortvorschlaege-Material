from util_Z import *

test_datensatz = [["ich", "mag", "physik"], ["ich", "mag", "sport"], ["ich", "liebe", "mathe"], ["jeder", "mag", "ferien"]]

N1 = getNxFromDataset(test_datensatz, 1)

N3 = getNxFromDataset(test_datensatz, 3)


def checkA1(T1, test_datensatz):
    T1_correct = Tabelle(getLablesFromDataset(test_datensatz, 2))
    woerter = getWordsFormDataset(test_datensatz)
    zweiWortGruppen = getNWordGroups(test_datensatz, 2)

    # Ersetze NaN
    for wort in woerter:  # durchläuft alle Wörter des Datensatzes
        for zweiWortGruppe in zweiWortGruppen:  # durchläuft alle Wörter des Datensatzes

            # Schritt 2: Liste der zweier Wortsequenzen filtern
            N2_gefiltert = filtern([zweiWortGruppe[0], zweiWortGruppe[1], wort], N3)
            # Schritt 4: Eintrag mit der Länge der gefilterten Liste befüllen
            T1_correct.at[zweiWortGruppe[0] + " " +  zweiWortGruppe[1], wort] = len(N2_gefiltert)
    if T1_correct.equals(T1):
        output.printSuccess("Du hast die Fuktion korrekt bestimmt")
        return T1
    else:
        output.printError("Überprüfe deine Funktion nochmal")


def checkB1(T2, T1, test_datensatz):
    T2_correct = T1.copy()

    T2_correct.at["ich mag", "physik"] = T1.at["ich mag", "physik"]/(T1.at["ich mag", "physik"]+T1.at["ich mag", "sport"])

    T2_correct.at["ich mag", "sport"] = T1.at["ich mag", "sport"]/(T1.at["ich mag", "physik"]+T1.at["ich mag", "sport"])

    if T2_correct.equals(T2):
        output.printSuccess("Du hast die Werte korrekt geändert")
        return T2
    else:
        output.printError("Überprüfe die Werte nochmal")


def bestesWort_Tri_small(historyStr):
    match historyStr:
        case "ich mag":
            return "physik"
        case "ich liebe":
            return "Mathe"
        case "jeder mag":
            return "Ferien"
        case _:
            output.printError("Hierfür kann kein vorschlag gemacht werden")


def checkA2(T2, T1, test_datensatz):
    T2_correct = T1.copy()

    # Ersetze NaN
    for Wort in getWordsFormDataset(test_datensatz):

        N1_gefiltert = filtern([Wort], N1)  # Liste der Wörter filtern

        T2_correct.at["Häufigkeit", Wort] = len(N1_gefiltert)  # Eintrag mit der Länge der gefilterten Liste befüllen
    if T2_correct.equals(T2):
        output.printSuccess("Du hast die Fuktion korrekt bestimmt")
        return T2
    else:
        output.printError("Überprüfe deine Funktion nochmal")


def checkB2(N):
    if N == len(N1):
        output.printSuccess("Du hast die Länge von N1 korrekt bestimmt")
    else:
        output.printError("Überprüfe die Länge von nochmal")


def checkC2(T3, T2, N):
    T3_correct = T2.copy()

    for Wort in getWordsFormDataset(test_datensatz):
        T3_correct.at["Häufigkeit", Wort] =  T2.at["Häufigkeit", Wort]/N

    if T3_correct.equals(T3):
        output.printSuccess("Du hast die Fuktion korrekt bestimmt")
        return T3
    else:
        output.printError("Überprüfe deine Funktion nochmal")

def bestesWort_Uni_small(historyStr):
    return "ich"