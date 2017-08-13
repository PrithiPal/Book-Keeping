
from .models import Author
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_form_author_names_no1(f_name,l_name) :

    all_names =  [(str(x.first_name),str(x.last_name)) for x in Author.objects.all()]
    if (str(f_name),str(l_name)) in all_names:
        raise ValidationError(_("First and Last names cannot be identical"))

def validate_form_username_conventions_no2(value) :

    REGEX = r'^(?=.*[A-z][a-z])(?=.*[0-9]).*$'

    if re.match(REGEX,value) is None :
        raise ValidationError(_("Illegal Username"))
