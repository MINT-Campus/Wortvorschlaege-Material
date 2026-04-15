import json
import operator
import ast

class modell_Wortvorschlaege:
    def __init__(self):
        self.data_dicts = {}
        self.possible_words = []

    def load_data(self, zusatzblatt=False):
        if zusatzblatt:
            data_path = '../../data/'
        else:
            data_path = '../data/'
        json_files = ['T_Uni_dict.json', 'T_Uni_g_dict.json', 'T_Bi_dict.json',
                      'T_Bi_g_dict.json', 'T_Tri_dict.json', 'T_Tri_g_dict.json',
                      'T_Test_dict.json']
        for file_name in json_files:
            with open(data_path + file_name, 'r') as f:
                # Load the JSON data into a dictionary
                data = json.load(f)
                # Store it in the data_dicts using the file name
                # (without extension) as the key
                key = file_name.split('.')[0]
                self.data_dicts[key] = data
        self.possible_words = list(self.data_dicts['T_Uni_dict'].keys())

    def get_possible_words(self):
        return self.possible_words

    def find(self, dict_name):
        if dict_name not in self.data_dicts:
            return []
        if dict_name == 'T_Tri_dict' or dict_name == 'T_Tri_g_dict':
            return self.liste_zu_string(self.data_dicts[dict_name].keys())
        return self.data_dicts[dict_name].keys()

    def liste_zu_string(self, liste_str):
        try:
            # Wandle den String in eine echte Liste um
            liste = ast.literal_eval(liste_str)
            # Überprüfen, ob es wirklich eine Liste aus Strings ist
            if isinstance(liste, list) and all(isinstance(wort, str) for wort in liste):
                return ' '.join(liste)
            else:
                return "Ungültiges Format"
        except (ValueError, SyntaxError):
            return "Ungültiger Eingabestring"

    def predict_uni(self):
        sortiertes_dict = sorted(self.data_dicts['T_Uni_dict'].items(),
                                 key=lambda item: item[1], reverse=True)
        words = [tup[0] for tup in sortiertes_dict[:3]]
        return words

    def predict_bi(self, historyStr):
        if len(historyStr.split()) < 1:
            return None

        history = historyStr.split()[-1].lower()

        if history in self.data_dicts['T_Bi_dict']:
            sorted_tuples = sorted(self.data_dicts['T_Bi_dict'][history].items()
                                   , key=lambda item: item[1], reverse=True)
            words = [tup[0] for tup in sorted_tuples[:3]]
            return words
        else:
            return None

    def predict_tri(self, historyStr):
        if len(historyStr.split()) < 2:
            return None

        w_last = historyStr.split()[-1].lower()
        w_second_to_last = historyStr.split()[-2].lower()
        history = '["' + w_second_to_last + '", "' + w_last + '"]'

        if history in self.data_dicts['T_Tri_dict']:
            sorted_tuples = sorted(self.data_dicts['T_Tri_dict'][history], key=operator.itemgetter(1)
                                   , reverse=True)
            words = [tup.split('"')[3] for tup in sorted_tuples[:3]]
            return words
        else:
            return None

    def P_uni(self, w, goethe=False):
        if goethe:
            dictonary = self.data_dicts['T_Uni_g_dict']
        else:
            dictonary = self.data_dicts['T_Uni_dict']
        if w in dictonary:
            return dictonary[w]
        else:
            return 0

    def P_bi(self, historyStr, w, goethe=False):
        if goethe:
            dictonary = self.data_dicts['T_Bi_g_dict']
        else:
            dictonary = self.data_dicts['T_Bi_dict']
        if len(historyStr.split()) < 1:
            return 0

        history = historyStr.split()[-1].lower()

        if history in dictonary and w in dictonary[history]:
            return dictonary[history][w]
        else:
            return 0

    def P_tri(self, historyStr, w, goethe=False):
        if goethe:
            dictonary = self.data_dicts['T_Tri_g_dict']
        else:
            dictonary = self.data_dicts['T_Tri_dict']
        if len(historyStr.split()) < 2:
            return 0

        w_last = historyStr.split()[-1].lower()
        w_second_to_last = historyStr.split()[-2].lower()
        history = '["' + w_second_to_last + '", "' + w_last + '"]'

        if history in dictonary and '["' + w_last + '", "' + w + '"]' in dictonary[history]:
            return dictonary[history]['["' + w_last + '", "' + w + '"]']
        else:
            return 0