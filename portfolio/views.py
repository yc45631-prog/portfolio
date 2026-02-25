from django.shortcuts import render , get_object_or_404
from .models import Project, Article

def home(request):
    # Static data extracted from your CV 
    context = {
        'name': 'Christian Yousef',
        'role': 'Informatics Engineer & Data Science Developer',
        'email': 'christianyousef164@gmail.com',
        'phone': '+963 941 768 217',
        'location': 'Tartous, Syria',
        'summary': 'Informatics Engineer specialized in transforming raw data into actionable insights. Expert in building end-to-end Machine Learning pipelines, from data cleaning and exploratory analysis to deploying scalable models via Django. Proven track record in Computer Vision and NLP.',        'education': [
            {
                'degree': 'Bachelor of Informatics Engineering',
                'school': 'Wadi International University',
                'year': '2020 - 2025',
                'details': 'Graduated with Excellent grade (88.20%), GPA 3.41. [cite: 392, 444]'
            }
        ],
        'certifications': [
            'DeepLearning.AI TensorFlow Developer (Coursera)',
            'IBM Data Analyst Professional Certificate (Coursera)',
            'Mini Diploma in Data Analytics (Syrian Youth Assembly)'
        ]
    }
    return render(request, 'portfolio/index.html', context)

def project_list(request):
    projects = Project.objects.all().order_by('-date_created')
    return render(request, 'portfolio/projects.html', {'projects': projects})

def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'portfolio/articles.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, 'portfolio/article_detail.html', {'article': article})