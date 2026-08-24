from django import forms


class NIDCheckForm(forms.Form):
    nid_number = forms.CharField(
        label="NID Card Number",
        max_length=20,
        min_length=10,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your NID number",
                "autocomplete": "off",
                "inputmode": "numeric",
            }
        ),
    )

    def clean_nid_number(self):
        nid = self.cleaned_data["nid_number"].strip()

        if not nid.isdigit():
            raise forms.ValidationError(
                "NID number must contain digits only."
            )

        return nid


    