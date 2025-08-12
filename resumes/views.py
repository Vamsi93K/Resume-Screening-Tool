from django.shortcuts import render
from .models import Resume
from .utils.parser import extract_text
from .utils.scorer import score_resume 
from keybert import KeyBERT
from .models import JobDescription
from .models import RoleKeywordProfile
from django.http import JsonResponse

from django.shortcuts import render, redirect
from .models import Resume
from .utils.parser import extract_text
from .utils.scorer import score_resume

def bulk_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('resumes')
        keywords = request.POST.getlist('keywords')

        uploaded_ids = []

        for f in files:
            resume = Resume.objects.create(file=f)
            resume.save()  # Ensure file is saved before accessing path

            try:
                text = extract_text(resume.file.path)
                score, matched = score_resume(text, keywords)
                resume.score = score
                resume.matched_keywords = matched
                resume.save()
                uploaded_ids.append(resume.id)
            except Exception as e:
                print(f"Error processing {resume.file.name}: {e}")

        request.session['uploaded_ids'] = uploaded_ids
        return redirect('results')

    return render(request, 'resumes/bulk_upload.html')

def results_view(request):
    uploaded_ids = request.session.get('uploaded_ids', [])
    resumes = Resume.objects.filter(id__in=uploaded_ids)
    return render(request, 'resumes/results.html', {'resumes': resumes})

def leaderboard(request):
    resumes = Resume.objects.order_by('-score')
    return render(request, 'resumes/leaderboard.html', {'resumes': resumes})

def extract_keywords_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        kw_model = KeyBERT()
        keywords = [kw[0] for kw in kw_model.extract_keywords(text, top_n=10)]
        jd = JobDescription.objects.create(title=title, text=text, extracted_keywords=keywords)
        return render(request, 'resumes/keywords_result.html', {'keywords': keywords})
    return render(request, 'resumes/jd_input.html')

def save_role_profile(request):
    if request.method == 'POST':
        role = request.POST['role']
        keywords = request.POST.getlist('keywords')
        RoleKeywordProfile.objects.update_or_create(role_name=role, defaults={'keywords': keywords})
    return render(request, 'resumes/save_profile.html')

def load_role_keywords(request, role_name):
    profile = RoleKeywordProfile.objects.get(role_name=role_name)
    return JsonResponse({'keywords': profile.keywords})

def fetch_from_email():
    # Use imaplib or Gmail API to fetch attachments
    # Save resumes and trigger parsing
    pass
def dashboard(request):
    resumes = Resume.objects.all()
    return render(request, 'dashboard.html', {'resumes': resumes})

from django.shortcuts import redirect
from .models import Resume

def clear_resumes(request):
    Resume.objects.all().delete()
    return redirect('dashboard')