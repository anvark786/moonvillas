from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from . models import Gallery
from .forms import ContactForm
from .functions import generate_form_errors
import json 


def index(request):
	
	context = {
		'title': "About",
		"about": "current",		
	}
	return render(request,'web/index.html',context)


def gallery(request):
	all_gallery_images = Gallery.objects.all()
	context = {
		'title': "Gallery",
		"gallery": "current",
		"all_gallery_images":all_gallery_images,

	}
	return render(request,'web/gallery.html',context)


def about_wayanad(request):
	context = {
		'title': "About Wayanad",
		"wayanad": "current",
	}
	return render(request,'web/about_wayanad.html',context)

	
def contact(request):
	if request.method == "POST":        
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			
			response_data = {
				"status" : "true",
				"title" : "Successfully Submitted",
				"message" : "Your Message Successfully Submitted.",
			}
		else:
			message = generate_form_errors(form,formset=False)

			response_data = {
				"status" : "false",
				"stable" : "true",
				"title" : "Form validation error",
				"message" : message
			}
		return HttpResponse(json.dumps(response_data), content_type='application/javascript')
	else:
		form = ContactForm()
		context = {
			'title': "Contact",
			"contact": "current",
			"form": form,
		}
	return render(request,'web/contact.html',context)
