from real_estate import ColoredProperty, ColoredPropertyGroup, Property, RailroadPropertyGroup, UtilityPropertyGroup
import random
property_hash = {
1: ColoredProperty("Mediterranean Ave"	,1,	60,	30,	(2,	10,	30,	90,	160,	250), ColoredPropertyGroup((1,3),
"Purple"))
,3: ColoredProperty("Baltic Ave"		,3,	60,	30,	(4,	20,	60,	180,	320,	450),
ColoredPropertyGroup((1,3), "Purple"))
,6: ColoredProperty("Oriental Ave"		,6,	100,	50,	(6,	30,	90,	270,	400,	550),
ColoredPropertyGroup((6,8,9), "Light Blue"))
,8: ColoredProperty("Vermont Ave"		,8,	100,	50,	(6,	30,	90,	270,	400,	550),
ColoredPropertyGroup((6,8,9), "Light Blue"))
,9: ColoredProperty("Connecticut Ave"	,9,	120,	60,	(8,	40,	100,	300,	450,	600), ColoredPropertyGroup((6,8,9),
"Light Blue"))
,11: ColoredProperty("St. Charles Place"	,11,	140,	70,	(10,	50,	150,	450,	625,	750),
ColoredPropertyGroup((11,13,14), "Pink"))
,13: ColoredProperty("States Ave"		,13,	140,	70,	(10,	50,	150,	450,	625,	750),
ColoredPropertyGroup((11,13,14), "Pink"))
,14: ColoredProperty("Virginia Ave"		,14,	160,	80,	(12,	60,	180,	500,	700,	900),
ColoredPropertyGroup((11,13,14), "Pink"))
,16: ColoredProperty("St. James Place"	,16,	180,	90,	(14,	70,	200,	550,	750,	950), ColoredPropertyGroup((16,18,19),
"Orange"))
,18: ColoredProperty("Tennesee Ave"		,18,	180,	90,	(14,	70,	200,	550,	750,	950),
ColoredPropertyGroup((16,18,19), "Orange"))
,19: ColoredProperty("New York Ave"		,19,	200,	100,	(16,	80,	220,	600,	800,	1000),
ColoredPropertyGroup((16,18,19), "Orange"))
,21: ColoredProperty("Kentucky Ave"		,21,	220,	110,	(18,	90,	250,	700,	875,	1050),
ColoredPropertyGroup((21,23,24), "Red"))
,23: ColoredProperty("Indiana Ave"		,23,	220,	110,	(18,	90,	250,	700,	875,	1050),
ColoredPropertyGroup((21,23,24), "Red"))
,24: ColoredProperty("Illinois Ave"		,24,	240,	120,	(20,	100,	300,	750,	925,	1100),
ColoredPropertyGroup((21,23,24), "Red"))
,26: ColoredProperty("Atlantic Ave"		,26,	260,	130,	(22,	110,	330,	800,	975,	1150),
ColoredPropertyGroup((26,27,29), "Yellow"))
,27: ColoredProperty("Ventnor Ave"		,27,	260,	130,	(22,	110,	330,	800,	975,	1150),
ColoredPropertyGroup((26,27,29), "Yellow"))
,29: ColoredProperty("Marvin Gardens"	,29,	280,	140,	(22,	120,	360,	850,	1025,	1200), ColoredPropertyGroup((26,27,29),
"Yellow"))
,31: ColoredProperty("Pacific Ave"		,31,	300,	150,	(26,	130,	390,	900,	1100,	1275),
ColoredPropertyGroup((31,32,34), "Green"))
,32: ColoredProperty("North Carolina Ave"	,32,	300,	150,	(26,	130,	390,	900,	1100,	1275),
ColoredPropertyGroup((31,32,34), "Green"))
,34: ColoredProperty("Pennsylvania Ave"	,34,	320,	160,	(28,	150,	450,	1000,	1200,	1400), ColoredPropertyGroup((31,32,34),
"Green"))
,37: ColoredProperty("Park Place"		,37,	350,	175,	(35,	175,	500,	1100,	1300,	1500),
ColoredPropertyGroup((37,39), "Blue"))
,39: ColoredProperty("Boardwalk"		,39,	400,	200,	(50,	200,	600,	1400,	1700,	2000),
ColoredPropertyGroup((37,39), "Blue"))
,0: "Go"
,2: "Community Chest"
,4: "Income Tax"
,7: "Chance"
,10: "Jail"
,17: "Community Chest"
,20: "Free Parking"
,22: "Chance"
,30: "Go to Jail"
,33: "Community Chest"
,36: "Chance"
,38: "Luxury Tax"


,5: Property("Reading RR", 		5,	200,	100, 	RailroadPropertyGroup((5,15, 25, 35)))
,15: Property("Pennsylvania RR", 	15, 	200, 	100, 	RailroadPropertyGroup((5,15, 25, 35)))
,25: Property("B&O RR", 		25, 	200, 	100, 	RailroadPropertyGroup((5,15, 25, 35)))
,35: Property("Short Line RR",		35, 	200, 	100,	RailroadPropertyGroup((5,15, 25, 35)))


,12: Property("Electic Company", 	12, 	150, 	75, 	UtilityPropertyGroup((12,28)))
,28: Property("Water Works",		28,	150, 	75, 	UtilityPropertyGroup((12,28)))

}
display_property_hash = dict(zip(property_hash.keys(), [x.name for x in filter(lambda x: isinstance(x, Property), property_hash.values())]))

board_functions = {

"Go" : 2
, "Income Tax" : -200
, "Chance" : random.randint(1, 100)
, "Jail": 0
, "Community Chest" : random.randint(1, 100)
, "Free Parking" : 0 
, "Go to Jail": 0
, "Luxury Tax": -75
} 


