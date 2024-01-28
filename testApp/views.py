from django.shortcuts import render

# Create your views here.
def countView(request):

    count = int(request.COOKIES.get('count', 0))
    newCount = count+1
    response = render(request, 'testApp/count.html', {'count' : newCount})
    response.set_cookie('count', newCount, max_age=180)

    return response
