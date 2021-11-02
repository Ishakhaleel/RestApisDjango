import random
import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestAPIs.models import User, Advisor
from .serializers import  UserSerializer, AdvisorSerializer, BookingSerializer


# Create your views here.

def Home(request):
    return render(request, "MyHome.html")


@api_view(['POST'])
def addUser(request):
    print(request.data)
    v1 = request.data["name"]
    userObj = User()
    userObj.user_id = v1[:3] + str(random.randint(400, 900))
    userObj.name = v1
    userObj.email = request.data["email"]
    userObj.password = request.data["password"]
    userObj.save()

    return Response(userObj.user_id, status=status.HTTP_200_OK)


@api_view(['POST'])
def addAdvisor(request):
    advisorObj = Advisor()
    try:
        v1 = request.data["name"]

        advisorObj.advisor_id = "ADV" + v1[:3] + str(random.randint(400, 900))
        advisorObj.name = v1
        advisorObj.photo_url = request.data["photo_url"]
        advisorObj.booking_id = "NA"
        advisorObj.booking_time = "NA"
        if len(request.data["name"]) == 0 or len(request.data["photo_url"]) == 0:
            return Response(advisorObj.name, status=status.HTTP_400_BAD_REQUEST)
        advisorObj.save()
    except:
        return Response(advisorObj.name, status=status.HTTP_400_BAD_REQUEST)
    return Response(advisorObj.name, status=status.HTTP_200_OK)


@api_view(["GET"])
def getAdvisors(request, uID):
    advs = Advisor.objects.filter(user_id="NA")
    serializer = AdvisorSerializer(advs, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def bookAdvisor(request, usid, advid):
    bookTime = request.data["booking_time"]
    userId = usid.split('/')[0]
    advisorId = advid.split('/')[0]
    print("usid:", userId)
    print("advid:", advisorId)
    # Check if userid and advisor exists..
    if len(User.objects.filter(user_id=userId)) == 1 and len(Advisor.objects.filter(advisor_id=advisorId)) == 1:
        print("ids exists")
        for a in Advisor.objects.all():
            if a.advisor_id == advisorId:
                a.booking_time = bookTime
                a.booking_id = userId + advisorId + "1234"
                a.user_id = userId
                a.save()

    return Response("", status=status.HTTP_200_OK)


@api_view(["GET"])
def getBookings(request, uId):
    userId = uId.split('/')[0]
    print(userId)
    advs = Advisor.objects.filter(user_id=userId)
    serializer = BookingSerializer(advs, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def login(request):
    try:
        email = request.data["email"]
        password = request.data["password"]
    except:
        return Response("Missing Fields", status=status.HTTP_400_BAD_REQUEST)
    for u in User.objects.all():
        if u.email == email and u.password == password:
            return Response(u.user_id, status=status.HTTP_200_OK)
    else:
        return Response("Incorrect mail/password", status=status.HTTP_401_UNAUTHORIZED)
