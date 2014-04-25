from django.forms import ModelForm
from models import Suggestion
from django.utils.translation import gettext as _

class SuggestionForm(ModelForm):
	class Meta:
		model = Suggestion
