from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from MTV.models import Car,Manager,OptionA,OptionB,OptionC,OptionD,MyCar
import random
from django.contrib.auth.models import User
import time


# Create your views here.


def Login (request):
  
  return render(request, "MTV/login.html")

def Main (request):

  Car_List = Car.objects.all().order_by()

  return render(request, "MTV/main.html",{"Car_List" : Car_List})


def Search_reset (request, keyword):
  str = keyword
  result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str)
  count = Car.objects.filter(name__icontains=str).count() | Car.objects.filter(owner__icontains=str).count()
  return render(request, "MTV/search.html",{"Car_List" : result, "Keyword" : str, "Count" : count})

def Create (request):
  man1 = Manager.objects.get(name="유영현")
  man2 = Manager.objects.get(name="백승혁")
  man3 = Manager.objects.get(name="이재한")
  man4 = Manager.objects.get(name="정다운")
  man5 = Manager.objects.get(name="유대선")
  
  
  list=[]
  list.append(Car(name="올 뉴 아반떼 CN7", age="2020.09",model="1.6 인스퍼레이션", price=2340, kilo=28395, owner="백승혁",img="car1",price_score=98, quality_score=94,manager=man1))
  list.append(Car(name="아반떼 AD7", age="2018.07",model="1.6 GDi 밸류플러스", price=1360, kilo=32607, owner="정다운",img="car2",price_score=97, quality_score=92,manager=man1))
  list.append(Car(name="GV70", age="2020.12", model="2.5T AWD 기본형", price=6350, kilo=17043, owner="유영현",img="car3",price_score=99, quality_score=91,manager=man2))
  list.append(Car(name="더 올 뉴 G80", age="2020.10", model="2.5 2WD 기본형", price=5000, kilo=28099, owner="이재한",img="car4",price_score=90, quality_score=92,manager=man2))
  list.append(Car(name="더 뉴 모닝", age="2016.11", model="가솔린 럭셔리", price=680, kilo=83780, owner="익명",img="car5",price_score=89, quality_score=87,manager=man3))
  list.append(Car(name="팰리세이드", model="2.2 디젤 AWD 캘리그래피", age="2020.05", kilo=34232, price=4300,  owner="익명",img="car6",price_score=97, quality_score=94,manager=man3))
  list.append(Car(name="더 뉴 카니발", model="디젤 프레스티지", age="2018.06", kilo=78958, price=2350,  owner="익명",img="car7",price_score=98, quality_score=94,manager=man4))
  list.append(Car(name="더 올 뉴 투싼", model="1.6T AWD 인스퍼레이션", age="2020.10", kilo=15937, price=3580,  owner="익명",img="car8",price_score=92, quality_score=92,manager=man4))
  list.append(Car(name="셀토스", model="1.6 디젤 2WD 시그니처", age="2021.01", kilo=16925, price=2630,  owner="익명",img="car9",price_score=94, quality_score=90,manager=man5))
  list.append(Car(name="더 뉴 소렌토", model="디젤 R2.0 2WD 프레스티지", age="2018.07", kilo=41340, price=2190,  owner="익명",img="car10",price_score=92, quality_score=91,manager=man5))
  list.append(Car(name="티볼리 에어", model="가솔린 2WD RX", age="2017.11", kilo=53507, price=1400,  owner="익명",img="car11",price_score=88, quality_score=98,manager=man1))
  list.append(Car(name="더 뉴 그랜저 IG", model="3.3 익스클루시브", age="2020.02", kilo=42204, price=3100,  owner="익명",img="car12",price_score=99, quality_score=84,manager=man2))
  list.append(Car(name="LF 소나타 뉴 라이즈", model="2.0 CVVL 모던", age="2018.08", kilo=54796, price=1830,  owner="익명",img="car13",price_score=97, quality_score=90,manager=man3))
  list.append(Car(name="올 뉴 K3", model="1.6 프레스티지", age="2018.07", kilo=31119, price=1640,  owner="익명",img="car14",price_score=92, quality_score=99,manager=man4))
  list.append(Car(name="올 뉴 K5", model="2.0 시그니처", age="2019.12", kilo=42654, price=2790,  owner="익명",img="car15",price_score=91, quality_score=91,manager=man5))
  
  
  
  cnt = Car.objects.count()
  if cnt == 0: 
    for item in list:
      item.save()
    print("create Success")
  else:
    print("Data already exist")
  return HttpResponseRedirect(reverse('MTV:main')) 

def Delete (request):
  list = Car.objects.all()
  cnt = Car.objects.count()
  if cnt != 0:
    for i in list:
      i.delete()
    print("delete all success")
  else:
    print("Table is already empty")
  return HttpResponseRedirect(reverse('MTV:main'))

def Create_Opta(request):
  cnt = OptionA.objects.count()
  bol = [True, False]
  

    
  if cnt == 0:
    car_list = Car.objects.all()
    for car in car_list:
      
      index = []
      for i in range (10):
         index.append(round(random.random()))
         
      optA = OptionA(Car=car, opt1=bol[index[0]], opt2=bol[index[1]], opt3=bol[index[2]], opt4=bol[index[3]]
                     ,opt5=bol[index[4]],opt6=bol[index[5]],opt7=bol[index[6]],opt8=bol[index[7]]
                     ,opt9=bol[index[8]],opt10=bol[index[9]])
      
      optA.save()
  return HttpResponseRedirect(reverse('MTV:main')) 

def Create_Optb(request):
  cnt = OptionB.objects.count()
  bol = [True, False]
  

    
  if cnt == 0:
    car_list = Car.objects.all()
    for car in car_list:
      
      index = []
      for i in range (12):
         index.append(round(random.random()))
         
      optB = OptionB(Car=car, opt1=bol[index[0]], opt2=bol[index[1]], opt3=bol[index[2]], opt4=bol[index[3]]
                     ,opt5=bol[index[4]],opt6=bol[index[5]],opt7=bol[index[6]],opt8=bol[index[7]]
                     ,opt9=bol[index[8]],opt10=bol[index[9]],opt11=bol[index[10]],opt12=bol[index[11]])
      
      optB.save()
  return HttpResponseRedirect(reverse('MTV:main')) 

def Create_Optc(request):
  cnt = OptionC.objects.count()
  bol = [True, False]
  

    
  if cnt == 0:
    car_list = Car.objects.all()
    for car in car_list:
      
      index = []
      for i in range (10):
         index.append(round(random.random()))
         
      optC = OptionC(Car=car, opt1=bol[index[0]], opt2=bol[index[1]], opt3=bol[index[2]], opt4=bol[index[3]]
                     ,opt5=bol[index[4]],opt6=bol[index[5]],opt7=bol[index[6]],opt8=bol[index[7]]
                     ,opt9=bol[index[8]],opt10=bol[index[9]])
      
      optC.save()
  return HttpResponseRedirect(reverse('MTV:main')) 

def Create_Optd(request):
  cnt = OptionD.objects.count()
  bol = [True, False]
  

    
  if cnt == 0:
    car_list = Car.objects.all()
    for car in car_list:
      
      index = []
      for i in range (10):
         index.append(round(random.random()))
         
      optD = OptionD(Car=car, opt1=bol[index[0]], opt2=bol[index[1]], opt3=bol[index[2]], opt4=bol[index[3]]
                     ,opt5=bol[index[4]],opt6=bol[index[5]],opt7=bol[index[6]],opt8=bol[index[7]]
                     ,opt9=bol[index[8]],opt10=bol[index[9]])
      
      optD.save()
  return HttpResponseRedirect(reverse('MTV:main')) 



def Detail (request, Car_id):
  A_list = ["블랙박스", "하이패스","전동 사이드 미러","파노라마 썬 루프", "썬 루프", "열선 핸들", "전동 트렁크", "알루미늄 휠","크롬 휠","오토라이트"]
  B_list = ["전방 카메라", "후방 카메라","스마트 키","크루즈 컨트롤","스마트 크루즈 컨트롤","내비게이션","헤드업 디스플레이","어라운드 뷰 모니터링 시스템","에어 서스펜션","무선 충전 시스템","풀 오토 에어컨","블루투스"]
  C_list = ["경사로 저속 주행장치","차선 이탈 경보장치","자동 긴급 제동시스템","차체 자세 제어장치","주행 조향 보조시스템","급 제동 경보장치","후측방 충돌 회피 지원시스템","타이어 공기입 경보 장치","운전석 에어백","조수석 에어백"]
  D_list = ["가죽 시트","전동 안마시트", "메모리 시트","운전석 전동 시트","운전석 통풍 시트","운전석 열선 시트","조수석 전동 시트","조수석 열선 시트","조수석 통풍 시트","뒷자석 폴딩 시트"]
  car = Car.objects.get(id=Car_id)
  manager = Manager.objects.get(id=car.manager.id) 
  A_con = []
  B_con = []
  C_con = []
  D_con = []
  if request.user.is_authenticated:
    active = MyCar.objects.filter(mycar=car, car_user=request.user)
  else:
    active = request.user.is_authenticated
  

  opt_A = OptionA.objects.filter(Car=car).values_list()
  opt_A = list(opt_A)
  opt_A = list(opt_A[0])
  del opt_A[:2]
  for i in range(len(opt_A)):
    context = {"name" : A_list[i], "value" : opt_A[i]}
    A_con.append(context)
    
  opt_B = OptionB.objects.filter(Car=car).values_list()
  opt_B = list(opt_B)
  opt_B = list(opt_B[0])
  del opt_B[:2]
  for i in range(len(opt_B)):
    context = {"name" : B_list[i], "value" : opt_B[i]}
    B_con.append(context)
    
  opt_C = OptionC.objects.filter(Car=car).values_list()
  opt_C = list(opt_C)
  opt_C = list(opt_C[0])
  del opt_C[:2]
  for i in range(len(opt_C)):
    context = {"name" : C_list[i], "value" : opt_C[i]}
    C_con.append(context)
    
  opt_D = OptionD.objects.filter(Car=car).values_list()
  opt_D = list(opt_D)
  opt_D = list(opt_D[0])
  del opt_D[:2]
  for i in range(len(opt_D)):
    context = {"name" : D_list[i], "value" : opt_D[i]}
    D_con.append(context)

  return render(request, 'MTV/detail.html', {'Car' : car, 'Manager' : manager,
  "opt_A" : A_con, "opt_B" : B_con, "opt_C" : C_con, "opt_D" : D_con, "active" : active})
  

def Sort_Main(request, man):
  car = ""
  check = ""
  if man == 'ageup':
    car = Car.objects.all().order_by('-age')
    check = "ageup"
  elif man == 'agedown':
    car = Car.objects.all().order_by('age')
    check = "agedown"
  elif man == 'kiloup':
    car = Car.objects.all().order_by('-kilo')
    check = "kiloup"
  elif man == 'kilodown':
    car = Car.objects.all().order_by('kilo')
    check = "kilodown"
  elif man == 'priceup':
    car = Car.objects.all().order_by('-price')
    check = "priceup"
  elif man == 'pricedown':
    car = Car.objects.all().order_by('price')
    check = "pricedown"
  return render(request, "MTV/main.html",{"Car_List" : car, "check" : check})

def Sort_Search(request, man, keyword):
  str = keyword
  count = Car.objects.filter(name__icontains=str).count() | Car.objects.filter(owner__icontains=str).count()
  
  if man == 'ageup':
    result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str).order_by('-age')
    check = "ageup"
  elif man == 'agedown':
    result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str).order_by('age')
    check = "agedown"
  elif man == 'kiloup':
    result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str).order_by('-kilo')
    check = "kiloup"
  elif man == 'kilodown':
    result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str).order_by('kilo')
    check = "kilodown"
  elif man == 'priceup':
    result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str).order_by('-price')
    check = "priceup"
  elif man == 'pricedown':
    result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str).order_by('price')
    check = "pricedown"
  return render(request, "MTV/search.html",{"Car_List" : result, "Keyword" : str, "check" : check, "Count" : count})
  
def Search (request):
  str = request.POST['keyword']
  result = Car.objects.filter(name__icontains=str) | Car.objects.filter(owner__icontains=str)
  count = Car.objects.filter(name__icontains=str).count() | Car.objects.filter(owner__icontains=str).count()
  print(result)
  return render(request, "MTV/search.html",{"Car_List" : result, "Keyword" : str, "Count" : count})

def Mycar (request):
  result = MyCar.objects.filter(car_user=request.user)
  count = MyCar.objects.filter(car_user=request.user).count()
  return render(request, "MTV/mycar.html",{"Car_List" : result, "Count" : count})

def Mycar_Create (request, car):
  mycar = Car.objects.get(id=car)
  Car_id = mycar.id
  myuser = request.user
  Mycar = MyCar(mycar=mycar,car_user=myuser)
  Mycar.save()
  return Detail(request, Car_id)

def Mycar_Delete (request, car):
  mycar = Car.objects.get(id=car)
  Car_id = mycar.id
  myuser = request.user
  Mycar = MyCar.objects.filter(mycar=mycar,car_user=myuser)
  Mycar.delete()
  return Detail(request, Car_id)