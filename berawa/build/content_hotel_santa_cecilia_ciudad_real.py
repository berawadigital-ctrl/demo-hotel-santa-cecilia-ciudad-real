# Contenido de la demo Hotel Santa Cecilia (Ciudad Real) (es/en/fr/de). Hechos de santacecilia.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Twin, Doble Superior y Triple','Junior Suite y habitaciones adaptadas'],'en':['Twin, Superior Double and Triple','Junior Suite and accessible rooms'],'fr':['Twin, Double Supérieure et Triple','Junior Suite et chambres adaptées'],'de':['Twin, Superior-Doppelzimmer und Dreibettzimmer','Junior Suite und barrierefreie Zimmer']}
RD={
'es':['Twin de 35 m² con dos camas y Doble Superior de 40 m² con cama Queen y bañera semicircular; Triples con espacio para tres personas.','Junior Suite de 45 m² en dos ambientes, con vestidor y columna de hidromasaje, y habitaciones adaptadas para personas con movilidad reducida.'],
'en':['35 m² Twin rooms with two beds and 40 m² Superior Doubles with a Queen bed and semicircular bathtub; Triples with room for three.','A 45 m² Junior Suite in two areas, with dressing room and hydromassage column, and rooms adapted for guests with reduced mobility.'],
'fr':['Twin de 35 m² avec deux lits et Double Supérieure de 40 m² avec lit Queen et baignoire semi-circulaire ; Triples pour trois personnes.','Junior Suite de 45 m² en deux espaces, avec dressing et colonne d’hydromassage, et chambres adaptées aux personnes à mobilité réduite.'],
'de':['Twin-Zimmer mit 35 m² und zwei Betten, Superior-Doppelzimmer mit 40 m², Queen-Bett und halbrunder Badewanne; Dreibettzimmer für drei Personen.','Junior Suite mit 45 m² in zwei Bereichen, mit Ankleide und Hydromassagesäule, sowie barrierefreie Zimmer für Gäste mit eingeschränkter Mobilität.']}
ART={
'hero':('arches',9981,['#2b1d14','#d9a35a','#f1d29a','#8a5a2e','#6e4622','#3a2410']),
'intro':('columns',9982,['#f2ece2','#faf6ee','#8a5a2e','#6e4622','#3a2410']),
'r1':('arches',9991,['#f0e9de','#c99350','#8a5a2e','#6e4622','#3a2410']),
'r2':('skyline',9992,['#2b1d14','#e0aa64','#f4d7a6','#9a6a3e','#7a5230','#40281a']),
'g1':('skyline',9993,['#2b1d14','#d9a35a','#f1d29a','#8a5a2e','#6e4622','#3a2410']),
'g2':('arches',9994,['#f0ece4','#f9f5ee','#9c6a36','#6a4a2a','#3a2a18']),
'g3':('hills',9995,['#ece7da','#f1e2c3','#d6a160','#a8a07e','#7c7458','#55503c']),
'g4':('columns',9996,['#2b1d14','#e0aa64','#f4d7a6','#9a6a3e','#7a5230','#40281a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Santa Cecilia · Hotel de cuatro estrellas en el centro de Ciudad Real',see_rooms='Ver las habitaciones',hero_k='Ciudad Real · Calle Tinte 3',hero_t='Un clásico en el corazón de Ciudad Real',hero_s='Hotel urbano de cuatro estrellas junto a la Plaza del Pilar.',
 intro_t='Elegante y clásico',intro_p1='El Hotel Santa Cecilia es un hotel urbano de cuatro estrellas en el centro neurálgico de Ciudad Real, junto a la Plaza del Pilar, pensado para viajes de negocios y de placer.',
 intro_p2='Tiene 70 habitaciones repartidas en un edificio de cinco plantas, restaurante Guijas de la Mancha, salones para reuniones y celebraciones y piscina de verano para clientes.',
 stats=['4 estrellas','70 habitaciones','Recepción 24 h','Piscina en verano'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Todas con wifi gratuito, TV, aire acondicionado, caja de seguridad y minibar.',
 svcs=['Restaurante Guijas de la Mancha','Recepción 24 h','Piscina (1 de junio a 1 de septiembre)','Aparcamiento privado','Salones para eventos','Accesos adaptados'],
 around_s='La Plaza del Pilar a 50 metros, la Puerta de Toledo y el Parque Arqueológico de Alarcos, a unos 8 km.',
 loc_p='Calle Tinte 3 · 13001 Ciudad Real. Desde la estación de AVE, autobuses urbanos 3, 4 o 5 hasta la parada Plaza del Pilar.',
 chips=['¿Qué habitaciones tenéis?','¿Hay piscina?','¿Dónde aparco?','¿Cómo reservo?']),
'en':dict(title='Hotel Santa Cecilia · Four-star hotel in central Ciudad Real',see_rooms='See the rooms',hero_k='Ciudad Real · Calle Tinte 3',hero_t='A classic in the heart of Ciudad Real',hero_s='Four-star city hotel next to Plaza del Pilar.',
 intro_t='Elegant and classic',intro_p1='Hotel Santa Cecilia is a four-star city hotel in the heart of Ciudad Real, next to Plaza del Pilar, designed for business and leisure travel.',
 intro_p2='It has 70 rooms in a five-storey building, the Guijas de la Mancha restaurant, meeting and event rooms and a summer pool for guests.',
 stats=['4 stars','70 rooms','24-hour reception','Summer pool'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='All with free wifi, TV, air conditioning, safe and minibar.',
 svcs=['Guijas de la Mancha restaurant','24-hour reception','Pool (1 June to 1 September)','Private parking','Event rooms','Accessible entrances'],
 around_s='Plaza del Pilar 50 metres away, the Puerta de Toledo and the Alarcos Archaeological Park, about 8 km away.',
 loc_p='Calle Tinte 3 · 13001 Ciudad Real. From the AVE station, city buses 3, 4 or 5 to the Plaza del Pilar stop.',
 chips=['Which rooms do you have?','Is there a pool?','Where can I park?','How do I book?']),
'fr':dict(title='Hôtel Santa Cecilia · Hôtel quatre étoiles au centre de Ciudad Real',see_rooms='Voir les chambres',hero_k='Ciudad Real · Calle Tinte 3',hero_t='Un classique au cœur de Ciudad Real',hero_s='Hôtel urbain quatre étoiles près de la Plaza del Pilar.',
 intro_t='Élégant et classique',intro_p1='L’Hôtel Santa Cecilia est un hôtel urbain quatre étoiles au cœur de Ciudad Real, près de la Plaza del Pilar, pensé pour les voyages d’affaires et d’agrément.',
 intro_p2='Il compte 70 chambres dans un bâtiment de cinq étages, le restaurant Guijas de la Mancha, des salons pour réunions et célébrations et une piscine d’été pour les clients.',
 stats=['4 étoiles','70 chambres','Réception 24 h/24','Piscine en été'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Toutes avec wifi gratuit, TV, climatisation, coffre-fort et minibar.',
 svcs=['Restaurant Guijas de la Mancha','Réception 24 h/24','Piscine (1er juin au 1er septembre)','Parking privé','Salons pour événements','Accès adaptés'],
 around_s='La Plaza del Pilar à 50 mètres, la Puerta de Toledo et le parc archéologique d’Alarcos, à environ 8 km.',
 loc_p='Calle Tinte 3 · 13001 Ciudad Real. Depuis la gare AVE, bus urbains 3, 4 ou 5 jusqu’à l’arrêt Plaza del Pilar.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il une piscine ?','Où me garer ?','Comment réserver ?']),
'de':dict(title='Hotel Santa Cecilia · Vier-Sterne-Hotel im Zentrum von Ciudad Real',see_rooms='Zimmer ansehen',hero_k='Ciudad Real · Calle Tinte 3',hero_t='Ein Klassiker im Herzen von Ciudad Real',hero_s='Vier-Sterne-Stadthotel neben der Plaza del Pilar.',
 intro_t='Elegant und klassisch',intro_p1='Das Hotel Santa Cecilia ist ein Vier-Sterne-Stadthotel im Zentrum von Ciudad Real, neben der Plaza del Pilar, für Geschäfts- und Urlaubsreisen.',
 intro_p2='Es hat 70 Zimmer in einem fünfstöckigen Gebäude, das Restaurant Guijas de la Mancha, Säle für Tagungen und Feiern und einen Sommerpool für Gäste.',
 stats=['4 Sterne','70 Zimmer','Rezeption rund um die Uhr','Pool im Sommer'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Alle mit kostenlosem WLAN, TV, Klimaanlage, Safe und Minibar.',
 svcs=['Restaurant Guijas de la Mancha','Rezeption rund um die Uhr','Pool (1. Juni bis 1. September)','Privatparkplatz','Veranstaltungssäle','Barrierefreie Zugänge'],
 around_s='Die Plaza del Pilar 50 Meter entfernt, die Puerta de Toledo und der Archäologische Park Alarcos, etwa 8 km entfernt.',
 loc_p='Calle Tinte 3 · 13001 Ciudad Real. Vom AVE-Bahnhof mit den Stadtbussen 3, 4 oder 5 bis zur Haltestelle Plaza del Pilar.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Pool?','Wo kann ich parken?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://hotelsantacecilia.bookinweb.es/'
BOOK=dict(mode='engine',url=dict(es=R+'es/reserva',en=R+'en/reserva',fr=R+'en/reserva',de=R+'en/reserva'))
D=dict(name='Hotel Santa Cecilia',ac='#1f2a36',ac2='#8a5a2e',ac2_a11y='#6e4622',book=BOOK,around=['Plaza del Pilar','Puerta de Toledo'],foot=FOOT,
 address='Calle Tinte 3 · 13001 Ciudad Real',phones=['+34 926 22 85 45'],emails=['recepcion@santacecilia.com'],maps='Hotel Santa Cecilia, Calle Tinte 3, 13001 Ciudad Real',t=T)
META=dict(repo='demo-hotel-santa-cecilia-ciudad-real',name='Hotel Santa Cecilia',legal_name='Hotel Santa Cecilia S.A (aviso legal de su web)',registry_ids=['A13026208'],
 url='https://www.santacecilia.com/',domain='santacecilia.com',municipality='Ciudad Real',province='Ciudad Real',sector='hotel urbano de cuatro estrellas en el centro de Ciudad Real',
 read_at='2026-10-30T11:26:00+01:00',created_at='2026-10-30T11:25:00+01:00',built_at='2026-10-30T11:35:00+01:00',audit_date='2026-10-30T11:26:30+01:00',
 rating=dict(value=4.1,coincide=['tel', 'web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Santa+Cecilia/@38.9819253,-3.9287351,17z/data=!4m9!3m8!1s0xd6bc315068d4829:0x20f6c2bdcc8e478a!5m2!4m1!1i2!8m2!3d38.9819253!4d-3.9287351!16s%2Fg%2F1tdljmxp'),
 book=dict(mode='engine',url=R+'es/reserva',note='motor de reservas real enlazado desde su web (Bookinweb), HTTP 200 comprobado el 30/10/2026 en /es/reserva y /en/reserva; el motor no tiene francés ni alemán: fr y de usan la versión inglesa.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay piscina?','K02'),('¿Dónde aparco?','K03'),('¿Tenéis cuna para bebés?','K04'),('¿Hay restaurante?','K05'),('¿Dónde está el hotel?','K06'),('¿Qué se puede visitar?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Tenéis salones para eventos?','K09'),('¿Hay recepción 24 horas?','K10'),('¿Hay wifi?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis spa?',None)],
'en':[('Which rooms do you have?','K01'),('Is there a pool?','K02'),('Where can I park?','K03'),('Do you have a cot for babies?','K04'),('Is there a restaurant?','K05'),('Where is the hotel?','K06'),('What is there to visit?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Do you have event rooms?','K09'),('Is reception open 24 hours?','K10'),('Is there wifi?','K11'),('How much is a night?',None),('Do you have a spa?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il une piscine ?','K02'),('Où me garer ?','K03'),('Avez-vous un lit bébé ?','K04'),('Y a-t-il un restaurant ?','K05'),('Où se trouve l’hôtel ?','K06'),('Que peut-on visiter ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Avez-vous des salons pour événements ?','K09'),('La réception est-elle ouverte 24 h/24 ?','K10'),('Y a-t-il le wifi ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous un spa ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es einen Pool?','K02'),('Wo kann ich parken?','K03'),('Gibt es ein Babybett?','K04'),('Gibt es ein Restaurant?','K05'),('Wo liegt das Hotel?','K06'),('Was kann man besichtigen?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es Veranstaltungssäle?','K09'),('Ist die Rezeption rund um die Uhr besetzt?','K10'),('Gibt es WLAN?','K11'),('Was kostet eine Nacht?',None),('Haben Sie ein Spa?',None)]}
