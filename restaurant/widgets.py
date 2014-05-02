from django.forms.util import flatatt 
from django.utils.encoding import StrAndUnicode, force_unicode 
from django.utils.html import conditional_escape 
from django.utils.safestring import mark_safe

class StarsRadioInput(RadioChoiceInput):
    def __init__(self, *args, **kwargs):
        msg = "RadioInput has been deprecated. Use RadioChoiceInput instead."
        warnings.warn(msg, PendingDeprecationWarning, stacklevel=2)
        super(RadioInput, self).__init__(*args, **kwargs)

class StarsRadioFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = RadioChoiceInput


