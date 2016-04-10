# -*- coding: UTF-8 -*-
import pygame, sys, random
from pokemonFx import *
pygame.init()
end=0
types=['','Combat','Dragon','Eau','Electrik','Feu','Glace','Insecte','Normal','Plante','Poison','Psy','Roche','Sol','Spectre','Vol','Acier']
save=eval(open('save.sav','r').readline())
size=width,height=910,512
black=0,0,0
white=255,255,255
blue=0,25,136
green=86,163,89
fighttext=[('Un ','sid',' sauvage apparait !'),('','mid',' ! Go !'),['Attaque','Sac','Pokemon','Fuite']]
typemodtext=['in','tres peu ','pas tres ','super ','extremement ']
framecount=0
fighttextcount=-1

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Frozen")

#pygame.mixer.music.load('Autres images\\sons/Battle theme.wav')
#pygame.mixer.music.play(0, 0.0)

wild=[5.0, 109, [0,0,0,0,0,0,1.0,1.0,1.0,1.0], 3, 110, 64, 0, 30, 30, 20, 0]

sid=wild[1]
mid=save[3]
Wmaxpv=pokemon(sid)[3][3]*wild[0]/50+wild[0]+10.0
Wpv=Wmaxpv
Smaxpv=pokemon(mid)[3][3]*save[0]/50+save[0]+10.0
wildim=pygame.image.load("Sprites Pokemons/N°"+str(sid)+"-"+pokemon(sid)[0]+".png").convert_alpha()
selfim=pygame.transform.flip(pygame.image.load("Sprites Pokemons/N°"+str(mid)+"-"+pokemon(mid)[0]+".png").convert_alpha(),True,False)

while not end:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			end=1
	framecount+=1
	if fighttextcount==-1 and framecount>60:
		fighttextcount=0
		framecount=0
		textW1=pygame.font.SysFont('Arial', 20, False, False).render(pokemon(sid)[0], True, black)
		textW2=pygame.font.SysFont('Arial', 20, False, False).render('n. '+str(int(wild[0])), True, black)
		textW3=pygame.font.SysFont('Arial', 20, False, False).render('PV', True, black)
		textS1=pygame.font.SysFont('Arial', 20, False, False).render(pokemon(mid)[0], True, black)
		textS2=pygame.font.SysFont('Arial', 20, False, False).render('n. '+str(int(save[0])), True, black)
		textS3=pygame.font.SysFont('Arial', 20, False, False).render('PV', True, black)
		textS4=pygame.font.SysFont('Arial', 20, False, False).render(str(int(save[2]))+'/'+str(int(Smaxpv)), True, black)
		textS5=pygame.font.SysFont('Arial', 12, False, False).render('exp', True, black)
	if fighttextcount in [0,1]:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[fighttextcount][0]+pokemon(eval(fighttext[fighttextcount][1]))[0]+fighttext[fighttextcount][2], True, black)
	if framecount>20 and fighttextcount==0 and pygame.key.get_pressed()[111]==1:
		fighttextcount+=1
		framecount=0
	if framecount>70 and fighttextcount==1:
		fighttextcount+=1
		submenu=0
		framecount=0
		J=0,0
		LA=0,0
	if fighttextcount==2:
		if submenu==0:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Que doit faire ', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' ?', True, black)
			text2=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][0], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][1], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][2], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][3], True, black)
			if framecount>20 and pygame.key.get_pressed()[111]==1:
				submenu=J[0]+J[1]*2+1
				framecount=0
				J=0,0
				if submenu==1:
					J=LA
			if pygame.key.get_pressed()[100]==1 and J[0]==0:
				J=1,J[1]
			if pygame.key.get_pressed()[113]==1 and J[0]==1:
				J=0,J[1]
			if pygame.key.get_pressed()[115]==1 and J[1]==0:
				J=J[0],1
			if pygame.key.get_pressed()[122]==1 and J[1]==1:
				J=J[0],0
		if submenu==1:
			text2=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[5])[4], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[6])[4], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[7])[4], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[8])[4], True, black)
			text6=pygame.font.SysFont('Arial', 35, False, False).render('PP '+str(save[J[0]+2*J[1]+9])+'/'+str(attaque(save[J[0]+2*J[1]+5])[5]), True, black)
			text7=pygame.font.SysFont('Arial', 35, False, False).render(types[attaque(save[J[0]+2*J[1]+5])[0]], True, black)
			if framecount>20 and pygame.key.get_pressed()[111]==1:
				if save[J[0]+2*J[1]+9]>0:
					paralised=(random.randint(1,4)==1 and save[4][1]==1)
					if paralised or save[4][3]>0 or save[4][4]>0:
						fighttextcount=3.4
						attacked=[1,0]
						framecount=0
					elif random.randint(1,2)==1 and save[4][5]>0:
						fighttextcount=3.5
						attacked=[1,0]
						framecount=0
						alea=random.uniform(0.85,1)
						LA=J
					else:
						fighttextcount=7
						attacked=[0,0]
						framecount=0
						alea=random.uniform(0.85,1)
						critical=0
						typemod=1
						if attaque(save[J[0]+J[1]*2+5])[1]>0:
							if random.randint(1,16)==1:
								critical=1
							typemod=table(attaque(save[J[0]+2*J[1]+5])[0],pokemon(sid)[1])*table(attaque(save[J[0]+2*J[1]+5])[0],pokemon(sid)[2])
						stab=1+(attaque(save[J[0]+2*J[1]+5])[0]==pokemon(mid)[1] or attaque(save[J[0]+2*J[1]+5])[0]==pokemon(mid)[2])*0.5
						effectdo=(random.randint(1,100)<=attaque(save[J[0]+2*J[1]+5])[6])
						save[J[0]+2*J[1]+9]-=1
						LA=J
						effectdone=0
						effect2done=0
						if save[4][5]>0:
							save[4][5]-=1
				else:
					framecount=0
					submenu=1.5
			if pygame.key.get_pressed()[100]==1 and J[0]==0 and save[6+2*J[1]]!=0:
				J=1,J[1]
			if pygame.key.get_pressed()[113]==1 and J[0]==1 and save[5+2*J[1]]!=0:
				J=0,J[1]
			if pygame.key.get_pressed()[115]==1 and J[1]==0 and save[7+J[0]]!=0:
				J=J[0],1
			if pygame.key.get_pressed()[122]==1 and J[1]==1 and save[5+J[0]]!=0:
				J=J[0],0
		if submenu==1.5:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Cette attaque n\'a plus de PP !', True, black)
			if framecount>60:
				submenu=1
		if submenu>=2:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Fonctionalite non disponible.', True, black)
			if framecount>60:
				submenu=0
	if fighttextcount==3:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' utilise '+attaque(save[J[0]+J[1]*2+5])[4]+' !', True, black)
		if framecount in range(60,111) and attaque(save[J[0]+J[1]*2+5])[1]>0:
			Wpv+=-((save[0]*0.4+2)*(pokemon(mid)[3][0]*save[0]/50+5)*save[4][6]*attaque(save[J[0]+J[1]*2+5])[1]/(pokemon(sid)[3][1]*wild[0]/50+5)/wild[2][7]/50+2)*(critical+1)*typemod*stab*alea/50
			if Wpv<1:
				Wpv=0.0
				fighttextcount=4.1
				framecount=0
				if critical or typemod!=1 or (attaque(save[J[0]+J[1]*2+5])[3] in [8,10,12,15,16,18,19,20,21,23,24,25,26,27,28,30,31] and effectdo):
					fighttextcount=3.1
					framecount=0
					prevW2=wild[2][:]
		if framecount==140-(attaque(save[J[0]+J[1]*2+5])[1]==0)*80:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Que doit faire ', True, black)
			text2=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][0], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][1], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][2], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][3], True, black)
			fighttextcount=7
			framecount=0
			submenu=0
			if critical or typemod!=1 or (attaque(save[J[0]+J[1]*2+5])[3]!=0 and effectdo):
				fighttextcount=3.1
				framecount=0
				prevW2=wild[2][:]
			else:
				J=0,0
	if fighttextcount==3.1:
		text1b=pygame.font.SysFont('Arial', 35, False, False).render('', True, black)
		if critical:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Coup critique !', True, black)
		if typemod!=1 and framecount>critical*80:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('C\'est '+typemodtext[[0,0.25,0.5,2,4].index(typemod)]+'efficace !', True, black)
		if effectdo and framecount>critical*80+(typemod!=1)*80 and not (Wpv<1 and attaque(save[J[0]+J[1]*2+5])[3] in [1,2,3,4,5,6,9,11,13,14,17,29]):
			if attaque(save[J[0]+J[1]*2+5])[3]==1 and prevW2[0]==0 and pokemon(sid)[1]!=10 and pokemon(sid)[2]!=10 and pokemon(sid)[1]!=16 and pokemon(sid)[2]!=16:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+" ennemi a ete empoisonne !", True, black)
				wild[2][0]=1
			if attaque(save[J[0]+J[1]*2+5])[3]==2 and prevW2[1]==0:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+" ennemi a ete paralyse !", True, black)
				text1b=pygame.font.SysFont('Arial', 35, False, False).render("Il pourrait ne pas pouvoir attaquer.", True, black)
				wild[2][1]=1
			if attaque(save[J[0]+J[1]*2+5])[3]==3 and prevW2[2]==0 and pokemon(sid)[1]!=5 and pokemon(sid)[2]!=5:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+" ennemi a ete brule !", True, black)
				wild[2][2]=1
			if attaque(save[J[0]+J[1]*2+5])[3]==4 and prevW2[3]==0 and pokemon(sid)[1]!=6 and pokemon(sid)[2]!=6:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+" ennemi a ete completement gele !", True, black)
				wild[2][3]=1
				while random.randint(1,5)!=1:
					wild[2][3]+=1
			if attaque(save[J[0]+J[1]*2+5])[3]==5 and prevW2[4]==0:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+" ennemi s'est endormi !", True, black)
				wild[2][4]=random.randint(1,4)
			if attaque(save[J[0]+J[1]*2+5])[3]==6 and prevW2[5]==0:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+" ennemi est deveu confus !", True, black)
				wild[2][5]=random.randint(1,4)
			if attaque(save[J[0]+J[1]*2+5])[3]==8:
				if save[4][6]>3.7 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if save[4][6]<1 and not effectdone:
						save[4][6]+=2*save[4][6]*save[4][6]/(4-2*save[4][6])
						effectdone=1
					if save[4][6]>=0.9 and not effectdone:
						save[4][6]+=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0]+" augmente.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==9:
				if wild[2][6]<0.27 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if wild[2][6]<=1.1 and not effectdone:
						wild[2][6]-=2*wild[2][6]*wild[2][6]/(4+2*wild[2][6])
						effectdone=1
					if wild[2][6]>1 and not effectdone:
						wild[2][6]-=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0]+" baisse.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==10:
				if save[4][7]>3.7 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if save[4][7]<1 and not effectdone:
						save[4][7]+=2*save[4][7]*save[4][7]/(4-2*save[4][7])
						effectdone=1
					if save[4][7]>=0.9 and not effectdone:
						save[4][7]+=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0]+" augmente.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==11:
				if wild[2][7]<0.27 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if wild[2][7]<=1 and not effectdone:
						wild[2][7]-=2*wild[2][7]*wild[2][7]/(4+2*wild[2][7])
						effectdone=1
					if wild[2][7]>1 and not effectdone:
						wild[2][7]-=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0]+" baisse.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==12:
				if save[4][8]>3.7 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if save[4][8]<1 and not effectdone:
						save[4][8]+=2*save[4][8]*save[4][8]/(4-2*save[4][8])
						effectdone=1
					if save[4][8]>=0.9 and not effectdone:
						save[4][8]+=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0]+" augmente.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==13:
				if wild[2][8]<0.27 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if wild[2][8]<=1 and not effectdone:
						wild[2][8]-=2*wild[2][8]*wild[2][8]/(4+2*wild[2][8])
						effectdone=1
					if wild[2][8]>1 and not effectdone:
						wild[2][8]-=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0]+" baisse.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==14:
				if wild[2][9]<0.27 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La precision de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if wild[2][9]<=1 and not effectdone:
						wild[2][9]-=2*wild[2][9]*wild[2][9]/(4+2*wild[2][9])
						effectdone=1
					if wild[2][9]>1 and not effectdone:
						wild[2][9]-=0.5
						effectdone=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La precision de "+pokemon(sid)[0]+" baisse.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==21:
				if save[4][6]>3.7 and framecount<40+critical*80+(typemod!=1)*80 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical*80+(typemod!=1)*80:
						if save[4][6]<1 and not effectdone:
							save[4][6]+=2*save[4][6]*save[4][6]/(4-2*save[4][6])
							effectdone=1
						if save[4][6]>=0.9 and not effectdone:
							save[4][6]+=0.5
							effectdone=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0]+" augmente.", True, black)
				if save[4][8]>3.7 and framecount>=40+critical*80+(typemod!=1)*80 and not effect2done:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical*80+(typemod!=1)*80:
						if save[4][8]<1 and not effect2done:
							save[4][8]+=2*save[4][8]*save[4][8]/(4-2*save[4][8])
							effect2done=1
						if save[4][8]>=0.9 and not effect2done:
							save[4][8]+=0.5
							effect2done=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0]+" augmente.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==26:
				if save[4][6]>3.7 and framecount<40+critical*80+(typemod!=1)*80 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical*80+(typemod!=1)*80:
						if save[4][6]<1 and not effectdone:
							save[4][6]+=2*save[4][6]*save[4][6]/(4-2*save[4][6])
							effectdone=1
						if save[4][6]>=0.9 and not effectdone:
							save[4][6]+=0.5
							effectdone=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0]+" augmente beaucoup.", True, black)
				if save[4][6]>3.7 and framecount>=40+critical*80+(typemod!=1)*80 and not effect2done:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical*80+(typemod!=1)*80:
						if save[4][6]<1 and not effect2done:
							save[4][6]+=2*save[4][6]*save[4][6]/(4-2*save[4][6])
							effect2done=1
						if save[4][6]>=0.9 and not effect2done:
							save[4][6]+=0.5
							effect2done=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0]+" augmente beaucoup.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==27:
				if save[4][7]>3.7 and framecount<40+critical*80+(typemod!=1)*80 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical*80+(typemod!=1)*80:
						if save[4][7]<1 and not effectdone:
							save[4][7]+=2*save[4][7]*save[4][7]/(4-2*save[4][7])
							effectdone=1
						if save[4][7]>=0.9 and not effectdone:
							save[4][7]+=0.5
							effectdone=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0]+" augmente beaucoup.", True, black)
				if save[4][7]>3.7 and framecount>=40+critical*80+(typemod!=1)*80 and not effect2done:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical*80+(typemod!=1)*80:
						if save[4][7]<1 and not effect2done:
							save[4][7]+=2*save[4][7]*save[4][7]/(4-2*save[4][7])
							effect2done=1
						if save[4][7]>=0.9 and not effect2done:
							save[4][7]+=0.5
							effect2done=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0]+" augmente beaucoup.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==28:
				if save[4][8]>3.7 and framecount<40+critical*80+(typemod!=1)*80 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical*80+(typemod!=1)*80:
						if save[4][8]<1 and not effectdone:
							save[4][8]+=2*save[4][8]*save[4][8]/(4-2*save[4][8])
							effectdone=1
						if save[4][8]>=0.9 and not effectdone:
							save[4][8]+=0.5
							effectdone=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0]+" augmente beaucoup.", True, black)
				if save[4][8]>3.7 and framecount>=40+critical*80+(typemod!=1)*80 and not effect2done:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical*80+(typemod!=1)*80:
						if save[4][8]<1 and not effect2done:
							save[4][8]+=2*save[4][8]*save[4][8]/(4-2*save[4][8])
							effect2done=1
						if save[4][8]>=0.9 and not effect2done:
							save[4][8]+=0.5
							effect2done=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0]+" augmente beaucoup.", True, black)
			if attaque(save[J[0]+J[1]*2+5])[3]==29:
				if wild[2][7]<0.27 and framecount<40+critical*80+(typemod!=1)*80 and not effectdone:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if framecount<40+critical*80+(typemod!=1)*80:
						if wild[2][7]<=1 and not effectdone:
							wild[2][7]-=2*wild[2][7]*wild[2][7]/(4+2*wild[2][7])
							effectdone=1
						if wild[2][7]>1 and not effectdone:
							wild[2][7]-=0.5
							effectdone=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0]+" baisse beaucoup.", True, black)
				if wild[2][7]<0.27 and framecount>=40+critical*80+(typemod!=1)*80 and not effect2done:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if framecount>=40+critical*80+(typemod!=1)*80:
						if wild[2][7]<=1 and not effect2done:
							wild[2][7]-=2*wild[2][7]*wild[2][7]/(4+2*wild[2][7])
							effect2done=1
						if wild[2][7]>1 and not effect2done:
							wild[2][7]-=0.5
							effect2done=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0]+" baisse beaucoup.", True, black)
		if framecount>critical*80+(typemod!=1)*80+effectdo*80-(prevW2[0:6]==wild[2][0:6] and effectdo and attaque(save[J[0]+J[1]*2+5])[3] in range(1,7))*80:
			if Wpv<1:
				fighttextcount=4.1
			else:
				fighttextcount=7
				framecount=0
	
		
	if fighttextcount==3.4:
		if paralised:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' est paralise !', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render('Il ne peut pas bouger !', True, black)
		if save[4][3]>0:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' est gele !', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render('Il ne peut pas bouger !', True, black)
		if save[4][4]>0:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' dort !', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render('', True, black)
		if framecount>80:
			if save[4][3]>0:
				save[4][3]-=1
			if save[4][4]>0:
				save[4][4]-=1
			fighttextcount=7
			framecount=0	
	if fighttextcount==3.5:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' se blesse dans sa confusion !', True, black)
		textS4=pygame.font.SysFont('Arial', 20, False, False).render(str(int(save[2]))+'/'+str(int(Smaxpv)), True, black)
		if framecount in range(60,111):
			save[2]-=((save[0]*0.4+2)*(pokemon(mid)[3][0]*save[0]/50+5)*save[4][6]*40.0/(pokemon(mid)[3][1]*save[0]/50+5)/save[4][7]/50+2)/50
			if save[2]<1:
				fighttextcount=4.2
		if framecount>140:
			save[4][5]-=1
			fighttextcount=7
			framecount=0
	if fighttextcount==4.1:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' sauvage est K.O.!', True, black)
		if framecount>20 and pygame.key.get_pressed()[111]==1:
			end=1
	if fighttextcount==4.2:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' est K.O.!', True, black)
		if framecount>20 and pygame.key.get_pressed()[111]==1:
			end=1
	if fighttextcount==5:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' utilise '+attaque(wild[attackNum+2])[4]+' !', True, black)
		if framecount in range(60,111) and attaque(wild[attackNum+2])[1]>0:
			save[2]-=((wild[0]*0.4+2)*(pokemon(sid)[3][0]*wild[0]/50+5)*wild[2][6]*attaque(wild[attackNum+2])[1]/(pokemon(mid)[3][1]*save[0]/50+5)/save[4][7]/50+2)*(critical2+1)*typemod2*stab2*alea2/50
			textS4=pygame.font.SysFont('Arial', 20, False, False).render(str(int(save[2]))+'/'+str(int(Smaxpv)), True, black)
			if save[2]<1:
				save[2]=0.0
				fighttextcount=4.2
				framecount=0
				if critical2 or typemod2!=1 or (attaque(wild[attackNum+2])[3] in [8,10,12,15,16,18,19,20,21,23,24,25,26,27,28,30,31] and effectdo2):
					fighttextcount=5.1
					framecount=0
					prevS2=save[4][:]
		if framecount==140-(attaque(wild[attackNum+2])[1]==0)*80:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Que doit faire ', True, black)
			text2=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][0], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][1], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][2], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][3], True, black)
			fighttextcount=7
			framecount=0
			submenu=0
			if critical2 or typemod2!=1 or (attaque(wild[attackNum+2])[3]!=0 and effectdo2):
				fighttextcount=5.1
				framecount=0
				prevS2=save[4][:]
	if fighttextcount==5.1:
		text1b=pygame.font.SysFont('Arial', 35, False, False).render('', True, black)
		if critical2:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Coup critique !', True, black)
		if typemod2!=1 and framecount>critical2*80:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('C\'est '+typemodtext[[0,0.25,0.5,2,4].index(typemod2)]+'efficace !', True, black)
		if effectdo2 and framecount>critical2*80+(typemod2!=1)*80 and not (save[2]<1 and attaque(wild[attackNum+2])[3] in [1,2,3,4,5,6,9,11,13,14,17,29]):
			if attaque(wild[attackNum+2])[3]==1 and prevS2[0]==0 and pokemon(mid)[1]!=10 and pokemon(mid)[2]!=10 and pokemon(mid)[1]!=16 and pokemon(mid)[2]!=16:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+" a ete empoisonne !", True, black)
				save[4][0]=1
			if attaque(wild[attackNum+2])[3]==2 and prevS2[1]==0:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+" a ete paralyse !", True, black)
				text1b=pygame.font.SysFont('Arial', 35, False, False).render("Il pourrait ne pas pouvoir attaquer.", True, black)
				save[4][1]=1
			if attaque(wild[attackNum+2])[3]==3 and prevS2[2]==0 and pokemon(mid)[1]!=5 and pokemon(mid)[2]!=5:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+" a ete brule !", True, black)
				save[4][2]=1
			if attaque(wild[attackNum+2])[3]==4 and prevS2[3]==0 and pokemon(mid)[1]!=6 and pokemon(mid)[2]!=6:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+" a ete completement gele !", True, black)
				save[4][3]=1
				while random.randint(1,5)!=1:
					save[4][3]+=1
			if attaque(wild[attackNum+2])[3]==5 and prevS2[4]==0:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+" s'est endormi !", True, black)
				save[4][4]=random.randint(1,4)
			if attaque(wild[attackNum+2])[3]==6 and prevS2[5]==0:
				text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+" est deveu confus !", True, black)
				save[4][5]=random.randint(1,4)
			if attaque(wild[attackNum+2])[3]==8:
				if wild[2][6]>3.7 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if wild[2][6]<1 and not effectdone2:
						wild[2][6]+=2*wild[2][6]*wild[2][6]/(4-2*wild[2][6])
						effectdone2=1
					if wild[2][6]>=0.9 and not effectdone2:
						wild[2][6]+=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0]+" augmente.", True, black)
			if attaque(wild[attackNum+2])[3]==9:
				if save[4][6]<0.27 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if save[4][6]<=1.1 and not effectdone2:
						save[4][6]-=2*save[4][6]*save[4][6]/(4+2*save[4][6])
						effectdone2=1
					if save[4][6]>1 and not effectdone2:
						save[4][6]-=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(mid)[0]+" baisse.", True, black)
			if attaque(wild[attackNum+2])[3]==10:
				if wild[2][7]>3.7 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if wild[2][7]<1 and not effectdone2:
						wild[2][7]+=2*wild[2][7]*wild[2][7]/(4-2*wild[2][7])
						effectdone2=1
					if wild[2][7]>=0.9 and not effectdone2:
						wild[2][7]+=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0]+" augmente.", True, black)
			if attaque(wild[attackNum+2])[3]==11:
				if save[4][7]<0.27 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if save[4][7]<=1 and not effectdone2:
						save[4][7]-=2*save[4][7]*save[4][7]/(4+2*save[4][7])
						effectdone2=1
					if save[4][7]>1 and not effectdone2:
						save[4][7]-=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0]+" baisse.", True, black)
			if attaque(wild[attackNum+2])[3]==12:
				if wild[2][8]>3.7 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if save[4][8]<1 and not effectdone2:
						wild[2][8]+=2*wild[2][8]*wild[2][8]/(4-2*wild[2][8])
						effectdone2=1
					if wild[2][8]>=0.9 and not effectdone2:
						wild[2][8]+=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0]+" augmente.", True, black)
			if attaque(wild[attackNum+2])[3]==13:
				if save[4][8]<0.27 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if save[4][8]<=1 and not effectdone2:
						save[4][8]-=2*save[4][8]*save[4][8]/(4+2*save[4][8])
						effectdone2=1
					if save[4][8]>1 and not effectdone2:
						save[4][8]-=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0]+" baisse.", True, black)
			if attaque(wild[attackNum+2])[3]==14:
				if save[4][9]<0.27 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La precision de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if save[4][9]<=1 and not effectdone2:
						save[4][9]-=2*save[4][9]*save[4][9]/(4+2*save[4][9])
						effectdone2=1
					if save[4][9]>1 and not effectdone2:
						save[4][9]-=0.5
						effectdone2=1
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La precision de "+pokemon(mid)[0]+" baisse.", True, black)
			if attaque(wild[attackNum+2])[3]==21:
				if wild[2][6]>3.7 and framecount<40+critical2*80+(typemod2!=1)*80 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical2*80+(typemod2!=1)*80:
						if wild[2][6]<1 and not effectdone2:
							wild[2][6]+=2*wild[2][6]*wild[2][6]/(4-2*wild[2][6])
							effectdone2=1
						if wild[2][6]>=0.9 and not effectdone2:
							wild[2][6]+=0.5
							effectdone2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0]+" augmente.", True, black)
				if wild[2][8]>3.7 and framecount>=40+critical2*80+(typemod2!=1)*80 and not effect2done2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical2*80+(typemod2!=1)*80:
						if wild[2][8]<1 and not effect2done2:
							wild[2][8]+=2*wild[2][8]*wild[2][8]/(4-2*wild[2][8])
							effect2done2=1
						if wild[2][8]>=0.9 and not effect2done2:
							wild[2][8]+=0.5
							effect2done2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0]+" augmente.", True, black)
			if attaque(wild[attackNum+2])[3]==26:
				if wild[2][6]>3.7 and framecount<40+critical2*80+(typemod2!=1)*80 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical2*80+(typemod2!=1)*80:
						if wild[2][6]<1 and not effectdone2:
							wild[2][6]+=2*wild[2][6]*wild[2][6]/(4-2*wild[2][6])
							effectdone2=1
						if wild[2][6]>=0.9 and not effectdone2:
							wild[2][6]+=0.5
							effectdone2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0]+" augmente beaucoup.", True, black)
				if wild[2][6]>3.7 and framecount>=40+critical2*80+(typemod2!=1)*80 and not effect2done2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical2*80+(typemod2!=1)*80:
						if wild[2][6]<1 and not effect2done2:
							wild[2][6]+=2*wild[2][6]*wild[2][6]/(4-2*wild[2][6])
							effect2done2=1
						if wild[2][6]>=0.9 and not effect2done2:
							wild[2][6]+=0.5
							effect2done2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("L'attaque de "+pokemon(sid)[0]+" augmente beaucoup.", True, black)
			if attaque(wild[attackNum+2])[3]==27:
				if wild[2][7]>3.7 and framecount<40+critical2*80+(typemod2!=1)*80 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical2*80+(typemod2!=1)*80:
						if wild[2][7]<1 and not effectdone2:
							wild[2][7]+=2*wild[2][7]*wild[2][7]/(4-2*wild[2][7])
							effectdone2=1
						if wild[2][7]>=0.9 and not effectdone2:
							wild[2][7]+=0.5
							effectdone2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0]+" augmente beaucoup.", True, black)
				if wild[2][7]>3.7 and framecount>=40+critical2*80+(typemod2!=1)*80 and not effect2done2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical2*80+(typemod2!=1)*80:
						if wild[2][7]<1 and not effect2done2:
							wild[2][7]+=2*wild[2][7]*wild[2][7]/(4-2*wild[2][7])
							effect2done2=1
						if wild[2][7]>=0.9 and not effect2done2:
							wild[2][7]+=0.5
							effect2done2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(sid)[0]+" augmente beaucoup.", True, black)
			if attaque(wild[attackNum+2])[3]==28:
				if wild[2][8]>3.7 and framecount<40+critical2*80+(typemod2!=1)*80 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount<40+critical2*80+(typemod2!=1)*80:
						if wild[2][8]<1 and not effectdone2:
							wild[2][8]+=2*wild[2][8]*wild[2][8]/(4-2*wild[2][8])
							effectdone2=1
						if wild[2][8]>=0.9 and not effectdone2:
							wild[2][8]+=0.5
							effectdone2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0]+" augmente beaucoup.", True, black)
				if wild[2][8]>3.7 and framecount>=40+critical2*80+(typemod2!=1)*80 and not effect2done2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus augmenter.", True, black)
				else:
					if framecount>=40+critical2*80+(typemod2!=1)*80:
						if wild[2][8]<1 and not effect2done2:
							wild[2][8]+=2*wild[2][8]*wild[2][8]/(4-2*wild[2][8])
							effect2done2=1
						if wild[2][8]>=0.9 and not effect2done2:
							wild[2][8]+=0.5
							effect2done2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La vitesse de "+pokemon(sid)[0]+" augmente beaucoup.", True, black)
			if attaque(wild[attackNum+2])[3]==29:
				if save[4][7]<0.27 and framecount<40+critical2*80+(typemod2!=1)*80 and not effectdone2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if framecount<40+critical2*80+(typemod2!=1)*80:
						if save[4][7]<=1 and not effectdone2:
							save[4][7]-=2*save[4][7]*save[4][7]/(4+2*save[4][7])
							effectdone2=1
						if save[4][7]>1 and not effectdone2:
							save[4][7]-=0.5
							effectdone2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0]+" baisse beaucoup.", True, black)
				if save[4][7]<0.27 and framecount>=40+critical2*80+(typemod2!=1)*80 and not effect2done2:
					text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0], True, black)
					text1b=pygame.font.SysFont('Arial', 35, False, False).render("ne peut plus baisser.", True, black)
				else:
					if framecount>=40+critical2*80+(typemod2!=1)*80:
						if save[4][7]<=1 and not effect2done2:
							save[4][7]-=2*save[4][7]*save[4][7]/(4+2*save[4][7])
							effect2done2=1
						if save[4][7]>1 and not effect2done2:
							save[4][7]-=0.5
							effect2done2=1
						text1=pygame.font.SysFont('Arial', 35, False, False).render("La defense de "+pokemon(mid)[0]+" baisse beaucoup.", True, black)
		if framecount>critical2*80+(typemod2!=1)*80+effectdo2*80-(prevS2[0:6]==save[4][0:6] and effectdo2 and attaque(wild[attackNum+2])[3] in range(1,7))*80:
			if save[2]<1:
				fighttextcount=4.2
			else:
				fighttextcount=7
				framecount=0
	if fighttextcount==5.4:
		if paralised2:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' est paralise !', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render('Il ne peut pas bouger !', True, black)
		if wild[2][3]>0:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' est gele !', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render('Il ne peut pas bouger !', True, black)
		if wild[2][4]>0:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' dort !', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render('', True, black)
		if framecount>80:
			if wild[2][3]>0:
				wild[2][3]-=1
			if wild[2][4]>0:
				wild[2][4]-=1
			fighttextcount=7
			framecount=0	
	if fighttextcount==5.5:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' se blesse dans sa confusion !', True, black)
		if framecount in range(60,111):
			Wpv-=((wild[0]*0.4+2)*(pokemon(sid)[3][0]*wild[0]/50+5)*wild[2][6]*40.0/(pokemon(sid)[3][1]*wild[0]/50+5)/wild[2][7]/50+2)/50
			if Wpv<1:
				fighttextcount=4.1
		if framecount>140:
			wild[2][5]-=1
			fighttextcount=7
			framecount=0


	if fighttextcount==6:
		if save[4][0]==1:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' souffre du poison.', True, black)
			textS4=pygame.font.SysFont('Arial', 20, False, False).render(str(int(save[2]))+'/'+str(int(Smaxpv)), True, black)
			if framecount in range(20,41):
				save[2]-=Smaxpv/8/20
				if save[2]<1:
					fighttextcount=4.2
		if wild[2][0]==1 and framecount>(save[4][0]==1)*70:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' souffre du poison.', True, black)
			if framecount in range(20+(save[4][0]==1)*70,41+(save[4][0]==1)*70):
				Wpv-=Wmaxpv/8/20
				if Wpv<1:
					fighttextcount=4.1
		if save[4][2]==1 and framecount>(save[4][0]==1)*70+(wild[2][0]==1)*70:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' brule.', True, black)
			textS4=pygame.font.SysFont('Arial', 20, False, False).render(str(int(save[2]))+'/'+str(int(Smaxpv)), True, black)
			if framecount in range(20+(save[4][0]==1)*70+(wild[2][0]==1)*70,41+(save[4][0]==1)*70+(wild[2][0]==1)*70):
				save[2]-=Smaxpv/8/20
				if save[2]<1:
					fighttextcount=4.2
		if wild[2][2]==1 and framecount>(save[4][0]==1)*70+(wild[2][0]==1)*70+(save[4][2]==1)*70:
			text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' brule.', True, black)
			if framecount in range(20+(save[4][0]==1)*70+(wild[2][0]==1)*70+(save[4][2]==1)*70,41+(save[4][0]==1)*70+(wild[2][0]==1)*70+(save[4][2]==1)*70):
				Wpv-=Wmaxpv/8/20
				if Wpv<1:
					fighttextcount=4.1
		if framecount>(save[4][0]==1)*70+(wild[2][0]==1)*70+(save[4][2]==1)*70+(wild[2][2]==1)*70:
			submenu=0
			J=0,0
			fighttextcount=2
	if fighttextcount==7:
		if attacked==[0,0]:
			attWposs=[]
			for att in range(7,11):
				if wild[att]!=0:
					attWposs.append(wild[att-4])
			attackNum=wild.index(random.choice(attWposs))-2
			if ((pokemon(mid)[3][2]*save[0]/50+5)*save[4][8]>(pokemon(sid)[3][2]*wild[0]/50+5)*wild[2][8] or attaque(save[J[0]+J[1]*2+5])[3]==7) and not attaque(wild[attackNum+2])[3]==7:
				fighttextcount=3
				attacked[0]=1
			else:
				paralised2=(random.randint(1,4)==1 and wild[2][1]==1)
				if paralised2 or wild[2][3]>0 or wild[2][4]>0:
					fighttextcount=5.4
					attacked[1]=1
				elif random.randint(1,2)==1 and wild[2][5]>0:
					fighttextcount=5.5
					attacked[1]=1
					alea2=random.uniform(0.85,1)
				else:
					fighttextcount=5
					attacked[1]=1
					alea2=random.uniform(0.85,1)
					critical2=0
					typemod2=1
					if attaque(wild[attackNum+2])[1]>0:
						if random.randint(1,16)==1:
							critical2=1
						typemod2=table(attaque(wild[attackNum+2])[0],pokemon(mid)[1])*table(attaque(wild[attackNum+2])[0],pokemon(mid)[2])
					stab2=1+(attaque(wild[attackNum+2])[0]==pokemon(sid)[1] or attaque(wild[attackNum+2])[0]==pokemon(sid)[2])*0.5
					effectdo2=(random.randint(1,100)<=attaque(wild[attackNum+2])[6])
					wild[attackNum+6]-=1
					effectdone2=0
					effect2done2=0
					if wild[2][5]>0:
						wild[2][5]-=1
		elif attacked==[0,1]:
			fighttextcount=3
			attacked[0]=1
		elif attacked==[1,0]:
			paralised2=(random.randint(1,4)==1 and wild[2][1]==1)
			if paralised2 or wild[2][3]>0 or wild[2][4]>0:
				fighttextcount=5.4
				attacked[1]=1
			elif random.randint(1,2)==1 and wild[2][5]>0:
				fighttextcount=5.5
				attacked[1]=1
				alea2=random.uniform(0.85,1)
			else:
				fighttextcount=5
				attacked[1]=1
				attWposs=[]
				for att in range(7,11):
					if wild[att]!=0:
						attWposs.append(wild[att-4])
				attackNum=wild.index(random.choice(attWposs))-2
				alea2=random.uniform(0.85,1)
				critical2=0
				typemod2=1
				if attaque(wild[attackNum+2])[1]>0:
					if random.randint(1,16)==1:
						critical2=1
					typemod2=table(attaque(wild[attackNum+2])[0],pokemon(mid)[1])*table(attaque(wild[attackNum+2])[0],pokemon(mid)[2])
				stab2=1+(attaque(wild[attackNum+2])[0]==pokemon(sid)[1] or attaque(wild[attackNum+2])[0]==pokemon(sid)[2])*0.5
				effectdo2=(random.randint(1,100)<=attaque(wild[attackNum+2])[6])
				wild[attackNum+6]-=1
				effectdone2=0
				effect2done2=0
				if wild[2][5]>0:
					wild[2][5]-=1
		elif attacked==[1,1]:
			fighttextcount=6



	screen.fill(white)
	if not (fighttextcount in [3,5.5] and framecount in range(11,21)+range(31,41)):
		screen.blit(wildim, [(fighttextcount==-1)*framecount*15-256+(fighttextcount>=0)*913,60])
	if fighttextcount>=0:
		pygame.draw.rect(screen,blue,[115,385,682,126],4)
		pygame.draw.rect(screen,green,[669,0,239,55],4)
		if Wpv>=1:
			pygame.draw.line(screen,green,(778,41),(778+120*Wpv/Wmaxpv,41),4)
		screen.blit(textW1, [684, 6])
		screen.blit(textW2, [844, 6])
		screen.blit(textW3, [746, 31])
	if fighttextcount>1:
		pygame.draw.rect(screen,green,[0,0,241,91],4)
		if save[2]>=1:
			pygame.draw.line(screen,green,(112,41),(112+120*save[2]/Smaxpv,41),4)
		if not (fighttextcount in [3.5,5] and framecount in range(11,21)+range(31,41)):
			screen.blit(selfim, [0,120])
		screen.blit(textS1, [18, 6])
		screen.blit(textS2, [178, 6])
		screen.blit(textS3, [80, 31])
		screen.blit(textS4, [162, 51])
		screen.blit(textS5, [65, 72])
	if fighttextcount in [0,1,3,3.1,3.4,3.5,4.1,4.2,5,5.1,5.4,5.5,6]:
		screen.blit(text1, [140, 400])
	if fighttextcount in [3.1,3.4,5.1,5.4]:
		screen.blit(text1b, [140, 450])
	if fighttextcount==2:
		if submenu==0:
			pygame.draw.rect(screen,black,[511+J[0]*171,412+J[1]*50,15,15])
			pygame.draw.line(screen,blue,(490,385),(490,511),4)
			screen.blit(text1, [140, 400])
			screen.blit(text1b, [140, 450])
			screen.blit(text2, [530, 400])
			screen.blit(text3, [700, 400])
			screen.blit(text4, [530, 450])
			screen.blit(text5, [700, 450])
		if submenu==1:
			pygame.draw.rect(screen,black,[121+J[0]*260,412+J[1]*50,15,15])
			pygame.draw.line(screen,blue,(640,385),(640,511),4)
			screen.blit(text2, [140, 400])
			screen.blit(text3, [400, 400])
			screen.blit(text4, [140, 450])
			screen.blit(text5, [400, 450])
			screen.blit(text6, [650, 400])
			screen.blit(text7, [650, 450])
		if submenu>1:
			screen.blit(text1, [140, 400])
	pygame.display.flip()
	pygame.time.Clock().tick(60)
save[4][6]=1.0
save[4][7]=1.0
save[4][8]=1.0
save[4][9]=1.0
open('save.sav','w').write(repr(save))
sys.exit()
