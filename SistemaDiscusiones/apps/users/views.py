from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View

class ExtraDataView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'users/extra-data.html')


def LogOut(request):
	logout(request)
	return redirect('/')
