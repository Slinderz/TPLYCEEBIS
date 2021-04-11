from django.forms.models import ModelForm
from .models import Student, Presence


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'mail',
            'phone',
            'cursus',
            'comment'
        )


class PresenceForm(ModelForm):
    class Meta:
        model = Presence
        fields = (
            'date',
            'reason',
            'isMissing',
            'student',
        )
