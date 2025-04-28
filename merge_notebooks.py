import nbformat

# Lista twoich notatników do połączenia
notebooks = ['fraud_eda.ipynb', 'fraud_fe.ipynb', 'fraud_model.ipynb']

# Wczytaj pierwszy notatnik jako bazowy
merged_notebook = nbformat.read(notebooks[0], as_version=4)

# Iteruj przez pozostałe i dodawaj ich komórki
for nb_file in notebooks[1:]:
    nb = nbformat.read(nb_file, as_version=4)
    merged_notebook.cells.extend(nb.cells)

# Zapisz wynik do nowego pliku
with open('merged_notebook.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)

print("Notatniki zostały poprawnie połączone!")