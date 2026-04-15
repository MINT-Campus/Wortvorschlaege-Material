from util import *

def show_transition_table():
    to_fill_df = pd.DataFrame([
    [0,     0,     0,     0,     0,     0],
    [0,     0,     0,     0,     0,     0],
    [0,     0,     0,     0,     0,     0],
    [0,     0,     0,     0,     0,     0],
    [0,     0,     0,     0,     0,     0],
    [0,     0,     0,     0,     0,     0]
    ], columns=["ich", "liebe", "mag", "Mathe", "Physik", "Sport"],
       index=["ich", "liebe", "mag", "Mathe", "Physik", "Sport"])

    correct_df = pd.DataFrame([
        [0,     1/3,   2/3,   0,     0,     0],
        [0,     0,     0,     1,     0,     0],
        [0,     0,     0,     0,     1/2,   1/2],
        [0,     0,     0,     0,     0,     0],
        [0,     0,     0,     0,     0,     0],
        [0,     0,     0,     0,     0,     0]
    ], columns=["ich", "liebe", "mag", "Mathe", "Physik", "Sport"],
       index=["ich", "liebe", "mag", "Mathe", "Physik", "Sport"])
    table.show_tabel_from_df("AB5-3m", to_fill_df, correct_df) 

# --- 


def checkA(p1, p2, p3, p4, p5):
    if p1 == 2/3 and p2 == 1/3 and p3 == 1/2 and p4 == 1/2 and p5 == 1:
        output.printSuccess("Deine Antwort ist korrekt!")
        img = mpimg.imread("../figs/Beispiel_Bigramm.JPG")
        plt.figure(figsize=(5, 4))
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Überlege nochmal ob du:<br>"
                     "... beachtet hast, dass manche Wörter mehrfach im Text vorkommen?<br>"
                     "... gezählt hast, wie oft jedes Wort auftritt und auch gezählt hast, wie oft jedes Wort nach einem bestimmten Wort auftaucht?")


def checkB(B):
    # Define the correct matrix
    correct_matrix = np.array([
        [0, 1/3, 2/3, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1/2, 1/2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ])

    # Check if the input matrix matches the correct matrix
    if np.array_equal(B, correct_matrix):
        output.printSuccess("Deine Antwort ist korrekt!")
        img = mpimg.imread("../figs/Tabelle_filled.JPG")
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()
    else:
        output.printError("Deine Antwort ist noch nicht korrekt. Überlege nochmal ob du:\n"
                     "...die Reihenfolge der Wörter beachtet hast. Die Zeile steht für das vorherige und die Spalte für das nachfolgende Wort.\n")


# vollständiges Bi-Gramm-Modell für kleinen Trainingsdatensatz
T_Bi_small = {
    'ich': {'liebe': 1/3, 'mag': 2/3},
    'liebe': {'mathe': 1},
    'mag': {'physik': 0.5, 'sport': 0.5}
}


def bestesWort_Bi_small(w, T_Bi_dict=T_Bi_small):
    # Extract the last word from the input string, assuming it's separated by non-word characters
    w_last = re.split(r'\W+', w)[-1].lower()

    # Check if the last word is in the dictionary
    if w_last in T_Bi_dict:
        # Sort the suggestions by their values in descending order
        sorted_suggestions = sorted(T_Bi_dict[w_last].items(), key=lambda x: x[1], reverse=True)

        # Gibt die drei bessten suggestions aus
        return sorted_suggestions[:3]
    else:
        print("Es kann kein Vorschlag gemacht werden.")


def prompt_3():
    questions.prompt_answer("AB1-3", input_prompt="Deine Beobachtung", input_description = "Deine Beobachtung zu Aufgabe 3:")


def prompt_4a():
    questions.prompt_answer("AB1-4a", input_prompt="Deine Beschreibung", input_description = "Deine Beschreibung zu Aufgabe 4a):")


def prompt_4b():
    questions.prompt_answer("AB1-4b", input_prompt="Deine Erläuterung", input_description = "Deine Erläuterung zu Aufgabe 4b:")


def prompt_Z2():
    questions.prompt_answer("AB1-Z2", input_prompt="Anzahl der Zweier-Wortsequenzen", input_description = "Anzahl der Zweier-Wortsequenzen zu Aufgabe  Z2:")
