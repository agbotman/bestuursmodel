from .models import *
from django.forms import Form, ModelForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from django.template import Context, Template
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse_lazy

class FormsetField(LayoutObject):
    """
    Layout object. It renders an entire formset, as though it were a Field.
    """

    #template = "formset_field.html"

    def __init__(self, formset, template="formset_field.html"):

        # crispy_forms/layout.py:302 requires us to have a fields property
        self.fields = []
        self.template = template
        self.formset = formset

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        return render_to_string(self.template,
                                Context({'formset': self.formset,},)
                                )

class FunctieForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FunctieForm, self).__init__(*args, **kwargs)
        self.takenformset = TakenFormSet(*args, **kwargs)
        for f in self.takenformset.forms:
            for field in f.fields.itervalues():
                widg = field.widget
                widg.attrs['class'] = 'input-sm'
        self.helper = FormHelper()
        self.takenformset.helper = TakenFormSetHelperInline()
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
                Fieldset('Functie',
                        Field('naam', css_class="input-sm"),
                        Field('beschrijving', css_class="input-sm", rows=3),
                        Field('afdeling', css_class="input-sm"),
                        Field('functietype', css_class="input-sm"),
                        ),
                        FormsetField(formset=self.takenformset, template="table_inline_formset2.html"),
                ButtonHolder(Submit('submit', 'Submit', css_class='button white'))
                )

    class Meta:
        model = Functie
        
    def is_valid(self):
        if super(FunctieForm, self).is_valid():
            return self.takenformset.is_valid()
        return False
        
    def save(self):
        self.object = super(FunctieForm, self).save()
        self.takenformset.instance = self.object
        t = self.takenformset
        self.takenformset.save()
        return self.object

TakenFormSet = inlineformset_factory(Functie, 
    FunctieTaak.functies.through, 
    can_delete=True,
    extra=1)
    
class TakenFormSetHelperInline(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TakenFormSetHelperInline, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.label_class = 'col-lg-3'
        self.field_class = 'col-lg-9'
        

