import random

def random_enc(num):

	def roll_dice(numbr,dice):
		roll = 0
		i = 1
		dice_s = []
		while i <= dice:
			dice_s += [i]
			i += 1
		i = 1
		while i <= numbr:
			roll += random.choice(dice_s)
			i += 1
		return(roll)

	man_tab = { 3: 'Special Encounte', 
				4: 'Moving Vehicle or Ultra-tech Bunker', 
				5: 'Small Settlemen', 
				6: 'Lone Wandere', 
				7: 'Caravan or Wasteland Gan', 
				8: 'Ruin', 
				9: 'Vehicle (junk)', 
				10: 'Animals', 
				11: 'Remain', 
				12: 'Ruin', 
				13: 'Trap or Ambus', 
				14: 'Raiders or Slaver', 
				15: 'Super Mutants or Cannibals Fortificatio', 
				16: 'Fortificatio', 
				17: 'Military Unit or Military Outpos (Note: Usually either BOS or Unity Mutants or Mercenaries)', 
				18: 'Special Encounte' }
	spc_enc = 'Special Encounte'
	mov_veh = { 3: 'Heavy MBT ', 
				4: 'Light or medium AFV', 
				5: 'Improvised APC', 
				6: 'Hummer', 
				7: 'Scout Car', 
				8: 'Highwayman', 
				9: 'Dune Buggy', 
				10: 'Bicycle or Caravan Trailer', 
				11: 'Motorcycle', 
				12: 'Trike', 
				13: 'Semi-Truck', 
				14: 'Truck', 
				15: 'Hang-glider or para-glider', 
				16: 'Single Prop Airplane', 
				17: 'Dual prop transport airplane', 
				18: 'Military Aircraft (chopper or jet)' }
	sml_set = 'Small Settlement'
	lon_wan = { 3: 'BOS Paladin', 
				4: 'Heavily armed badass hero(ine)', 
				5: 'Samaritan Medic or BOS Knight', 
				6: 'Helpless and pitiable victim', 
				7: 'Desert ranger with assault rifle', 
				8: 'Survivalist with AR-7 or bow or crossbow', 
				9: 'Hunter with bow or rifle or spear', 
				10: 'Drifter with knife or other light weapon', 
				11: 'Scav with pistol or slingshot', 
				12: 'Tribal hunter with bow or spear', 
				13: 'Raider with .223 rifle', 
				14: 'Mercenary with AK-47', 
				15: 'Super Mutant with flamethrower or machinegun', 
				16: 'Elite Mercenary with AR-15A2 HBAR', 
				17: 'Hostile Cannibal / Serial Killer with Ripper', 
				18: 'Hostile Evil Sniper with PSG-1 or Barret M82A2'}
	caravan = 'Caravan'
	ruins   = { 3: 'Ghost Town ((2D6-2)x100)', 
				4: 'Abandoned Fort ((D6-1)x10)', 
				5: 'Abandoned Survival Bunker (D10-1)', 
				6: 'Looted Survival Bunker (2D4-2)', 
				7: 'Ruined Gas-station (D8-1)', 
				8: 'Abandoned Farmstead (D6-1)', 
				9: 'Ragged Tents (D4-1)', 
				10: 'Rubble (D3-1)', 
				11: 'Ruined Building (D4-1)', 
				12: 'Burned and looted Village (D6-1)', 
				13: 'Ruined Highway Motel (D8-1)', 
				14: 'Lots of Rubble (2D4-2)', 
				15: 'Burned General Store (2D6-2)', 
				16: 'Abandoned Camo-net tents (D10-1)', 
				17: 'Hidden Cache ((D6-1)x10)', 
				18: 'Radioactive Crater surrounded by ruins ((D6-1)x10)' }
	veh_jun = { 3: 'Main Battle Tank (2D6-2)', 
				4: 'APC (3D6-3)', 
				5: 'Hummer (3D6-3)', 
				6: 'Solar Car (D6-1)', 
				7: 'Highwayman (D3-1)', 
				8: 'Scout Car (D3-1)', 
				9: 'Dune Buggy (D4-1)', 
				10: 'Caravan Trailer (D3-1)', 
				11: 'Motorcycle / Trike (D2-1)', 
				12: 'Dune Buggy (D4-1)', 
				13: 'Semi-Truck (2D4-2)', 
				14: 'Truck (2D6-2)', 
				15: '16 17', 
				15: 'Hang-glider (D2-1)', 
				16: 'Single Prop Airplane (3D6-3)', 
				17: 'Chopper (2D6-2)', 
				18: 'Jetfighter (D6-1)'}
	animals = { 3: 'Tiger or some other exotic animal', 
				4: 'Pre-sentient mutant humans', 
				5: 'Giant ants', 
				6: 'Pack of wolves or wild dogs', 
				7: 'Radscorpions', 
				8: 'Rattlesnake', 
				9: 'Radscorpion', 
				10: 'Small cockroaches or Geckos', 
				11: 'Mutant Rats or Pigrats', 
				12: 'Molerats or Geckos and Golden Geckos', 
				13: 'Big and Small Cockroaches', 
				14: 'Mutant Praying Mantises', 
				15: 'Deathclaw or Baby Deathclaws', 
				16: 'Centaurs or Floaters', 
				17: 'Aliens or Fire Geckos', 
				18: 'Deathclaws' }
	remains = { 3: '4D Corpses on battlefield (4D-4)', 
				4: 'Corpse of SpecOps Soldier (2D-2)', 
				5: 'Corpse of Soldier (D-1)', 
				6: 'Corpse of Lone Wanderer (roll)', 
				7: 'Bones of 2D6 animals', 
				8: 'Bones of 2D6 humans (D3-1)', 
				9: 'Bones of a human (D2-1)', 
				10: 'Bones of an animal', 
				11: 'Grave (D2-1)', 
				12: 'Bones of 2D6 humans (D3-1)', 
				13: 'Bones of 2D6 animals', 
				14: 'Graveyard (D4-1)', 
				15: 'Corpse of Lone Wanderer (roll) ', 
				16: 'Impaled human corpse', 
				17: 'Corpse of Survivalist (2D-2)', 
				18: 'Hangar w. 4D remains (3D-3)'}
	trp_amb = { 3: 'Anti-Tank', 
				4: 'Mine Rockslide Trap', 
				5: 'Gas Trap', 
				6: 'Poison Dart-Thrower', 
				7: 'Anti-personnel Mine', 
				8: 'Tripwire but no mine', 
				9: 'Pit with sharp sticks ', 
				10: 'Rabbit Snare', 
				11: 'Mousetrap', 
				12: 'Bear-Trap', 
				13: 'Man-snare', 
				14: 'Grenade Trap', 
				15: 'Large Cage with Bait', 
				16: 'Used up Trap (roll again for type)', 
				17: 'Car-bomb', 
				18: 'Treasure Ambush Trap' }
	rai_slv = 'Raiders or Slavers'
	sup_mut = 'Super Mutants or Cannibals'
	fortifc = 'Fortification'
	mil_unt = { 3: 'Four PCA squad with HMGs', 
				4: 'Two PCA Troopers', 
				5: 'Special Ops Squad', 
				6: 'Paratroopers', 
				7: 'Two Armed Dune Buggies', 
				8: 'Ten Man Squad', 
				9: 'Five Man Squad ', 
				10: 'Two Man Patrol', 
				11: 'Five Man Squad', 
				12: 'Ten Man Squad', 
				13: 'Two HUMVEEs', 
				14: 'Two APCs', 
				15: 'Four APCs', 
				16: 'Chopper Transport + Gunship', 
				17: 'AFV formation (4 AFVs)', 
				18: 'Jetfighter Wing of 2' }
	
	v1 = { 3: ((roll_dice(2,6)-2)*100), 
				4: ((roll_dice(1,6)-1)*10), 
				5: (roll_dice(1,10)-1), 
				6: (roll_dice(2,4)-2), 
				7: (roll_dice(1,8)-1), 
				8: (roll_dice(1,6)-1), 
				9: (roll_dice(1,4)-1), 
				10: (roll_dice(1,3)-1), 
				11: (roll_dice(1,4)-1), 
				12: (roll_dice(1,6)-1), 
				13: (roll_dice(1,8)-1), 
				14: (roll_dice(2,4)-2), 
				15: (roll_dice(2,6)-2), 
				16: (roll_dice(1,10)-1), 
				17: ((roll_dice(1,6)-1)*10), 
				18: ((roll_dice(1,6)-1)*10) }
	v2 = { 3: (roll_dice(2,6)-2), 
				4: (roll_dice(3,6)-3), 
				5: (roll_dice(3,6)-3), 
				6: (roll_dice(1,6)-1), 
				7: (roll_dice(1,3)-1), 
				8: (roll_dice(1,3)-1), 
				9: (roll_dice(1,4)-1), 
				10: (roll_dice(1,3)-1), 
				11: (roll_dice(1,2)-1), 
				12: (roll_dice(1,4)-1), 
				13: (roll_dice(2,4)-2), 
				14: (roll_dice(2,6)-2), 
				15: (roll_dice(1,2)-1), 
				16: (roll_dice(3,6)-3), 
				17: (roll_dice(2,6)-2), 
				18: (roll_dice(1,6)-1)}
	v3 = { 3: (roll_dice(4,6)-4), 
				4: (roll_dice(2,6)-2), 
				5: (roll_dice(1,6)-1), 
				6: '?', 
				7: 0, 
				8: (roll_dice(1,3)-1), 
				9: (roll_dice(1,2)-1), 
				10: 0, 
				11: (roll_dice(1,2)-1), 
				12: (roll_dice(1,3)-1), 
				13: 0, 
				14: (roll_dice(1,4)-1), 
				15: '?', 
				16: 0, 
				17: (roll_dice(2,6)-2), 
				18: (roll_dice(3,6)-3)}
	
	corpses = { 3: roll_dice(4,6), 
				4: 1, 
				5: 1, 
				6: 1, 
				7: roll_dice(2,6), 
				8: roll_dice(2,6), 
				9: 1, 
				10: 1, 
				11: 0, 
				12: roll_dice(2,6), 
				13: roll_dice(2,6), 
				14: '?', 
				15: 1, 
				16: 1, 
				17: 1, 
				18: roll_dice(4,6)}
	

	i = 1

	while i <= num:
		print i, '-------------------------------------------'
		result_of_roll=roll_dice(3,6)
		result_of_roll2=roll_dice(3,6)
	
		if result_of_roll==3:
			print '  ', spc_enc
		elif result_of_roll==4:
			print '  ', mov_veh[result_of_roll2]
		elif result_of_roll==5:
			print '  ', sml_set
		elif result_of_roll==6:
			print '  ', lon_wan [result_of_roll2]
		elif result_of_roll==7:
			print '  ', caravan
		elif result_of_roll==8:
			print '  ', ruins[result_of_roll2]
		elif result_of_roll==9:
			print '  ', veh_jun[result_of_roll2]
		elif result_of_roll==10:
			print '  ', animals[result_of_roll2]
		elif result_of_roll==11:
			print '  ', remains[result_of_roll2]
		elif result_of_roll==12:
			print '  ', ruins[result_of_roll2]
		elif result_of_roll==13:
			print '  ', trp_amb[result_of_roll2]
		elif result_of_roll==14:
			print '  ', rai_slv
		elif result_of_roll==15:
			print '  ', sup_mut
		elif result_of_roll==16:
			print '  ', fortifc
		elif result_of_roll==17:
			print '  ', mil_unt[result_of_roll2]
		else:
			print '  ', spc_enc
	
		if result_of_roll == 8:
			print '   ', v1[result_of_roll2], 'useful items'
		elif result_of_roll == 9:
			print '   ', v2[result_of_roll2], 'useful items'
		elif result_of_roll == 11:
			print '   ', corpses[result_of_roll2], 'corpses'
			print '   ', v3[result_of_roll2], 'useful items'
		elif result_of_roll == 12: 
			print '   ', v1[result_of_roll2], 'useful items'

		i += 1

	return''


line = 0
number = 0

while True:
    try:
    	print '\nEnter number of random encounters:'
        line = raw_input('> ')

        if line == 'exit':
            print  'Done.'
            break

        number = int(line)
        print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        print random_enc(number)
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    except :
        print('Not a number.\n')
