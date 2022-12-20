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
    pass

def project_view(request):
    pass

def personal_information_view(request):
    pass