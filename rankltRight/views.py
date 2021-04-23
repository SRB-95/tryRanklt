from django.shortcuts import render, redirect
from rankltRight.models import person
from .forms import detail_form

import requests
from bs4 import BeautifulSoup
import os

# Create your views here.
def user_form(request):
    if request.method == "POST":
        form = detail_form(request.POST)
        if form.is_valid():
            name = request.POST['name']
            contact = request.POST['contact']
            url = request.POST['url']
            form_data = person(name=name, contact=contact, url=url)
            form_data.save()
            return redirect('rankltRight:details')
    else:
        form=detail_form(request.POST)
    return render(request, 'user_form.html', {"form": form})

def details(request):
    user_details = person.objects.all()
    # print(user_details)
    return render(request, 'details.html', {"user_details":user_details})

def f_search(request):
    # user_ref = person.objects.all()
    search_query = request.GET.get('s_form', None)
    if len(search_query) > 50:
        user_ref = []
    else:
        user_ref = person.objects.filter(name__icontains=search_query)
    return render(request, 'search.html', {'user_ref':user_ref, "search_query":search_query})


def gi_ajax(request, user_id):
    if user_id:
        user_data = person.objects.get(id=user_id)
        url = user_data.url
        print("URL", url)
        def scrap(myUrl):
            r = requests.get(myUrl)
            soup = BeautifulSoup(r.text, 'html.parser')
            images = soup.find_all('img', class_='ProjectCoverNeue-image-1MZ')
            img_li = []
            for image in images:
                all_images = image['src']
                img_li.append(all_images)
            # print("Image URL: ", img_li)
            return render(request, 'get_image.html', {'img_li': img_li })
        scrap(url)
    return scrap(url)