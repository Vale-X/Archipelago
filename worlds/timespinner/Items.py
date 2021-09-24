from typing import Dict, Tuple, NamedTuple

class ItemData(NamedTuple):
    category: str
    code: int
    count: int = 1
    progression: bool = False

# A lot of items arent normally dropped by the randomizer as they are mostly enemy drops, but they can be enabled if desired
item_table: Dict[str, ItemData] = {
    'Eternal Crown': ItemData('Equipment', 1337000),
    #'Security Visor': ItemData('Equipment', 1337001),
    #'Engineer Goggles': ItemData('Equipment', 1337002),
    #'Leather Helmet': ItemData('Equipment', 1337003),
    #'Copper Helmet': ItemData('Equipment', 1337004),
    'Pointy Hat': ItemData('Equipment', 1337005),
    #'Dragoon Helmet': ItemData('Equipment', 1337006),
    'Buckle Hat': ItemData('Equipment', 1337007),
    #'Advisor Hat': ItemData('Equipment', 1337008),
    'Librarian Hat': ItemData('Equipment', 1337009),
    #'Combat Helmet': ItemData('Equipment', 1337010),
    'Captain\'s Cap': ItemData('Equipment', 1337011),
    'Lab Glasses': ItemData('Equipment', 1337012),
    'Empire Crown': ItemData('Equipment', 1337013),
    'Viletian Crown': ItemData('Equipment', 1337014),
    #'Sunglasses': ItemData('Equipment', 1337015),
    'Old Coat': ItemData('Equipment', 1337016),
    #'Trendy Jacket': ItemData('Equipment', 1337017),
    #'Security Vest': ItemData('Equipment', 1337018),
    #'Leather Jerkin': ItemData('Equipment', 1337019),
    #'Copper Breastplate': ItemData('Equipment', 1337020),
    'Traveler\'s Cloak': ItemData('Equipment', 1337021),
    #'Dragoon Armor': ItemData('Equipment', 1337022),
    'Midnight Cloak': ItemData('Equipment', 1337023),
    #'Advisor Robe': ItemData('Equipment', 1337024),
    'Librarian Robe': ItemData('Equipment', 1337025),
    #'Military Armor': ItemData('Equipment', 1337026),
    'Captain\'s Uniform': ItemData('Equipment', 1337027),
    'Lab Coat': ItemData('Equipment', 1337028),
    'Empress Robe': ItemData('Equipment', 1337029),
    'Princess Dress': ItemData('Equipment', 1337030),
    'Eternal Coat': ItemData('Equipment', 1337031),
    #'Synthetic Plume': ItemData('Equipment', 1337032),
    #'Cheveur Plume': ItemData('Equipment', 1337033),
    'Metal Wristband': ItemData('Equipment', 1337034),
    #'Nymph Hairband': ItemData('Equipment', 1337035),
    #'Mother o\' Pearl': ItemData('Equipment', 1337036),
    'Bird Statue': ItemData('Equipment', 1337037),
    #'Chaos Stole': ItemData('Equipment', 1337038),
    'Pendulum': ItemData('Equipment', 1337039),
    #'Chaos Horn': ItemData('Equipment', 1337040),
    'Filigree Clasp': ItemData('Equipment', 1337041),
    #'Azure Stole': ItemData('Equipment', 1337042),
    'Ancient Coin': ItemData('Equipment', 1337043),
    #'Shiny Rock': ItemData('Equipment', 1337044),
    'Galaxy Earrings': ItemData('Equipment', 1337045),
    'Selen\'s Bangle': ItemData('Equipment', 1337046),
    'Glass Pumpkin': ItemData('Equipment', 1337047),
    'Gilded Egg': ItemData('Equipment', 1337048),
    'Meyef': ItemData('Familiar', 1337049),
    'Griffin': ItemData('Familiar', 1337050),
    'Merchant Crow': ItemData('Familiar', 1337051),
    'Kobo': ItemData('Familiar', 1337052),
    'Sprite': ItemData('Familiar', 1337053),
    'Demon': ItemData('Familiar', 1337054),
    'Potion': ItemData('UseItem', 1337055, 0),
    'Ether': ItemData('UseItem', 1337056, 0),
    'Sand Vial': ItemData('UseItem', 1337057, 0),
    'Hi-Potion': ItemData('UseItem', 1337058, 0),
    'Hi-Ether': ItemData('UseItem', 1337059, 0),
    'Sand Bottle': ItemData('UseItem', 1337060, 0),
    'Berry Pick-Mi-Up': ItemData('UseItem', 1337061, 0),
    'Berry Pick-Mi-Up+': ItemData('UseItem', 1337062, 0),
    'Mind Refresh': ItemData('UseItem', 1337063, 0),
    'Mind Refresh ULTRA': ItemData('UseItem', 1337064, 0),
    'Antidote': ItemData('UseItem', 1337065, 0),
    'Chaos Rose': ItemData('UseItem', 1337066, 0),
    'Warp Shard': ItemData('UseItem', 1337067),
    #'Dream Wisp': ItemData('UseItem', 1337068),
    #'PlaceHolderItem1': ItemData('UseItem', 1337069),
    #'Lachiemi Sun': ItemData('UseItem', 1337070),
    'Jerky': ItemData('UseItem', 1337071),
    #'Biscuit': ItemData('UseItem', 1337072),
    #'Fried Cheveur': ItemData('UseItem', 1337073),
    #'Sautéed Wyvern Tail': ItemData('UseItem', 1337074),
    #'Unagi Roll': ItemData('UseItem', 1337075),
    #'Cheveur au Vin': ItemData('UseItem', 1337076),
    #'Royal Casserole': ItemData('UseItem', 1337077),
    'Spaghetti': ItemData('UseItem', 1337078),
    #'Plump Maggot': ItemData('UseItem', 1337079),
    #'Orange Juice': ItemData('UseItem', 1337080),
    'Filigree Tea': ItemData('UseItem', 1337081),
    #'Empress Cake': ItemData('UseItem', 1337082),
    #'Rotten Tail': ItemData('UseItem', 1337083),
    #'Alchemy Tools': ItemData('UseItem', 1337084),
    'Galaxy Stone': ItemData('UseItem', 1337085),
    #1337086 Used interally
    #'Essence Crystal': ItemData('UseItem', 1337087),
    #'Gold Ring': ItemData('UseItem', 1337088),
    #'Gold Necklace': ItemData('UseItem', 1337089),
    'Herb': ItemData('UseItem', 1337090),
    #'Mushroom': ItemData('UseItem', 1337091),
    #'Plasma Crystal': ItemData('UseItem', 1337092),
    'Plasma IV Bag': ItemData('UseItem', 1337093),
    #'Cheveur Drumstick': ItemData('UseItem', 1337094),
    #'Wyvern Tail': ItemData('UseItem', 1337095),
    #'Eel Meat': ItemData('UseItem', 1337096),
    #'Cheveux Breast': ItemData('UseItem', 1337097),
    'Food Synthesizer': ItemData('UseItem', 1337098),
    #'Cheveux Feather': ItemData('UseItem', 1337099),
    #'Siren Ink': ItemData('UseItem', 1337100),
    #'Plasma Core': ItemData('UseItem', 1337101),
    #'Silver Ore': ItemData('UseItem', 1337102),
    #'Historical Documents': ItemData('UseItem', 1337103),
    #'MapReveal 0': ItemData('UseItem', 1337104),
    #'MapReveal 1': ItemData('UseItem', 1337105),
    #'MapReveal 2': ItemData('UseItem', 1337106),
    'Timespinner Wheel': ItemData('Relic', 1337107, progression=True),
    'Timespinner Spindle': ItemData('Relic', 1337108, progression=True),
    'Timespinner Gear 1': ItemData('Relic', 1337109, progression=True),
    'Timespinner Gear 2': ItemData('Relic', 1337110, progression=True),
    'Timespinner Gear 3': ItemData('Relic', 1337111, progression=True),
    'Twin Pyramid Key': ItemData('Relic', 1337112, progression=True),
    'Celestial Sash': ItemData('Relic', 1337113, progression=True),
    'Succubus Hairpin': ItemData('Relic', 1337114, progression=True),
    'Talaria Attachment': ItemData('Relic', 1337115, progression=True),
    'Water Mask': ItemData('Relic', 1337116, progression=True),
    'Gas Mask': ItemData('Relic', 1337117, progression=True),
    'Soul Scanner': ItemData('Relic', 1337118),
    'Security Keycard A': ItemData('Relic', 1337119, progression=True),
    'Security Keycard B': ItemData('Relic', 1337120, progression=True),
    'Security Keycard C': ItemData('Relic', 1337121, progression=True),
    'Security Keycard D': ItemData('Relic', 1337122, progression=True),
    'Library Keycard V': ItemData('Relic', 1337123, progression=True),
    'Tablet': ItemData('Relic', 1337124, progression=True),
    'Elevator Keycard': ItemData('Relic', 1337125, progression=True),
    'Jewelry Box': ItemData('Relic', 1337126),
    'Goddess Brooch': ItemData('Relic', 1337127),
    'Wyrm Brooch': ItemData('Relic', 1337128), 	
    'Greed Brooch': ItemData('Relic', 1337129),
    'Eternal Brooch': ItemData('Relic', 1337130),
    'Blue Orb': ItemData('Orb Melee', 1337131),
    'Blade Orb': ItemData('Orb Melee', 1337132),
    'Fire Orb': ItemData('Orb Melee', 1337133, progression=True),
    'Plasma Orb': ItemData('Orb Melee', 1337134, progression=True),
    'Iron Orb': ItemData('Orb Melee', 1337135),
    'Ice Orb': ItemData('Orb Melee', 1337136),
    'Wind Orb': ItemData('Orb Melee', 1337137),
    'Gun Orb': ItemData('Orb Melee', 1337138),
    'Umbra Orb': ItemData('Orb Melee', 1337139),
    'Empire Orb': ItemData('Orb Melee', 1337140),
    'Eye Orb': ItemData('Orb Melee', 1337141),
    'Blood Orb': ItemData('Orb Melee', 1337142),
    'Forbidden Tome': ItemData('Orb Melee', 1337143),
    'Shattered Orb': ItemData('Orb Melee', 1337144),
    'Nether Orb': ItemData('Orb Melee', 1337145),
    'Radiant Orb': ItemData('Orb Melee', 1337146),
    'Aura Blast': ItemData('Orb Spell', 1337147),
    'Colossal Blade': ItemData('Orb Spell', 1337148),
    'Infernal Flames': ItemData('Orb Spell', 1337149, progression=True),
    'Plasma Geyser': ItemData('Orb Spell', 1337150, progression=True),
    'Colossal Hammer': ItemData('Orb Spell', 1337151),
    'Frozen Spires': ItemData('Orb Spell', 1337152),
    'Storm Eye': ItemData('Orb Spell', 1337153),
    'Arm Cannon': ItemData('Orb Spell', 1337154),
    'Dark Flames': ItemData('Orb Spell', 1337155),
    'Aura Serpent': ItemData('Orb Spell', 1337156),
    'Chaos Blades': ItemData('Orb Spell', 1337157),
    'Crimson Vortex': ItemData('Orb Spell', 1337158),
    'Djinn Inferno': ItemData('Orb Spell', 1337159, progression=True),
    'Bombardment': ItemData('Orb Spell', 1337160),
    'Corruption': ItemData('Orb Spell', 1337161),
    'Lightwall': ItemData('Orb Spell', 1337162, progression=True),
    'Bleak Ring': ItemData('Orb Passive', 1337163),
    'Scythe Ring': ItemData('Orb Passive', 1337164),
    'Pyro Ring': ItemData('Orb Passive', 1337165, progression=True),
    'Royal Ring': ItemData('Orb Passive', 1337166, progression=True),
    'Shield Ring': ItemData('Orb Passive', 1337167),
    'Icicle Ring': ItemData('Orb Passive', 1337168),
    'Tailwind Ring': ItemData('Orb Passive', 1337169),
    'Economizer Ring': ItemData('Orb Passive', 1337170),
    'Dusk Ring': ItemData('Orb Passive', 1337171),
    'Star of Lachiem': ItemData('Orb Passive', 1337172),
    'Oculus Ring': ItemData('Orb Passive', 1337173, progression=True),
    'Sanguine Ring': ItemData('Orb Passive', 1337174),
    'Sun Ring': ItemData('Orb Passive', 1337175),
    'Silence Ring': ItemData('Orb Passive', 1337176),
    'Shadow Seal': ItemData('Orb Passive', 1337177),
    'Hope Ring': ItemData('Orb Passive', 1337178),
    'Max HP': ItemData('Stat', 1337179, 12),
    'Max Aura': ItemData('Stat', 1337180, 13),
    # 1337181 - 1337248 Reserved
    'Max Sand': ItemData('Stat', 1337249, 14)
}

starter_melee_weapons: Tuple[str] = (
    'Blue Orb',
    'Blade Orb',
    'Fire Orb',
    'Iron Orb',
    'Ice Orb',
    'Wind Orb',
    'Gun Orb',
    'Umbra Orb',
    'Empire Orb',
    'Eye Orb',
    'Blood Orb',
    'Forbidden Tome',
    'Shattered Orb',
    'Nether Orb',
    'Radiant Orb'
)

starter_spells: Tuple[str] = (
    'Colossal Blade',
    'Infernal Flames',
    'Plasma Geyser',
    'Colossal Hammer',
    'Frozen Spires',
    'Storm Eye',
    'Arm Cannon',
    'Dark Flames',
    'Aura Serpent',
    'Chaos Blades',
    'Crimson Vortex',
    'Djinn Inferno',
    'Bombardment',
    'Corruption'
)

# weighted
starter_progression_items: Tuple[str] = (
    'Talaria Attachment',
    'Talaria Attachment',
    'Succubus Hairpin',
    'Succubus Hairpin',
    'Timespinner Wheel',
    'Timespinner Wheel',
    'Twin Pyramid Key',
    'Celestial Sash',
    'Lightwall'
)

filler_items: Tuple[str] = (
    'Potion',
    'Ether',
    'Hi-Potion',
    'Hi-Ether',
    'Sand Vial',
    'Sand Bottle',
    'Berry Pick-Mi-Up',
    'Berry Pick-Mi-Up+',
    'Mind Refresh',
    'Mind Refresh ULTRA',
    'Antidote',
    'Chaos Rose'
)