from django.shortcuts import render, redirect

reviews = []

def review_list(request):
    if request.method == "POST":
        name = request.POST.get("name")  # Получаем имя пользователя из формы
        text = request.POST.get("text")  # Получаем текст отзыва из формы
        if name and text:
            reviews.append({"name": name, "text": text})  # Добавляем отзыв в список
        return redirect("review_list")  # Перенаправляем на ту же страницу

    return render(request, "reviews/review_list.html", {"reviews": reviews})  # Отображаем страницу с отзывами
