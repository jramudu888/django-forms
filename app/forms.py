import email
from msilib import gen_uuid
from django import forms
g=[['MALE','male'],('FEMALE','female')]
c=[['PYTHON',"PYTHON"],('Django','Django'),['SQL','SQL']]
class SchoolForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField(max_length=100)

class SampleForm(forms.Form):
    email=forms.EmailField()
    url=forms.URLField()
    date=forms.DateField()
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':5,'rows':5}))
