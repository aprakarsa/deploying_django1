from django import forms 

from .models import Instagram


class InstagramForm(forms.ModelForm):
	class Meta:
		model = Instagram
		fields = [
			'nama_depan',
			'nama_belakang',
			'username',
		]

		widgets = {
			'nama_depan': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'isi dengan nama depan',
				}
			),
			'nama_belakang': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'isi dengan nama belakang',
				}
			),
			'username': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'isi dengan username',
				}
			),
		}
