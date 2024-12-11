from django.shortcuts import render

# Create your views here.

def portal(request):
    return render(request, 'testapp/home.html')

def movies(request):
    news1 = 'Kamal sir is going to host Bigg Boss 5'
    news2 = 'Beast last schedule, running up'
    news3 = 'Bigg Boss fame Sandy ready to haunt in silver screen'
    news4 = 'Doctor movie, hit or flap?'
    news5 = "Friends gathered in yuvan's birthday"
    dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5':news5}
    return render(request, 'testapp/movies.html', dict)

def sports(request):
    news1 = 'CSK qualified for finals'
    news2 = 'Kohli ended his captainship for RCB'
    news3 = 'Who is the opponent for CSK? DC vs KKR'
    news4 = 'BCCL announces the INDIAN TEAM Members for T20'
    news5 = "Will MSD's captaincy leed the team to win IPL"
    dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5':news5}
    return render(request, 'testapp/sports.html', dict)

def politics(request):
    news1 = 'VMI won 110 of 169 in local body election'
    news2 = 'MNM needs to get a strong foundation to lead'
    news3 = 'CM of TN has reduced his Convoy vehicles to reduce the traffic'
    news4 = 'The Prime Minister of Netherland met with a Tamil Youtuber in a public park'
    news5 = 'Who goes to be a next Prime Minister of INDIA'
    dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5':news5}
    return render(request, 'testapp/politics.html', dict)