from util_Z import *

test_datensatz = [["ich", "mag", "physik"], ["ich", "mag", "sport"], ["ich", "liebe", "mathe"]]

N2 = getNxFromDataset(test_datensatz, 2)


def checkB(Tabelle1):
    # Überprüfen der Bedingungen für T1
    if (Tabelle1.at["ich", "ich"] == 0 and
        Tabelle1.at['ich', 'liebe'] == 1 and
        Tabelle1.at['ich', 'mag'] == 2 and
        Tabelle1.at['ich', 'mathe'] == 0 and
        Tabelle1.at['ich', 'physik'] == 0 and
            Tabelle1.at['ich', 'sport'] == 0):
        output.printSuccess("Deine Antwort ist korrekt!")

        # Zeige die Tabelle
        return Tabelle1
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Möglicherweise hast du dich verzählt.")


def checkC(N2_gefiltert):
    correct_list = filtern(["ich", "mag"], N2)
    if N2_gefiltert == correct_list:
        output.printSuccess("Deine Antwort ist korrekt!")
        df = pd.DataFrame([' '.join(pair) for pair in N2_gefiltert], columns=["zweier Wortsequenzen"])
        return df
    else:
        output.printError("Deine Antwort ist noch nicht korrekt.")


def checkD():
    # Eingabefeld und Button
    text_input = widgets.Text(
        value='',
        placeholder='Dein Wort...',
        description='Lücke:',
        disabled=False
    )

    check_button = widgets.Button(
        description='Überprüfen',
    )

    ausgabe = widgets.Output()

    def on_check_clicked(b):
        with ausgabe:
            clear_output()
            eingabe = text_input.value.strip()
            if eingabe in ["Länge", "Mächtigkeit", "Größe", "Anzahl der Einträge", "Zeilenanzahl", "länge", "größe", "Zeilenlänge", "Anzahl der Zeilen"]:
                output.printSuccess("Deine Antwort ist korrekt")
            else:
                output.printError("Deine Antwort ist leider nicht korrekt")

    check_button.on_click(on_check_clicked)
    display(text_input, check_button, ausgabe)


def checkD2(Tabelle2):
    if (Tabelle2.at['ich', 'mag'] == 2):
        output.printSuccess("Deine Antwort ist korrekt!")

        # Zeige die Tabelle
        return Tabelle2
    else:
        output.printError("Deine Antwort ist noch nicht korrekt")


def checkE(Tabelle3):
    index, columns = getLablesFromDataset(test_datensatz, 1)
    T3_correct = Tabelle(getLablesFromDataset(test_datensatz, 1))
    for Wort1 in index:
        for Wort2 in columns:

            N2_gefiltert = filtern([Wort1, Wort2], N2)

            T3_correct.at[Wort1, Wort2] = len(N2_gefiltert)
    if T3_correct.equals(Tabelle3):
        output.printSuccess("Deine Antwort ist korrekt!")
    # Zeige die Tabelle
        return Tabelle3
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Möglicherweise hast du dich verzählt.")


def checkF(Tabelle4, Tabelle3):
    T4_correct = Tabelle(getLablesFromDataset(test_datensatz, 1))
    T4_correct.at["ich","ich"]   = Tabelle3.at["ich","ich"]/np.sum(Tabelle3.loc['ich'])
    T4_correct.at["ich","liebe"] = Tabelle3.at["ich","liebe"]/np.sum(Tabelle3.loc['ich'])
    T4_correct.at["ich","mag"]   = Tabelle3.at["ich","mag"]/np.sum(Tabelle3.loc['ich'])
    T4_correct.at["ich","mathe"] = Tabelle3.at["ich","mathe"]/np.sum(Tabelle3.loc['ich'])
    T4_correct.at["ich","physik"]= Tabelle3.at["ich","physik"]/np.sum(Tabelle3.loc['ich'])
    T4_correct.at["ich","sport"] = Tabelle3.at["ich","sport"]/np.sum(Tabelle3.loc['ich'])
    if T4_correct.equals(Tabelle4):
        output.printSuccess("Deine Antwort ist korrekt!")
        # Zeige die Tabelle
        return Tabelle4
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Möglicherweise hast du dich verzählt.")