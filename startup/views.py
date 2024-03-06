from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from startup.models import Newsletter, Review, Partenaire, Magazine, Team, Compositeur
from startup.utils.maisender import sendMail


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


def contact_send(request):
    message=None
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')
        file = request.POST.get('email')
        print(nom,prenom,email,sujet,message)
        if request.FILES['file']:
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            sendMail(["guedjegedeon03@gmail.com","contacts@workinmusic.fr"], 'mails/contact_us.html',f"Message envoyé par {prenom} {nom} - {sujet}",{
                "nom":nom,
                "prenom":prenom,
                "sujet":sujet,
                "message":message,
                "url":uploaded_file_url

            })
        else:
            sendMail(["guedjegedeon03@gmail.com","contacts@workinmusic.fr"], 'mails/contact_us.html', f"Message envoyé par {prenom} {nom} - {sujet}", {
                "nom": nom,
                "prenom": prenom,
                "sujet": sujet,
                "message": message,


            })


        message = "Message envoyé avec succès.Notre équipe vous contactera sous peu."
        return render(request, 'contact.html',{"message":message} )
    else:
        return render(request, 'contact.html',)

def newsletter_signup(request):
    message = None

    if request.method == 'POST':
        email = request.POST.get('nf_email')
        if email:
            Newsletter.objects.create(email=email)
            sendMail([email],'mails/newsletter_sign.html')
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


def mention(request):
    return render(request, 'mention.html')

def politique(request):
    return render(request, 'politique.html')

