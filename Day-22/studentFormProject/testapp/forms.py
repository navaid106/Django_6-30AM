from django import forms

class StudentForm(forms.Form):
    # Name, Email, Description
    # Name --> text
    # Email --> email
    # Description --> textarea

    # Single line text input
    name = forms.CharField(label="Full Name",
                           
        widget=forms.TextInput(attrs={'placeholder':'Enter your name'})
    )

    # Single line field
    email = forms.EmailField(label="Email",
        widget=forms.EmailInput(attrs={'placeholder':'Enter your email'})       
    
    )

    # Multi-line text area input

    description = forms.CharField(label="About yourself",
        widget=forms.Textarea(attrs={'placeholder':'Write about yourself...'})
    )