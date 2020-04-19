from django import forms


class NameForm(forms.Form):
    cities = [
        ('at', 'Austia'),
        ('uk', 'England'),
        ('blr', 'Bangalore'),
    ]
    Name = forms.CharField(label='Your name', max_length=100)
    Company = forms.CharField()
    City = forms.ChoiceField(choices=cities)
    Experience = forms.FloatField()
    CCTC = forms.FloatField()
    ECTC = forms.FloatField()
    WFH = forms.BooleanField(required=False)
