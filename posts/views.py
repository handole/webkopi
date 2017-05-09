# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
from .forms import PostForm
from .models import Post


# Create your views here.
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
        # messages success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Messages")

	context = {
    	"form": form,
    }
	return render(request, "post_form.html", context)

def post_detail(request, slug=None): # retrieve
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
    #share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance":instance,
    #    "share_string": share_string,
	}
	return render(request, "post_detail.html", context)


def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
		).distinct()

	paginator = Paginator(queryset_list , 6) # Show 6 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
	}
	return render(request, "post_list.html", context)
	# return HttpResponse("<h1>List!</h1>")


def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
        # messages success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request, "post_form.html", context)


def post_delete(request):
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")
