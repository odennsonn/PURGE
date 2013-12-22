Attack = ("Attack", "a6db6f1f-2e80-4a80-9f23-891cc4f95801")
Damage = ("Damage", "a6db6f1f-2e80-4a80-9f23-891cc4f95802")
Armor = ("Armor", "a6db6f1f-2e80-4a80-9f23-891cc4f95803")
Health = ("Health", "a6db6f1f-2e80-4a80-9f23-891cc4f95804")

#---------------------------------------------------------------------------
# Table group actions
#---------------------------------------------------------------------------

def flipCoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("{} flips heads.".format(me))
    else:
        notify("{} flips tails.".format(me))

def announceBA(group, x = 0, y = 0):
	mute()
	notify("**{} DECLARES ATTACK ON BATTLEFIELD VECTOR!**".format(me))

def announceSA(group, x = 0, y = 0):
	mute()
	notify("**{} DECLARES ATTACK ON STRONGHOLD VECTOR!**".format(me))

def holdOn(group, x = 0, y = 0):
	mute()
	notify("**HOLD ON PLEASE. I HAVE AN ACTION/QUESTION**")

def endTurn(group, x = 0, y = 0):
	mute()
	notify("**I PASS**")

def scoop(group, x = 0, y = 0):
	mute()
	
	if not confirm("Return cards to start position?"): return

	for c in me.hand: c.moveTo(me.Deck)
	for c in me.piles['TEK Discard']: c.moveTo (me.piles['TEK Deck'])
	for c in me.piles['OPS Discard']: c.moveTo (me.piles['OPS Deck'])
	for c in me.piles['WAR Discard']: c.moveTo (me.piles['WAR Deck'])

	myCards = (card for card in table
        	if card.owner == me
        	and card.controller == me)

	for card in myCards:
		if card.Type == "Commander": 
			card.moveTo(me.hand)
		elif card.Type == "Stronghold":
			card.moveTo(me.hand)
		elif card.Type == "UNIT": 
			card.moveTo(me.piles['WAR Deck'])
		elif card.Type == "OPS": 
			card.moveTo(me.piles['OPS Deck'])
		else: 
			card.moveTo(me.piles['TEK Deck'])
	
	notify("{} scoops the table.".format(me))


#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------

def flipcard(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} turns {} face down.".format(me, card))
        card.isFaceUp = False
    else:
        card.isFaceUp = True
        notify("{} turns {} face up.".format(me, card))

def addAttack(card, x = 0, y = 0):
    mute()
    notify("{} adds Attack to {}.".format(me, card))
    card.markers[Attack] += 1
    
def addDamage(card, x = 0, y = 0):
    mute()
    notify("{} adds Damage to {}.".format(me, card))
    card.markers[Damage] += 1    
    
def subAttack(card, x = 0, y = 0):
    mute()
    notify("{} subtracts Attack to {}.".format(me, card))
    card.markers[Attack] -= 1
    
def subDamage(card, x = 0, y = 0):
    mute()
    notify("{} subtracts Damage to {}.".format(me, card))
    card.markers[Damage] -= 1    

def addArmor(card, x = 0, y = 0):
    mute()
    notify("{} adds Armor to {}.".format(me, card))
    card.markers[Armor] += 1
    
def addHealth(card, x = 0, y = 0):
    mute()
    notify("{} adds Health to {}.".format(me, card))
    card.markers[Health] += 1    
    
def subArmor(card, x = 0, y = 0):
    mute()
    notify("{} subtracts Armor to {}.".format(me, card))
    card.markers[Armor] -= 1
    
def subHealth(card, x = 0, y = 0):
    mute()
    notify("{} subtracts Health to {}.".format(me, card))
    card.markers[Health] -= 1     


#---------------------------
#movement actions
#---------------------------

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------

def draw(group, x = 0, y = 0):
 if len(group) == 0: return
 mute()
 group[0].moveTo(me.hand)
 notify("{} draws a card.".format(me))

def discardMany (group, count = None):
 if count == None: count = askInteger("Discard how many cards?", 0)
 if (len(group) >= count):    
 	for c in group.top(count): c.moveTo(me.piles['Discard pile'])
 	notify("{} discards {} cards.".format(me, count))
 else:
	notify("Not enough cards.")

def shuffle(group):
  group.shuffle()

def reshuffle(group):
  mute()

  if not confirm("Are you sure? Re-shuffle discard pile back into deck?"): return

  myDeck = me.deck
  for c in group: c.moveTo(myDeck)
  myDeck.shuffle()
  notify("{} shuffles his {} back into his deck.".format(me, group.name))
  

def drawMany(group, count = None):
 if len(group) == 0: return
 mute()
 if count == None: count = askInteger("Draw how many cards?", 7)
 for c in group.top(count): c.moveTo(me.hand)
 notify("{} draws {} cards.".format(me, count))