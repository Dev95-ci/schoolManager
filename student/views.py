from kivy.uix.filechooser import error
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .models import Eleve  # Exemple avec les élèves
from django.shortcuts import render
from django.db.models import Sum, Count
from payements.models import Paiement
from classe.models import Classe
from .forms import EleveForm
from django.contrib import messages
from classe.models import Classe
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    
    total_eleves = Eleve.objects.count()
    total_classes = Classe.objects.count()
    total_paiements = Paiement.objects.aggregate(Sum('montant'))['montant__sum'] or 0
    derniers_paiements = Paiement.objects.order_by('-date_paiement')[:5]  # Les 5 derniers paiements

    context = {
        'total_eleves': total_eleves,
        'total_classes': total_classes,
        'total_paiements': total_paiements,
        'derniers_paiements': derniers_paiements,
    }
    return render(request, 'student/dashbord.html', context)


@login_required
def add_student(request):
    erreur = ""
    succes = ""
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            succes = "l'élève à été ajouté(e) avec succès"
            form = EleveForm()
        else:
            erreur = "Assurez-vous que les informations sont correctes. Et n'oublié pas que le matricule est unique pour chaque élève"
    else:
        form = EleveForm()
    return render(request, 'student/add_student.html', {'form': form, "erreur": erreur, "succes": succes})
        
    


@login_required
def student_list(request):
    search_query = request.GET.get('search', '')
    classe_filter = request.GET.get('classe', '')

    # Filtrer les élèves en fonction de la recherche et du filtre
    eleves = Eleve.objects.all()
    classes = Classe.objects.all()

    if search_query:
        eleves = eleves.filter(nom__icontains=search_query)

    if classe_filter:
        eleves = eleves.filter(classe__nom__icontains=classe_filter)

    # Pagination
    paginator = Paginator(eleves, 50)  # 5 élèves par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'student/list_student.html', {'page_obj': page_obj, 'search_query': search_query, 'classe_filter': classe_filter, "classes": classes})
