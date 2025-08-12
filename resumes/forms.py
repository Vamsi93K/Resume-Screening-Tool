from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    keyword_list = forms.CharField(
        required=False,
        help_text="Enter comma-separated keywords (e.g. Python, SQL, Tableau)",
        widget=forms.TextInput(attrs={'placeholder': 'Python, SQL, Tableau'})
    )

    class Meta:
        model = Resume
        fields = ['file_upload']