from django.shortcuts import render

# Create your views here.
def language_view(request):
    context = {
        "first_language": {
            'value': 'Persian',
            'rate': '100%'
        },
        "second_language": {
            'value': 'English',
            'rate': '50%'
        },
        'third_language': {
            'value': 'Arabic',
            'rate': '20%'
        }
    }
    return render(request, 'website/language.html', context)

def education_view(request):
    context = {
        'high_school': 'Sampad',
        'university': 'Sharif',
    }
    return render(request, 'website/education.html', context)

def skills_view(request):
    return render(request, 'website/skills.html')

def project_view(request):
    context = {
        "setare_sim": 'setaresim.com',
        'setare_aval': 'setareaval.com',
    }
    return render(request, 'website/projects.html', context)

def personal_information_view(request):
    context = {
        'living': 'Mazandaran, chalus',
        'phone_number': '09338633187',
        'gmail': 'javad.alghosi7904@gmail.com'
    }
    return render(request, 'website/personal-info.html', context)








