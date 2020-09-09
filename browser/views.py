from django.shortcuts import render


def homePage(request):

    return render(request, 'index.html', {
        "app_url": "home",
    })


def contact(request):

    return render(request,  "contact.html", {
        "app_url": "lien-he",
    })


def post(request):

    return render(request,  "blog.html", {
        "app_url": "lien-he",
    })


def thuoc(request):

    return render(request,  "shop-single.html", {
        "app_url": "thuoc",
    })


def postDetail(request):

    return render(request,  "blog-single.html", {
        "app_url": "blog-single",
    })
