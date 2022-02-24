from django import forms
from .models import Project
from users.models import Member

# class ProjectForm(forms.ModelForm):

#     discription = forms.CharField(
#                     required=False,
#                     widget=forms.Textarea(
#                         attrs={
#                             'class': 'form-control',
#                             'rows': '3',
#                         }
#                     )
#                 )

#     members = []
#     admin_list = []
    
#     data = Member.objects.all()
#     for i in data:
#         members.append(i.user_name)
#         if i.role == 'leader':
#             admin_list.append(i.user_name)

#     names = [(x, x) for x in members]
#     admin_list = [(x, x) for x in admin_list]

#     team = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=names)
#     admin = forms.ChoiceField(choices=admin_list)

#     class Meta:
#         model = Project
#         fields = ['title', 'discription', 'admin', 'team']

class ProjectForm(forms.ModelForm):

    discription = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            'class': 'form-control',
                            'rows': '3',
                        }
                    )
                )

    members = []
    admin_list = []
    
    data = Member.objects.all()
    for i in data:
        members.append(i.user_name)
        if i.role == 'leader':
            admin_list.append(i.user_name)

    names = [(x, x) for x in members]
    admin_list = [(x, x) for x in admin_list]

    team = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=names)
    admin = forms.ChoiceField(choices=admin_list)

    class Meta:
        model = Project
        fields = ['title', 'discription', 'admin', 'team']