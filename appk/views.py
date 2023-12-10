# views.py
from django.shortcuts import render
from .models import Document
from .utils import systeme_recherche, precision, rappel

def recherche(request):
    query = request.GET.get('q')
    if query:
        resultats_recherche = systeme_recherche(query, Document.objects.all())

        # Assuming you have a relevant set of documents in the database
        resultats_pertinents = Document.objects.filter(contenu__icontains=query)


       
        # Calculate precision and recall
        # common_results = set(resultats_recherche) & set(resultats_pertinents)
        common_results = set(result[0].strip() for result in resultats_recherche) & set(resultat_pertinent.contenu.strip() for resultat_pertinent in resultats_pertinents)

       
        print("Query:", query)
        print("Resultats Recherche:")
        for result in resultats_recherche:
            print(result)

        print("Resultats Pertinents:")
        for result in resultats_pertinents.values_list('contenu', flat=True):
            print(result)

       
        print("Common Results:", common_results)
        print("Resultats Recherche:")
        resultats_recherche_stripped = [result[0].strip() for result in resultats_recherche]

        for result in resultats_recherche_stripped:
            print(result)


        prec = len(common_results) / len(resultats_recherche) if len(resultats_recherche) > 0 else 0.0
        rapp = len(common_results) / len(resultats_pertinents) if len(resultats_pertinents) > 0 else 0.0

        print(prec)
        print(rapp)

    else:
        resultats_recherche_stripped=[]
        prec=0.0
        rapp=0.0


   

    return render(request, 'recherche.html', {'query': query, 'resultats_recherche': resultats_recherche_stripped, 'prec': prec, 'rapp': rapp})
