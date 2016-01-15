# -*- coding: UTF-8 -*-
def pokemon(id):
	return [('Nom','Type 1','Type 2','Stats au niv.50(Att,Def,Vitesse,PV)','Description Pokedex'),('Pikmin',9,0,(65,65,45,45),"Ce petit bourgeon court partout et est tres serviable. Sa force augmente lorsqu'il est en groupe."),('Maokai',9,0,(80,80,60,60),"Apres plusieurs annees passees a grandir, l'ancien bourgeon qu'il etait a decide de prendre les armes pour defendre son territoire."),('Arbre Mojo',9,0,(100,100,80,80),"Paisiblement installe dans la foret Kokiri, il veille sur le peuple de la foret. Son ventre abriterait un enorme donjon."),('Dodongo',5,0,(60,50,65,39),"Il aime manger des cailloux. Il s'est installe dans la caverne Dodongo en raison de la qualite des pierres qu'elle contenait."),('Blaze',5,0,(80,65,80,58),"Gardien de la forteresse des profondeurs, il n'hesitera a vous enflammer si vous vous approchez trop pres."),('Saphira',5,2,(120,80,90,75),"Ce dragon a un Q.I. tres superieur a celui de l'Homme. La legende raconte qu'elle fait partie des derniers representants de son espece."),('Sardine',3,0,(50,64,43,44),"Ce petit pokemon des rivieres a pris pour habitude de barboter sur la rive lorsque le niveau de l'eau s'abaisse."),('Anguille',3,4,(70,75,60,57),"Ce pokemon est capable d'envoyer des decharges electriques a 1 200 volts. Il est tres souvent pourchasse par les braconniers qui voient en lui un commerce tres lucratif."),('Leviathan',3,4,(90,100,80,77),"Au fur et a mesure des recits des quelques marins rescapes, il est devenu une veritable terreur des mers. Heureusement, il reste le plus souvent au large des cotes."),('Milou',8,0,(40,40,40,60),"Ce chien est un compagnon tres fidele."),('Anubis',8,0,(50,50,50,80),"La mythologie egyptienne l'a installe au rang de dieu de la momification. Il accompagne les morts jusqu'a la salle du jugement."),('Cerbere',8,0,(75,60,55,100),"Cerbere est un chien a trois tetes qui garde l'entree des Enfers. Il n'obeit qu'a son maitre mais il s'endort des qu'il entend de la musique."),('Epona',8,0,(60,45,75,40),"Si vous jouez de l'ocarina, elle vous rejoindra en un instant."),('Pegase',8,15,(75,55,90,50),"Ses grandes ailes lui permettent de voler longuement sans se fatiguer. Ainsi, il est capable de couvrir de longues distances en des temps tres courts."),('Dashie',8,15,(90,65,115,62),"Poney athletique et enthousiaste, elle se plait a voltiger en tout sens et parvient meme a passer le mur du son."),('Mygale',7,8,(70,40,60,60),"Son poison peut se reveler mortel s'il n'est pas traite rapidement avec des antivenins efficaces."),('Elise',7,8,(75,42,65,65),"Cette femme-araignee peut se transformer a volonte. Elle reste recluse sur son ile et il est tres difficile de l'approcher."),('Aragog',7,8,(80,45,72,70),"Elle a grandi dans la foret lorsqu'il lui est devenu impossible de se cacher. Ses araignees lui sont malgre tout restees fideles."),('Pampa',9,0,(35,70,45,75),"Les Pampa sont des cactus joueurs qui chercheront toujours a vous faire des noises."),('Plante Piranha',9,0,(50,100,60,90),"Elle resiste a l'hiver en s'enterrant dans un sol riche en mineraux."),('Abeille',7,10,(45,60,70,35),"Les elevages d'abeille permettent d'avoir du miel tout au long de l'annee."),('Guepe',7,10,(70,65,70,42),"La proliferation de ce pokemon entraine souvent des troubles de la faune et la flore aux alentours du nid."),('Frelon',7,10,(90,70,70,48),"Si les frelons attaquent en essaim, il est conseille de courir."),('Gargouille',15,0,(45,65,35,70),"Hissee sur les immeubles, elle regarde les passants et les toise du regard. Si vous le soutenez suffisamment longtemps, il se peut qu'elle detourne la tete."),('Ikran',15,0,(60,75,40,75),"Le lien qui l'unit a son dresseur est particulierement fort. Il communique souvent avec ce dernier sur son etat de sante."),('Toruk',15,0,(85,90,60,90),"« Toruk » signifie « la derniere ombre » en Na'Vi. Probablement celle que vous voyez avant de mourir...h"),('Pac-Man',10,0,(55,55,55,55),"Longtemps enferme dans un labyrinthe, il a decide de sortir afin de montrer au monde ce qu'il avait dans le ventre."),('Snake',10,0,(75,75,75,75),"Pour attirer un Snake, il est conseille d'utiliser une pomme pour l'appater. Cela le rend tres dangereux pour les agriculteurs."),('Taupe',13,12,(80,35,55,75),"Aveugle, elle parvient malgre tout a creuser des tunnels en se reperant grace a son sixieme sens."),('Foreuse',13,12,(92,50,60,75),"Sa grosse perceuse peut traverser des metaux tres resistants."),('Bulldozer',13,12,(103,80,75,75),"Ce pokemon est souvent utilise sur les chantiers de construction par les humains qui voient en lui une maniere tres efficace de transporter de lourdes charges."),('Silverfish',7,12,(45,45,60,45),"Il se cache dans les rochers en attendant qu'un mineur imprudent ne vienne briser son habitat..."),('Goron',1,12,(60,80,65,70),"Il passe la plupart de son temps en boule, a rouler dans le Mont du Peril."),('Biggoron',1,12,(85,110,55,90),"C'est un ancien maître d'armes qui a, un jour, forge une epee pour le Heros du Temps."),('Lucie',13,0,(50,50,70,60),"Les Lucie sont les derniers representants d'une espece eteinte depuis plusieurs millions d'annees."),('Donkey Kong',13,0,(60,75,75,75),"Il adore devaler la montagne dans de grands tonneaux. Il vit dans la jungle, afin de pouvoir se procurer des bananes a volonte."),('King Kong',13,1,(83,80,80,85),"Le premier King Kong decouvert a fini sur le toit de l'Empire State Building devant des milliers d'habitants terrifies."),('Nemo',3,0,(30,30,30,30),"Ce poisson-clown jovial n'a pas de conscience du danger. Il s'aventurera souvent dans des endroits peu sûrs."),('Cheep Cheep',3,0,(50,50,50,50),"Il a developpe la capacite de sauter hors de l'eau a plus de cinq metres de hauteur !"),('Flappy Bird',3,15,(90,70,100,90),"A force de faire de grands sauts, des ailes ont pousse sur son dos."),('Tetard',3,0,(45,55,70,60),"Si vous possedez un tetard dans un aquarium, vous le verrez grandir a une vitesse flagrante."),('Gun Gan',3,0,(65,68,70,77),"Les Gun Gan sont reputes pour etre une race de guerriers assez peu ouverts au monde et aux races qui les entourent."),('Jabba le Hutt',3,10,(60,140,15,110),"Cette grosse limace a longtemps organise des courses de pods sur Tatooïne. Il se nourrit exclusivement de larves plus petites que lui."),('Kamek',11,0,(70,45,70,60),"Il peut disparaître et se teleporter où bon lui semble dans un rayon de dix metres."),('Saroumane',11,0,(90,50,75,65),"Son bastion, Isengard, a ete detruit par les Ents."),('Voldemort',11,0,(120,55,80,70),"Il a divise son ame en huit morceaux. Aujourd'hui, ce n'est presque plus un homme."),('Sonic',4,0,(65,40,85,55),"La plupart des Sonic se voient retirer leur permis de conduire dans les mois suivant leur acquisition en raison d'exces de vitesse repetes."),('Flash',4,0,(75,50,105,68),"Il peut courir plus vite que la lumiere et ainsi echapper a la gravite."),('Raiden',4,0,(85,60,120,75),"Il maîtrise la foudre comme personne."),('Wheatley',4,16,(55,55,65,60),"C'est un processeur de personnalite developpe par Aperture Science."),('HAL 9000',4,16,(65,60,70,80),"HAL 9000 est un supercalculateur dote d'une intelligence artificielle forte."),('GlaDoS',4,16,(80,75,86,85),"Elle a une vision reductrice de la personnalite humaine mais promet des gateaux si l'on parveitn a reussir ses tests."),('Iron Golem',16,0,(62,55,40,80),"Il adore les fleurs, si bien qu'il en porte toujours sur lui pour en offrir au monde."),('Laputa',16,0,(80,55,40,105),"Selon les dires, ils garderaient l'entree d'un immense chateau volant."),('Cyberman',16,0,(100,60,45,135),"Leur objectif est la domination du monde en mettant a jour tous les humains pour qu'ils deviennent comme eux."),('Statue de Paques',12,0,(50,60,50,60),"Selon certains, ces statues geantes temoigneraient du passage d'une civilisation extraterrestre."),('La Chose',12,0,(70,72,60,78),"Ce mur de briques est le resultat d'une mutation genetique."),('Inexorable',12,11,(90,85,75,80),"L'Inexorable est un condense de sagesse et les contes de la Legende en parlent comme d'un dieu."),('Bob-Omb',5,0,(70,45,40,50),"Les Bob-Ombs adorent se faire exploser devant leurs adversaires."),('Bomberman',5,0,(90,50,70,68),"En grandissant, il a appris a lancer d'autres Bob-Ombs pour se defendre."),('Ziggs',5,0,(104,60,100,75),"Ce petit farceur adorera vous bomarder d'explosifs pendant qu'il est a une grande distance de vous. Beaucoup le trouvent insupportable."),('Haricot Magique',9,0,(15,100,15,100),"Les superstitions racontent que planter un haricot magique peuvent ouvrir une porte vers un nouveau monde. Malgre tout, rares sont les personnes a avoir essayer."),('Zyra',9,0,(80,60,70,90),"Les plantes ont pris possession de sa conscience, ce qui la rend tres instable. Les Zyra sont reputees pour ne pas avoir beaucoup de moral."),('Geant Vert',9,0,(85,90,70,90),"Desormais, il consacre sa vie a la preservation du regne vegetal."),('Epic Sax Guy',8,0,(3,60,60,60),"Son dehanche est devenu celebre a travers le monde entier et le rythme entraînant de son saxophone finira tres vite par vous insupporter."),('Tunak Tunak',8,0,(10,60,60,60),"Il a la capacite de se dedoubler lorsqu'il chante, afin de representer toutes les couleurs de l'arc-en-ciel."),('Nyan Cat',8,0,(15,30,200,30),"Un chat, une tartine, un arc-en-ciel, l'espace et de la musique. Que demander de plus ?"),('Winnie l\'Ourson',8,0,(46,60,50,60),"Il est a la recherche du pot de miel qu'il a perdu."),('Balou',8,0,(60,70,60,70),"Ce philosophe epicurien verra toujours le bon côte des choses."),('Pedobear',8,0,(75,85,70,90),"Il adore les petites filles..."),('Enderman',14,0,(50,45,70,70),"Ces creatures d'un autre monde passent leur temps a voler des blocs. Personne ne sait ce qu'ils en font."),('Herobrine',14,0,(70,52,85,90),"La semi-conscience qui l'habite a vole un corps pour pouvoir survivre."),('Slender',14,0,(85,60,106,110),"On ne compte plus le nombre de creepypastas a son sujet."),('Boo',14,0,(70,50,65,50),"Des que vous avez le dos tourne, il en profitera pour s'approcher de vous."),('Dame Blanche',14,11,(90,75,80,90),"Vous ne pourrez la croiser que la nuit, seulement si vous n'avez pas de chance."),('Ombre',14,0,(55,50,65,60),"Elles ne sortent jamais des cavernes qui les abritent, esperant le passage d'un randonneur malheureux."),('Scream',14,0,(65,62,75,80),"C'est un tueur en serie qui adore jouer avec ses victimes."),('Vashta Nerada',14,0,(80,70,85,90),"Litteralement «les ombres qui dissolvent la chair,» ces essaims mangeurs d'Homme vivent habituellement dans les forets."),('Anaconda',10,0,(55,50,60,60),"Ce serpent peut s'enrouler autour du cou de sa victime pour l'etouffer."),('Basilic',10,0,(63,59,73,80),"Le fait de le regarder dans les yeux vous assurera une mort immediate."),('Quetzalcõatl',10,15,(85,67,90,101),"Il regule toute la mythologie azteque. Peu de gens osent se mettre en travers de son chemin"),('Yoshi',2,0,(67,50,45,70),"Apres avoir passe beaucoup de temps dans un oeuf, il adorera decouvrir le monde, ce qui en fait un pokemon tres joueur."),('Rathian',2,11,(82,57,52,80),"Ce dragon passe le plus clair de son temps dans les montagnes, a chasser des animaux pour nourrir son nid."),('Glaedr',2,11,(97,65,58,88),"Il peut communiquer par telepathie avec toutes les especes vivantes, ce qui en fait une veritable encyclopedie sur la nature."),('Stitch',1,0,(62,50,55,55),"C'est devenue la mascotte de toutes les ecoles de dresseurs de pokemon grace a son caractere enjoue en toutes circonstances."),('Na\'Vi',1,11,(90,75,78,80),"Ils puisent leur force dans leur entente avec Eywa, la Deesse-Mere."),('Elsa',6,0,(65,65,45,45),"Longtemps incomprise, cette jeune femme a fini par choisir l'exil afin de proteger sa soeur."),('Jadis',6,0,(90,88,77,75),"Jadis est la derniere reine de Charn. Elle est reputee pour etre la souveraine la plus cruelle de Narnia."),('Olaf',6,0,(35,50,55,50),"Bonhomme de neige enjoue, Olaf adorera retirer son nez afin de vous taquiner avec."),('Lapin des Neiges',6,0,(55,62,63,71),"Il apporte une aide precieuse au plombier moustachu lorsque ce dernier se retrouve dans l'espace."),('Dragon des Glaces',6,2,(87,78,81,85),"Les Dragons des Glaces ne descendent jamais de leurs montagnes. Ainsi, si vous voulez l'approcher, il vaut mieux pratiquer l'alpinisme."),('Bowser',5,0,(50,70,30,75),"Cette tortue a mute pour devenir tres agressive. Prenez garde a ses piquants et son crachat de flammes."),('Ganondorf',5,0,(78,80,40,90),"Il a brise le sceau du Temple de la Lumiere pour s'emparer de la Triforce et faire du royaume d'Hyrule une veritable dystopie où il est le seul maître a gouverner."),('Sauron',5,0,(107,90,50,100),"Depuis sa Chute, il cherche a s'emparer a tout prix de l'Anneau de Pouvoir afin de recouvrer sa puissance et pouvoir dominer la Terre du Milieu."),('Gobelin',13,0,(55,50,58,70),"Reputes tres malins, les Gobelins ont une vision tres particuliere du commerce. Attention aux conditions lorsque vous traitez un signe avec eux."),('Gollum',13,0,(65,60,75,90),"L'Anneau de Pouvoir a completement corrompu son esprit."),('Xenomorphe',13,0,(85,70,89,100),"Il se developpe dans le ventre de son hôte et tue ce dernier pour sortir a la lumiere du jour."),('Klitschko',1,0,(75,40,55,50),"C'est un boxeur tres repute."),('M. Ali',1,0,(135,50,75,70),"Au fil de ses combats, c'est devenu une veritable legende du ring."),('K7',8,0,(50,68,30,65),"C'est une veritable galere lorsque vous devez la rembobiner a la main..."),('Vinyle',8,0,(70,80,33,70),"Aussi appele «78 tours,» il possede une qualite d'enregistrement encore rarement remise en cause."),('CD',8,0,(90,90,70,90),"Il s'est tres largement popularise. Certains l'utilisent pour faire apparaître un arc-en-ciel..."),('C-3PO',16,0,(50,60,60,65),"Monte de touts pieces par un jeune Jedi, il maîtrise plus de six millions de formes de communications."),('Captain America',16,1,(60,80,80,80),"Il est en mission pour sa patrie et son boucler peut le proteger d'a peu pres n'importe quoi."),('Terminator',16,1,(80,88,84,90),"N'oubliez de faire preuve de respect lorsque vous vous adressez a lui si vous tenez a la vie."),('Ver Blanc',7,0,(65,45,55,60),"Il passe la majeure partie de son temps sous la terre a se nourrir de nutriments."),('Ver Solitaire',7,0,(80,60,75,85),"C'est devenu un parasite qui penetre dans le systeme digestif de son hôte."),('Cloporte de Feu',7,5,(90,78,80,96),"Il a developpe la capacite de s'enflammer au moindre contact. C'est un moyen d'auto-defense qui a deja fait ses preuves."),('Pingu',6,0,(45,60,65,60),"Pingu est un pingouin casse-cou qui n'hesitera pas a partir a l'aventure."),('Snow Golem',6,0,(65,78,70,65),"La citrouille qu'il porte sur la tete ne sert qu'a effrayer les personnes facilement impressionables."),('Yeti',6,0,(86,80,78,85),"A l'origine, c'etait une legende urbaine. Mais une equipe de scientifique a fini par prouver son existence de maniere irrefutable."),('E-Bay',8,0,(40,40,40,40),"Attention aux arnaques, il est tres doue pour ca..."),('Amazone',1,0,(65,65,75,65),"Ces guerrieres avaient la reputation de monter les chevaux de profil pour mieux tirer a l'arc."),('Gerudo',1,0,(98,70,88,80),"Les forteresses qu'elles ont construites sont reputes pour etre imprenables."),('Faucon Millenium',16,15,(50,71,70,62),"Il a participe a de nombreuses batailles spatiales."),('DeLorean',16,15,(70,90,95,70),"Elle doit sa celebrite au convecteur temporel du Docteur Emmett Brown."),('TARDIS',16,15,(80,100,102,70),"«Time And Relative Dimension In Space,» tout simplement."),('False Prophet',5,0,(130,110,80,80),"Il aurait trahi toute une population avant de disparaître mysterieusement."),('Bird Jesus',15,8,(135,80,121,83),"Certains l'ont deja apercu volant tres haut dans le ciel."),('Lord Helix',3,12,(160,180,65,75),"Les ecrits a son sujet sont frequents mais personne n'est capable d'affirmer sa veritable existence. C'est sans doute une entite protectrice du monde.")][id]

def attaque(id):
	return [('type','puissance','precision','id de l\'effet','  -','pp','probabilite de l\'effet'),(8,90,75,15,'Belier',20,100),(8,100,85,0,'Bomb\'Oeuf',10,0),(8,35,100,0,'Charge',30,0),(8,18,80,16,'Combo-Griffe',15,100),(8,10,100,13,'Constriction',35,10),(8,70,100,17,'Coup d\'Boule',15,30),(),(8,80,90,17,'Croc de Mort',15,10),(8,65,100,17,'Ecrasement',20,30),(8,40,100,0,'Ecras\'face',20,0),(8,250,100,18,'Explosion',5,100),(8,15,80,16,'Torgnoles',10,100),(8,15,85,16,'Poing Comete',15,100),(8,80,85,0,'Ultimapoing',20,0),(8,40,100,0,'Griffe',35,0),(8,55,100,0,'Force Poigne',30,0),(8,15,75,19,'Etreinte',20,100),(8,80,75,0,'Souplesse',20,0),(8,120,75,0,'Ultimawashi',5,0),(8,65,100,0,'Koud\'Korne',25,0),(8,15,85,16,'Furie',35,100),(8,85,100,2,'Plaquage',15,30),(8,15,85,16,'Ligotage',20,100),(),(8,120,100,15,'Damocles',15,100),(8,150,90,20,'Ultralaser',5,100),(8,40,100,7,'Vive-Attaque',30,100),(),(8,200,100,18,'Destruction',5,100),(8,60,1000,0,'Meteores',20,0),(),(8,20,100,16,'Picanon',15,100),(8,15,85,16,'Pillonage',20,100),(8,70,100,6,'Uppercut',10,30),(),(8,70,100,22,'Tranche',20,100),(),(1,50,100,17,'Balayage',20,30),(1,50,100,22,'Poing-Karate',25,100),(1,30,100,23,'Double-Pied',30,100),(1,100,95,0,'Pied-Saute',10,0),(1,60,85,17,'Mawashi-Geri',15,30),(1,80,80,15,'Sacrifice',25,100),(),(),(5,75,100,3,'Poing de Feu',15,15),(5,40,100,3,'Flammeche',25,10),(5,95,100,3,'Lance-Flamme',15,10),(5,15,85,16,'Danse-Flamme',15,100),(5,120,85,3,'Deflagration',5,30),(3,65,100,13,'Bulles d\'O',20,10),(3,35,75,16,'Claquoir',10,100),(3,20,100,13,'Ecume',30,10),(3,40,100,0,'Pisolet a O',25,0),(3,110,80,0,'Hydrocanon',5,0),(3,90,85,22,'Pince-Masse',10,100),(4,40,100,2,'Eclair',30,10),(4,75,100,2,'Poing-Eclair',15,10),(4,95,100,2,'Tonnerre',15,10),(4,110,70,2,'Fatal-Foudre',10,10),(6,120,90,4,'Blizzard',5,10),(6,75,100,4,'Poinglace',15,10),(6,95,100,4,'Laser Glace',10,10),(6,65,100,4,'Onde Boreale',20,10),(7,25,100,23,'Double-Dard',20,100),(7,14,85,16,'Dard-Nuee',20,100),(7,20,100,24,'Vampirisme',20,100),(9,35,100,0,'Fouet Lianes',10,0),(9,20,100,24,'Vol-Vie',25,100),(9,40,100,24,'Mega-Sangsue',15,100),(9,55,95,22,'Tranch\'Herbe',25,100),(),(),(10,40,100,11,'Acide',30,10),(10,15,100,1,'Dard-Venin',35,30),(10,20,70,1,'Puredpois',20,40),(10,65,100,1,'Detritus',20,30),(11,50,100,6,'Choc Mental',25,10),(11,65,100,6,'Rafale Psy',20,10),(11,90,100,11,'Psyko',10,10),(),(12,75,90,17,'Eboulement',10,30),(12,50,90,0,'Jet-Pierres',15,0),(),(13,100,100,0,'Seisme',10,0),(),(13,65,85,17,'Mass d\'Os',20,10),(13,50,90,23,'Osmerang',10,100),(14,20,100,2,'Lechouille',30,30),(14,80,100,11,'Ball\'Ombre',15,20),(15,80,100,0,'Bec Vrille',20,0),(15,60,100,0,'Cru-Aile',35,0),(15,40,100,0,'Tornade',35,0),(15,35,100,0,'Picpic',35,0),(),(16,70,90,10,'Aile d\'Acier',25,10),(16,100,75,11,'Queue de Fer',15,10),(16,50,95,12,),(),(),(2,60,100,2,'Dracosouffle',20,30),(2,80,100,0,'Dracogriffe',15,0),(2,40,100,17,'Ouragan',20,20),(8,0,1000,8,'Affutage',30,100),(8,0,1000,10,'Armure',30,100),(8,0,55,5,'Berceuse',15,100),(8,0,1000,8,'Croissance',40,100),(),(8,0,1000,26,'Danse-Lames',30,100),(8,0,100,11,"Groz'Yeux",30,100),(8,0,100,9,'Rugissement',40,100),(),(8,0,55,6,'Ultrason',20,100),(8,0,85,29,'Grincement',40,100),(8,0,1000,30,'Soin',10,100),(8,0,75,2,'Intimidation',30,100),(7,0,95,13,'Secretion',40,100),(6,0,1000,31,'Buee Noire',30,100),(4,0,100,2,'Cage-Eclair',20,100),(3,0,1000,10,'Repli',40,100),(3,0,1000,0,'Trempette',40,0),(9,0,75,2,'Para-Spore',30,100),(9,0,75,5,'Poudre Dodo',30,100),(10,0,75,1,'Poudre Toxik',30,100),(10,0,55,1,'Gaz Toxik',40,100),(10,0,1000,27,'Acidarmure',40,100),(11,0,1000,27,'Bouclier',30,100),(11,0,70,5,'Hypnose',20,100),(11,0,1000,8,'Yoga',40,100),(11,0,1000,28,'Hate',30,100),(),(11,0,80,14,'Telekinesie',15,100),(11,0,1000,25,'Repos',10,100),(13,0,100,14,'Jet de Sable',15,100),(14,0,100,6,'Onde Folie',10,100),(2,0,1000,21,'Danse Draco',20,100),(),(3,95,100,0,'Surf',15,0),(1,40,100,0,'Eclate-Roc',15,0),(8,80,100,0,'Force',15,0)][id]

def table(ta,td):
	return [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2,0.5,2,1,0.5,0.5,2,1,0,0.5,2],[1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5],[1,1,0.5,0.5,1,2,1,1,1,0.5,1,1,2,2,1,1,1],[1,1,0.5,2,0.5,1,1,1,1,0.5,1,1,1,0,1,2,1],[1,1,0.5,0.5,1,0.5,2,2,1,2,1,1,0.5,1,1,1,2],[1,1,2,0.5,1,0.5,0.5,1,1,2,1,1,1,2,1,2,0.5],[1,0.5,1,1,1,0.5,1,1,1,2,0.5,2,1,1,0.5,0.5,0.5],[1,1,1,1,1,1,1,1,1,1,1,1,0.5,1,0,1,0.5],[1,1,0.5,2,1,0.5,1,0.5,1,0.5,0.5,1,2,2,1,0.5,0.5],[1,1,1,1,1,1,1,1,1,2,0.5,1,0.5,0.5,0.5,1,0],[1,2,1,1,1,1,1,1,1,1,2,0.5,1,1,1,1,0.5],[1,0.5,1,1,1,2,2,2,1,1,1,1,1,0.5,1,2,0.5],[1,1,1,1,2,2,1,0.5,1,0.5,2,1,2,1,1,0,2],[1,1,1,1,1,1,1,1,0,1,1,2,1,1,2,1,1],[1,2,1,1,0.5,1,1,2,1,2,1,1,0.5,1,1,1,0.5],[1,1,1,0.5,0.5,0.5,2,1,1,1,1,1,2,1,1,1,0.5]][ta][td]
