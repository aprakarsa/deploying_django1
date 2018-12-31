# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render

from .models import Instagram
from .forms import InstagramForm


def update(request, pk):
	akun_update = Instagram.objects.get(id=pk)
	data_update = {
		'nama_depan': akun_update.nama_depan,
		'nama_belakang': akun_update.nama_belakang,
		'username': akun_update.username,
	}
	akun_form = InstagramForm(request.POST or None, initial=data_update, instance=akun_update)
	
	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()
		return redirect('blog:list')

	context = {
		'page_title': 'Update List',
		'akun_form': akun_form,
	}

	return render(request, 'blog/create.html', context)


def delete(request, pk):
	Instagram.objects.filter(id=pk).delete()
	return redirect('blog:list')


def create(request):
	akun_form = InstagramForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('blog:list')

	context = {
		'page_title': 'Tambah List',
		'akun_form': akun_form,
	}

	return render(request, 'blog/create.html', context)


def list(request):
	akun = Instagram.objects.all()

	context = {
			'page_title': 'Social Media List',
			'akun_all': akun,
	}

	return render(request, 'blog/list.html', context)
