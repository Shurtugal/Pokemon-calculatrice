# -*- coding: UTF-8 -*-
def pokemon(id):
	return [('Nom','Type 1','Type 2','Stats au niv.50(Att,Déf,Vitesse,PV)','Description Pokédex'),('Pikmin',9,0,(65,65,45,45),"Ce petit bourgeon court partout et est très serviable. Sa force augmente lorsqu'il est en groupe."),('Maokai',9,0,(80,80,60,60),"Après plusieurs années passées à grandir, l'ancien bourgeon qu'il était a décidé de prendre les armes pour défendre son territoire."),('Arbre Mojo',9,0,(100,100,80,80),"Paisiblement installé dans la forêt Kokiri, il veille sur le peuple de la forêt. Son ventre abriterait un énorme donjon."),('Dodongo',5,0,(60,50,65,39),"Il aime manger des cailloux. Il s'est installé dans la caverne Dodongo en raison de la qualité des pierres qu'elle contenait."),('Blaze',5,0,(80,65,80,58),"Gardien de la forteresse des profondeurs, il n'hésitera à vous enflammer si vous vous approchez trop près."),('Saphira',5,2,(120,80,90,75),"Ce dragon a un Q.I. très supérieur à celui de l'Homme. La légende raconte qu'elle fait partie des derniers représentants de son espèce."),('Sardine',3,0,(50,64,43,44),"Ce petit pokémon des rivières a pris pour habitude de barboter sur la rive lorsque le niveau de l'eau s'abaisse."),('Anguille',3,4,(70,75,60,57),"Ce pokémon est capable d'envoyer des décharges électriques à 1 200 volts. Il est très souvent pourchassé par les braconniers qui voient en lui un commerce très lucratif."),('Léviathan',3,4,(90,100,80,77),"Au fur et à mesure des récits des quelques marins rescapés, il est devenu une véritable terreur des mers. Heureusement, il reste le plus souvent au large des côtes."),('Milou',8,0,(40,40,40,60),"Ce chien est un compagnon très fidèle."),('Anubis',8,0,(50,50,50,80),"La mythologie égyptienne l'a installé au rang de dieu de la momification. Il accompagne les morts jusqu'à la salle du jugement."),('Cerbère',8,0,(75,60,55,100),"Cerbère est un chien à trois têtes qui garde l'entrée des Enfers. Il n'obéit qu'à son maître mais il s'endort dès qu'il entend de la musique."),('Epona',8,0,(60,45,75,40),"Si vous jouez de l'ocarina, elle vous rejoindra en un instant."),('Pégase',8,15,(75,55,90,50),"Ses grandes ailes lui permettent de voler longuement sans se fatiguer. Ainsi, il est capable de couvrir de longues distances en des temps très courts."),('Dashie',8,15,(90,65,115,62),"Poney athlétique et enthousiaste, elle se plaît à voltiger en tout sens et parvient même à passer le mur du son."),('Mygale',7,8,(70,40,60,60),"Son poison peut se révéler mortel s'il n'est pas traité rapidement avec des antivenins efficaces."),('Elise',7,8,(75,42,65,65),"Cette femme-araignée peut se transformer à volonté. Elle reste recluse sur son île et il est très difficile de l'approcher."),('Aragog',7,8,(80,45,72,70),"Elle a grandi dans la forêt lorsqu'il lui est devenu impossible de se cacher. Ses araignées lui sont malgré tout restées fidèles."),('Pampa',9,0,(35,70,45,75),"Les Pampa sont des cactus joueurs qui chercheront toujours à vous faire des noises."),('Plante Piranha',9,0,(50,100,60,90),"Elle résiste à l'hiver en s'enterrant dans un sol riche en minéraux."),('Abeille',7,10,(45,60,70,35),"Les élevages d'abeille permettent d'avoir du miel tout au long de l'année."),('Guêpe',7,10,(70,65,70,42),"La prolifération de ce pokémon entraîne souvent des troubles de la faune et la flore aux alentours du nid."),('Frelon',7,10,(90,70,70,48),"Si les frelons attaquent en essaim, il est conseillé de courir."),('Gargouille',15,0,(45,65,35,70),"Hissée sur les immeubles, elle regarde les passants et les toise du regard. Si vous le soutenez suffisamment longtemps, il se peut qu'elle détourne la tête."),('Ikran',15,0,(60,75,40,75),""),('Toruk',15,0,(85,90,60,90),""),('Pac-Man',10,0,(55,55,55,55),""),('Snake',10,0,(75,75,75,75),""),('Taupe',13,12,(80,35,55,75),""),('Foreuse',13,12,(92,50,60,75),""),('Bulldozer',13,12,(103,80,75,75),""),('Silverfish',7,12,(45,45,60,45),""),('Goron',1,12,(60,80,65,70),""),('Biggoron',1,12,(85,110,55,90),""),('Lucie',13,0,(50,50,70,60),""),('Donkey Kong',13,0,(60,75,75,75),""),('King Kong',13,1,(83,80,80,85),""),('Nemo',3,0,(30,30,30,30),""),('Cheep Cheep',3,0,(50,50,50,50),""),('Flappy Bird',3,15,(90,70,100,90),""),('Têtard',3,0,(45,55,70,60),""),('Gun Gan',3,0,(65,68,70,77),""),('Jabba le Hutt',3,10,(60,140,15,110),""),('Kamek',11,0,(70,45,70,60),""),('Saroumane',11,0,(90,50,75,65),""),('Voldemort',11,0,(120,55,80,70),""),('Sonic',4,0,(65,40,85,55),""),('Flash',4,0,(75,50,105,68),""),('Raiden',4,0,(85,60,120,75),""),('Wheatley',4,16,(55,55,65,60),""),('HAL 9000',4,16,(65,60,70,80),""),('GlaDoS',4,16,(80,75,86,85),""),('Iron Golem',16,0,(62,55,40,80),""),('Laputa',16,0,(80,55,40,105),""),('Cyberman',16,0,(100,60,45,135),""),('Statue de Pâques',12,0,(50,60,50,60),""),('La Chose',12,0,(70,72,60,78),""),('Inexorable',12,11,(90,85,75,80),""),('Bob-Omb',5,0,(70,45,40,50),""),('Bomberman',5,0,(90,50,70,68),""),('Ziggs',5,0,(104,60,100,75),""),('Haricot Magique',9,0,(15,100,15,100),""),('Zyra',9,0,(80,60,70,90),""),('Géant Vert',9,0,(85,90,70,90),""),('Epic Sax Guy',8,0,(3,60,60,60),""),('Tunak Tunak',8,0,(10,60,60,60),""),('Nyan Cat',8,0,(15,30,200,30),""),('Winnie l\'Ourson',8,0,(46,60,50,60),""),('Balou',8,0,(60,70,60,70),""),('Pedobear',8,0,(75,85,70,90),""),('Enderman',14,0,(50,45,70,70),""),('Herobrine',14,0,(70,52,85,90),""),('Slender',14,0,(85,60,106,110),""),('Boo',14,0,(70,50,65,50),""),('Dame Blanche',14,11,(90,75,80,90),""),('Ombre',14,0,(55,50,65,60),""),('Scream',14,0,(65,62,75,80),""),('Vashta Nerada',14,0,(80,70,85,90),""),('Anaconda',10,0,(55,50,60,60),""),('Basilic',10,0,(63,59,73,80),""),('Quetzalcõatl',10,15,(85,67,90,101),""),('Yoshi',2,0,(67,50,45,70),""),('Rathian',2,11,(82,57,52,80),""),('Glaedr',2,11,(97,65,58,88),""),('Stitch',1,0,(62,50,55,55),""),('Na\'Vi',1,11,(90,75,78,80),""),('Elsa',6,0,(65,65,45,45),""),('Jadis',6,0,(90,88,77,75),""),('Olaf',6,0,(35,50,55,50),""),('Lapin des Neiges',6,0,(55,62,63,71),""),('Dragon des Glaces',6,2,(87,78,81,85),""),('Bowser',5,0,(50,70,30,75),""),('Ganondorf',5,0,(78,80,40,90),""),('Sauron',5,0,(107,90,50,100),""),('Gobelin',13,0,(55,50,58,70),""),('Gollum',13,0,(65,60,75,90),""),('Xénomorphe',13,0,(85,70,89,100),""),('Klitschko',1,0,(75,40,55,50),""),('M. Ali',1,0,(135,50,75,70),""),('K7',8,0,(50,68,30,65),""),('Vinyle',8,0,(70,80,33,70),""),('CD',8,0,(90,90,70,90),""),('C-3PO',16,0,(50,60,60,65),""),('Captain America',16,1,(60,80,80,80),""),('Terminator',16,1,(80,88,84,90),""),('Ver Blanc',7,0,(65,45,55,60),""),('Ver Solitaire',7,0,(80,60,75,85),""),('Cloporte de Feu',7,5,(90,78,80,96),""),('Pingu',6,0,(45,60,65,60),''),('Snow Golem',6,0,(65,78,70,65),""),('Yéti',6,0,(86,80,78,85),""),('E-Bay',8,0,(40,40,40,40),""),('Amazone',1,0,(65,65,75,65),""),('Gerudo',1,0,(98,70,88,80),""),('Faucon Millenium',16,15,(50,71,70,62),""),('DeLorean',16,15,(70,90,95,70),""),('TARDIS',16,15,(80,100,102,70),""),('False Prophet',5,0,(130,110,80,80),""),('Bird Jesus',15,8,(135,80,121,83),""),('Lord Helix',3,12,(160,180,65,75),"")][id]

def attaque(id):
	return [('type','puissance','précision','id de l\'effet','  -','pp','probabilité de l\'effet'),(8,90,75,15,'Bélier',20,100),(8,100,85,0,'Bomb\'Oeuf',10,0),(8,35,100,0,'Charge',30,0),(8,18,80,16,'Combo-Griffe',15,100),(8,10,100,13,'Constriction',35,10),(8,70,100,17,'Coup d\'Boule',15,30),(),(8,80,90,17,'Croc de Mort',15,10),(8,65,100,17,'Ecrasement',20,30),(8,40,100,0,'Ecras\'face',20,0),(8,250,100,18,'Explosion',5,100),(8,15,80,16,'Torgnoles',10,100),(8,15,85,16,'Poing Comète',15,100),(8,80,85,0,'Ultimapoing',20,0),(8,40,100,0,'Griffe',35,0),(8,55,100,0,'Force Poigne',30,0),(8,15,75,19,'Etreinte',20,100),(8,80,75,0,'Souplesse',20,0),(8,120,75,0,'Ultimawashi',5,0),(8,65,100,0,'Koud\'Korne',25,0),(8,15,85,16,'Furie',35,100),(8,85,100,2,'Plaquage',15,30),(8,15,85,16,'Ligotage',20,100),(),(8,120,100,15,'Damoclès',15,100),(8,150,90,20,'Ultralaser',5,100),(8,40,100,7,'Vive-Attaque',30,100),(),(8,200,100,18,'Destruction',5,100),(8,60,1000,0,'Météores',20,0),(),(8,20,100,16,'Picanon',15,100),(8,15,85,16,'Pillonage',20,100),(8,70,100,6,'Uppercut',10,30),(),(8,70,100,22,'Tranche',20,100),(),(1,50,100,17,'Balayage',20,30),(1,50,100,22,'Poing-Karaté',25,100),(1,30,100,23,'Double-Pied',30,100),(1,100,95,0,'Pied-Sauté',10,0),(1,60,85,17,'Mawashi-Geri',15,30),(1,80,80,15,'Sacrifice',25,100),(),(),(5,75,100,3,'Poing de Feu',15,15),(5,40,100,3,'Flammèche',25,10),(5,95,100,3,'Lance-Flamme',15,10),(5,15,85,16,'Danse-Flamme',15,100),(5,120,85,3,'Déflagration',5,30),(3,65,100,13,'Bulles d\'O',20,10),(3,35,75,16,'Claquoir',10,100),(3,20,100,13,'Ecume',30,10),(3,40,100,0,'Pisolet à O',25,0),(3,110,80,0,'Hydrocanon',5,0),(3,90,85,22,'Pince-Masse',10,100),(4,40,100,2,'Eclair',30,10),(4,75,100,2,'Poing-Eclair',15,10),(4,95,100,2,'Tonnerre',15,10),(4,110,70,2,'Fatal-Foudre',10,10),(6,120,90,4,'Blizzard',5,10),(6,75,100,4,'Poinglace',15,10),(6,95,100,4,'Laser Glace',10,10),(6,65,100,4,'Onde Boréale',20,10),(7,25,100,23,'Double-Dard',20,100),(7,14,85,16,'Dard-Nuée',20,100),(7,20,100,24,'Vampirisme',20,100),(9,35,100,0,'Fouet Lianes',10,0),(9,20,100,24,'Vol-Vie',25,100),(9,40,100,24,'Méga-Sangsue',15,100),(9,55,95,22,'Tranch\'Herbe',25,100),(),(),(10,40,100,11,'Acide',30,10),(10,15,100,1,'Dard-Venin',35,30),(10,20,70,1,'Purédpois',20,40),(10,65,100,1,'Détritus',20,30),(11,50,100,6,'Choc Mental',25,10),(11,65,100,6,'Rafale Psy',20,10),(11,90,100,11,'Psyko',10,10),(),(12,75,90,17,'Eboulement',10,30),(12,50,90,0,'Jet-Pierres',15,0),(),(13,100,100,0,'Séisme',10,0),(),(13,65,85,17,'Mass d\'Os',20,10),(13,50,90,23,'Osmerang',10,100),(14,20,100,2,'Léchouille',30,30),(14,80,100,11,'Ball\'Ombre',15,20),(15,80,100,0,'Bec Vrille',20,0),(15,60,100,0,'Cru-Aile',35,0),(15,40,100,0,'Tornade',35,0),(15,35,100,0,'Picpic',35,0),(),(16,70,90,10,'Aile d\'Acier',25,10),(16,100,75,11,'Queue de Fer',15,10),(16,50,95,12,),(),(),(2,60,100,2,'Dracosouffle',20,30),(2,80,100,0,'Dracogriffe',15,0),(2,40,100,17,'Ouragan',20,20),(8,0,1000,8,'Affûtage',30,100),(8,0,1000,10,'Armure',30,100),(8,0,55,5,'Berceuse',15,100),(8,0,1000,8,'Croissance',40,100),(),(8,0,1000,26,'Danse-Lames',30,100),(8,0,100,11,"Groz'Yeux",30,100),(8,0,100,9,'Rugissement',40,100),(),(8,0,55,6,'Ultrason',20,100),(8,0,85,29,'Grincement',40,100),(8,0,1000,30,'Soin',10,100),(8,0,75,2,'Intimidation',30,100),(7,0,95,13,'Sécrétion',40,100),(6,0,1000,31,'Buée Noire',30,100),(4,0,100,2,'Cage-Eclair',20,100),(3,0,1000,10,'Repli',40,100),(3,0,1000,0,'Trempette',40,0),(9,0,75,2,'Para-Spore',30,100),(9,0,75,5,'Poudre Dodo',30,100),(10,0,75,1,'Poudre Toxik',30,100),(10,0,55,1,'Gaz Toxik',40,100),(10,0,1000,27,'Acidarmure',40,100),(11,0,1000,27,'Bouclier',30,100),(11,0,70,5,'Hypnose',20,100),(11,0,1000,8,'Yoga',40,100),(11,0,1000,28,'Hâte',30,100),(),(11,0,80,14,'Télékinésie',15,100),(11,0,1000,25,'Repos',10,100),(13,0,100,14,'Jet de Sable',15,100),(14,0,100,6,'Onde Folie',10,100),(2,0,1000,21,'Danse Draco',20,100),(),(3,95,100,0,'Surf',15,0),(1,40,100,0,'Eclate-Roc',15,0),(8,80,100,0,'Force',15,0)][id]
