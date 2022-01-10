from django.shortcuts import render


def index(request):
	context = {
		'title': "Home",
		"home": "current",
	}
	return render(request,'web/index.html',context)


def about(request):
	context = {
		"title": "About",
		"about":"current",		
	}
	return render(request,'web/about.html',context)


def gallery(request):
	context = {
		'title': "Gallery",
		"gallery": "current",
	}
	return render(request,'web/gallery.html',context)



def about_wayanad(request):
	context = {
		'title': "About Wayanad",
		"wayanad": "current",
	}
	return render(request,'web/about_wayanad.html',context)


	
def contact(request):
	context = {
		'title': "Contact",
		"contact": "current",
	}
	return render(request,'web/contact.html',context)
