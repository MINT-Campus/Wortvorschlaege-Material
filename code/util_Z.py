from util import *


# gibt eine Liste alle wörter aus die im datensatz vorkommen in einer sortierten Liste ohne Dopplungen
def getWordsFormDataset(datensatz):
    # Erstelle eine Menge, um doppelte Wörter zu vermeiden
    unique_set = set()

    # Iteriere durch jede Liste im Datensatz
    for liste in datensatz:
        unique_set.update(liste)  # Füge Wörter zur Menge hinzu

    # Konvertiere die Menge zurück in eine Liste
    unique_list = sorted(unique_set)

    return unique_list


def finde(cur_model, w, dict_name):
    historyStr = w.split(" ")
    if len(historyStr) > 1:
        w_last = historyStr[-1].lower()
        w_second_to_last = historyStr[-2].lower()
        history = '["' + w_second_to_last + '", "' + w_last + '"]'
    else:
        history = w
    return cur_model.find(history, dict_name)


# Gibt alle xWortkommbinationen als Liste von Listen aus
def getNxFromDataset(datensatz, x):
    # Initialisiere eine leere Liste, um die Paare zu speichern
    nx = []

    # Iteriere durch jedes Element im Datensatz
    for liste in datensatz:
        # Erstelle Paare von benachbarten Wörtern
        for i in range(len(liste) - (x-1)):
            # Füge das Paar zur n2-Liste hinzu
            element = [liste[i]]
            for j in range(1, x):
                element.append(liste[i+j])
            nx.append(element)
    return nx


def getNWordGroups(datensatz, x):
    # Erstelle eine Menge, um doppelte x-Wort-Kombinationen zu vermeiden
    nWordGroups = set()

    # Füge alle Elemente der zurückgegebenen Liste hinzu
    nWordGroups.update(map(tuple, getNxFromDataset(datensatz, x)))

    # Gib die Kombinationen als sortierte Liste zurück
    return sorted(nWordGroups)


# Holt sich die Lables für eine Tabelle in der in den Zeilen alle Wörter aus dem Datensatz stehen und in den Spalten als xWortkommbinationen
def getLablesFromDataset(datensatz, x):
    columns_labels = getWordsFormDataset(datensatz)
    if x == 0:
        index_labels = ["Häufigkeit"]
    else:
        index_labels = []
        for group in getNWordGroups(datensatz, x):
            index_labels.append(" ".join(group))
    return index_labels, columns_labels


# Gibt eine Tabelle aus
def Tabelle(labels, data={}):
    index_labels, columns_labels = labels
    df = pd.DataFrame(0.0, index=index_labels, columns=columns_labels)
    for (row, col), value in data.items():
        df.at[(row,), col] = value
    return df


def filtern(name, lst):
    return list(filter(lambda p: p == name, lst))