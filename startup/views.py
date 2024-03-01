from django.shortcuts import render

from startup.models import Newsletter, Review, Partenaire, Magazine, Team, Compositeur


# Create your views here.
def home(request):
    reviews=Review.objects.filter(active=True)
    partenaires=Partenaire.objects.filter(active=True)
    magazines=Magazine.objects.filter(active=True)

    context={
        "reviews":reviews,
        "taille_comment":len(reviews),
        "partenaires":partenaires,
        "taille_partenaire":len(partenaires),
        "magazines":magazines,
        "taille_magazine":len(magazines)

    }
    return render(request,"index.html",context=context)

def about(request):
    teams=Team.objects.all()
    compositeurs=Compositeur.objects.all()
    context = {
        "teams": teams,
        "compositeurs":compositeurs


    }
    return render(request,"about.html",context=context)


def media(request):
    return render(request,"media.html")


def demarche(request):
    return render(request,"demarche.html")


def application(request):
    return render(request,"application.html")


def nouveaute(request):
    return render(request,"nouveaute.html")

def contact(request):
    return render(request,"contact.html")


def newsletter_signup(request):
    message = None

    if request.method == 'POST':
        email = request.POST.get('nf_email')
        if email:
            Newsletter.objects.create(email=email)
            message = "Mail enregistré avec succès."
    reviews = Review.objects.filter(active=True)
    partenaires = Partenaire.objects.filter(active=True)
    magazines = Magazine.objects.filter(active=True)
    context = {
        "reviews": reviews,
        "taille_comment": len(reviews),
        "partenaires": partenaires,
        "taille_partenaire": len(partenaires),
        "magazines": magazines,
        "taille_magazine": len(magazines),
        'message': message,

    }

    return render(request, 'index.html', context)
