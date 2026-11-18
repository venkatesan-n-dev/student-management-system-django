from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = [
            'name',
            'email',
            'age',
            'course',
            'marks'
        ]

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter student name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email'
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter age'
                }
            ),

            'course': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter course'
                }
            ),

            'marks': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter marks',
                    'step': '0.01'
                }
            ),
        }