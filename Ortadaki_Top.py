import pygame
from random import randint,choice
from pygame.locals import *
import tkinter as tk
pygame.init()

#yazı tipleri ve büyüklükleri
font=pygame.font.SysFont('Arial',50)
font2=pygame.font.SysFont('Italic',30)
font3=pygame.font.SysFont('Bold',40)
golses=True

biz_buyukluk=90
rakip_buyukluk=90

top_hiz = .5

#oyun alanı için ekran genişliği
ekran=pygame.display.set_mode((600,600))
kaleciRakip = pygame.image.load('foto/kaleciyukarı.png')
kaleciBiz = pygame.image.load('foto/kaleciaşağı.png')

pygame.display.set_caption('Yükleniyor')

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        pygame.transform.scale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('foto/cakma_arkaplan.jpg', [0,100])
ekran.fill((0,0,0))
boyut=60
pygame.mixer.music.load('ses/taraftar.mp3')
boing=pygame.mixer.Sound('ses/boing.mp3')
ses_gol=pygame.mixer.Sound('ses/gol.mp3')
xyapımcı=50
adet=0
pygame.mixer.music.play()
def yukleniyor():
    global boyut,xyapımcı,adet
    if boyut<=350:
        ekran.fill((0,0,0))
        ekran.blit(font2.render("Yapımcı : CanÜstün",True,(randint(0,255),randint(0,255),randint(0,255))),(xyapımcı,0))
        ekran.blit(font.render(" Ortadaki Top !",True,(255,255,255)),(150,30))
        ekran.blit(BackGround.image, BackGround.rect)
        xyapımcı+=0.6
        if adet==4:
            adet=0
        ekran.blit(font2.render(f"Yükleniyor {adet*' . '}",True,(255,150,255)),(240,500))
        boyut+=0.3
        adet+=1
        pygame.draw.rect(ekran,(255,255,255),pygame.Rect(140,530,boyut,4))
        pygame.display.update()
        pygame.time.wait(3)
        yukleniyor()

yukleniyor()
pygame.display.update()
pygame.time.wait(1000)

uzaklık_sekliBiz,uzaklık_sekliRakip=135,135

BackGround = Background('foto/cakma_arkaplan.png', [0,0])

#skor işlemleri
bizSkor,rakipSkor=0,0
y_rastgele=randint(150,450)
x_rastgele=randint(100,500)

#kaleci işlemleri
x,xR=260,260 #konumları
Rakiphiz,Bizhiz=1,1#hareketlilikleri

#topun konumuna etki edenler
sag_sol=0
topunXi=randint(300,400)
topunYsi,eksi_arti=300,0
tek_sefer=True

class gucler:

 def kaleci_buyut(self,top_hangi_yonde):
  global biz_buyukluk,rakip_buyukluk,uzaklık_sekliRakip,uzaklık_sekliBiz,top_hiz

  if top_hangi_yonde==-top_hiz:
   uzaklık_sekliBiz=152
   biz_buyukluk=150

  else:
   uzaklık_sekliRakip=152
   rakip_buyukluk=150

 def gol_arttirma(self,top_hangi_yonde):
  global bizSkor,rakipSkor,top_hiz
  if top_hangi_yonde==-top_hiz:
   bizSkor+=1
   
  else:rakipSkor+=1

 def kaleci_hizi(self,top_hangi_yonde):
  global Rakiphiz,Bizhiz,top_hiz

  if top_hangi_yonde==-top_hiz:
   Bizhiz=2.4

  else:Rakiphiz=2.4

 def kaleci_hizlanma(self,top_hangi_yonde):
  global Rakiphiz,Bizhiz,top_hiz
  if top_hangi_yonde==-top_hiz:
   Bizhiz=1.3

  else:Rakiphiz=1.3

 def kaleci_buyutme(self,top_hangi_yonde):
  global biz_buyukluk,rakip_buyukluk,uzaklık_sekliRakip,uzaklık_sekliBiz,top_hiz

  if top_hangi_yonde==-top_hiz:
   uzaklık_sekliBiz=71
   biz_buyukluk=70
   
  else:
   uzaklık_sekliRakip=72
   rakip_buyukluk=70

guclenme=gucler()

def sifirla(): #sıfırlama işlemleri
 global x,asagi_yukari,tek_sefer,topunYsi,eksi_arti,topunXi,xR,ekran
 global y_rastgele,x_rastgele,biz_buyukluk,rakip_buyukluk,uzaklık_sekliBBiz,uzaklık_sekliRakip
 global Rakiphiz,Bizhiz,sag_sol

 y_rastgele=randint(150,450)
 x_rastgele=randint(100,500)
 sag_sol=0

 Rakiphiz,Bizhiz=1,1
 ekran.fill((0,0,0))

 tek_sefer=True
 biz_buyukluk,rakip_buyukluk=90,90
 uzaklık_sekliBiz,uzaklık_sekliRakip=135,135
 
 #kaleci konumları
 x,xR=260,260

 #topun konumuna etki edenler
 topunXi=randint(300,400)
 topunYsi,eksi_arti=300,0

calis=True
pygame.display.set_caption('Kafa Topu 1 Buçuk')
while calis:
 kaleciRakip = pygame.transform.scale(kaleciRakip, (rakip_buyukluk, 50))
 kaleciBiz = pygame.transform.scale(kaleciBiz, (biz_buyukluk, 50))
 
 #top ilk aşağı mı, yukarı mı gidicek (rastgele) ayarlaması
 if tek_sefer:
  tek_sefer=False
  eksi_arti=top_hiz

  if randint(1,2)==2:
   eksi_arti=-top_hiz

 #çıkış tuşu basıldımı kontrol
 for olay in pygame.event.get():
  if olay.type==pygame.QUIT:
   calis=False

 #tuş tıklama ve kaleci hareket işlemleri
 keys=pygame.key.get_pressed()

 if keys[pygame.K_LEFT] and x>=10:x-=Bizhiz
 if keys[pygame.K_RIGHT] and x<=500:x+=Bizhiz
 if keys[pygame.K_a] and xR>=10:xR-=Rakiphiz
 if keys[pygame.K_d] and xR<=500:xR+=Rakiphiz

 #arkaplan rengi
 ekran.fill((0,0,0))
 ekran.blit(pygame.transform.scale(BackGround.image, (600,600)), (0, 0))
 ekran.blit(kaleciRakip, [xR, 50])
 ekran.blit(kaleciBiz, [x,500])
 
 #topun rengi, konumu ve boyutu
 pygame.draw.circle(ekran,(255,0,0),(topunXi,topunYsi),10)
 topunYsi+=eksi_arti
 topunXi+=sag_sol

 if topunXi>=570:
   sag_sol=-top_hiz

 elif topunXi<=10:
   sag_sol=top_hiz

 #top kaleciler ile aynı konumdaysa topu rakibe göndermesi için işlemler
 if topunYsi==104.0 and topunXi>xR-15 and topunXi<xR+uzaklık_sekliRakip:
  boing.play()
  eksi_arti=top_hiz
  sag_sol=choice([3,5,-6,-5,0,-1,2,-3])
 
 elif topunYsi==490.0 and topunXi>x-15 and topunXi<x+uzaklık_sekliBiz:
  boing.play()
  eksi_arti=-top_hiz
  sag_sol=choice([3,5,-6,-5,0,-1,2,-3])

 #güc topu
 pygame.draw.circle(ekran,(255,25,255),(x_rastgele,y_rastgele),12)

 if topunYsi<y_rastgele+30 and topunYsi>y_rastgele-30 and topunXi==x_rastgele:
     y_rastgele=randint(150,450)
     x_rastgele=randint(100,500)
     hangi_guc=randint(1,5)

     if hangi_guc==1:guclenme.kaleci_buyut(eksi_arti)
     elif hangi_guc==2:guclenme.gol_arttirma(eksi_arti)
     elif hangi_guc==3:guclenme.kaleci_hizi(eksi_arti)
     elif hangi_guc==4:guclenme.kaleci_buyutme(eksi_arti)
     else:guclenme.kaleci_hizlanma(eksi_arti)

 #kazan kaybet olayları
 if topunYsi>=590:
  rakipSkor+=1
  ses_gol.play()
  pygame.time.wait(1700)
  sifirla()
     
 elif topunYsi<=10:
  bizSkor+=1
  ses_gol.play()
  pygame.time.wait(1700)
  sifirla()

 ekran.blit(font3.render((str(bizSkor)),True,(250,250,250)),(300,570))
 ekran.blit(font3.render((str(rakipSkor)),True,(250,250,250)),(300,10))

 #ekranı sürekli güncelle
 pygame.display.update()
