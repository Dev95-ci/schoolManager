from django.shortcuts import render, redirect
from .models import Eleve, Paiement
from .forms import PaiementForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def effectuer_paiement(request):
    if request.method == "POST":
        form = PaiementForm(request.POST)
        if form.is_valid():
            paiement = form.save(commit=False)
            montant_restant = paiement.eleve.montant_total  # Récupérer le montant dû
            
            # Vérifier si le paiement dépasse le montant restant
            if paiement.montant > montant_restant:
                messages.error(request, f"Erreur : Le montant saisi ({paiement.montant} Fcfa) dépasse le solde restant ({montant_restant} fcfa).")
            else:
                # Déduire le montant payé du total dû
                paiement.eleve.montant_total -= paiement.montant
                paiement.eleve.save()
                paiement.save()
                messages.success(request, "Paiement enregistré avec succès.")
                
    else:
        form = PaiementForm()

    return render(request, "paiements/effectuer_paiement.html", {"form": form})







@login_required
def liste_paiements(request):
    query = request.GET.get('q', '')  # Récupérer la recherche
    filtre_methode = request.GET.get('methode', '')  # Filtre sur méthode de paiement
    filtre_status = request.GET.get('status', '')  # Filtre sur statut

    paiements = Paiement.objects.all()

    if query:
        paiements = paiements.filter(eleve__nom__icontains=query)

    if filtre_methode:
        paiements = paiements.filter(methode_paiement=filtre_methode)

    if filtre_status:
        paiements = paiements.filter(status=filtre_status)

    paginator = Paginator(paiements, 20)  # 10 paiements par page
    page_number = request.GET.get('page')
    paiements_page = paginator.get_page(page_number)

    return render(request, 'paiements/liste_paiements.html', {
        'paiements': paiements_page,
        'query': query,
        'filtre_methode': filtre_methode,
        'filtre_status': filtre_status
    })