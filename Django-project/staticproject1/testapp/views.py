from django.shortcuts import render
import datetime

# Create your views here.

def date_time(request):
    dt = datetime.datetime.now()
    h = dt.hour
    msg = "Hello!! Everyone, Good "
    if h < 12:
        msg = msg + "Morning"
    elif h < 16:
        msg = msg + "Afternoon"
    elif h < 21:
        msg = msg + "Evening"
    else:
        msg = msg + "Night"
    dict = {'date': dt, 'msg': msg}
    return render(request, 'testapp/result.html', dict)
    