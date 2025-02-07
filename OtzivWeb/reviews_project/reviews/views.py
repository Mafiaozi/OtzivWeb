from django.shortcuts import render, redirect

reviews = []

def review_list(request):
    if request.method == "POST":
        name = request.POST.get("name")  
        text = request.POST.get("text") 
        if name and text:
            reviews.append({"name": name, "text": text})  
        return redirect("review_list")  

    return render(request, "reviews/review_list.html", {"reviews": reviews})  
