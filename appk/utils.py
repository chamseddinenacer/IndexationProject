# utils.py
def systeme_recherche(requete, ensemble_documents):
    # Simulate the search system using simple criteria
    resultats = []
    for document in ensemble_documents:
        matching_terms = [mot_cle.lower() for mot_cle in requete.split() if mot_cle.lower() in document.contenu.lower().strip()]
        if matching_terms:
            resultats.append((document.contenu.strip(), matching_terms))
    return resultats




def precision(resultats_recherche, resultats_pertinents):
    
    if len(resultats_recherche) == 0 or len(resultats_pertinents) == 0:
        return 0.0
    return len(set(resultats_recherche) & set(resultats_pertinents)) / len(resultats_recherche)

def rappel(resultats_recherche, resultats_pertinents):
    
    if len(resultats_pertinents) == 0:
        return 0.0
    return len(set(resultats_recherche) & set(resultats_pertinents)) / len(resultats_pertinents)
