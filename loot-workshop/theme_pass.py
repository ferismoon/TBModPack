"""Author the reviewed theme pass. Config changes only; build.py publishes outputs."""
import json, re
from pathlib import Path
R=Path(__file__).resolve().parent
evidence=set(json.loads((R/'structure-item-evidence.json').read_text()))
profiles=json.loads((R/'structure-rewards.json').read_text())
def entries(ns,names,count=1,weight=2):
    result=[]
    for name in names.split():
        id=ns+':'+name
        assert id in evidence, id
        result.append(dict(item=id,count=count,weight=weight))
    return result
parts=entries('create','shaft cogwheel large_cogwheel andesite_casing andesite_funnel gearbox',1)
raw=entries('create','zinc_ingot andesite_alloy iron_sheet copper_sheet crushed_raw_iron crushed_raw_copper crushed_raw_zinc',2)
seeds=entries('farmersdelight','tomato_seeds cabbage_seeds rice',2)+entries('expandeddelight','asparagus_seeds chili_pepper_seeds peanut sweet_potato',2)+entries('farm_and_charm','barley_seeds oat_seeds lettuce_seeds',2)+entries('brewery','hops_seeds hops dried_barley',2)
food=entries('farmersdelight','chicken_soup beef_stew vegetable_soup stuffed_potato')+entries('expandeddelight','cheese_sandwich apple_juice sweet_roll asparagus_soup')+entries('candlelight','tomato_soup mushroom_soup')+entries('brewery','pretzel dumplings potato_salad beer_wheat beer_barley beer_oat')+entries('herbalbrews','black_tea green_tea hibiscus_tea lavender_tea')
herbs=entries('hexalia','lavender mandrake_seeds rabbage_seeds chillberries galeberries fragrant_nectar',2)
brews=entries('hexalia','brew_of_arachnid_grace brew_of_bloodlust brew_of_daybloom brew_of_hollow_silence brew_of_homestead brew_of_siphon brew_of_slimewalker brew_of_spikeskin')
machines=entries('create','mechanical_drill mechanical_saw mechanical_harvester mechanical_plough mechanical_pump mechanical_press brass_casing electron_tube',1,1)
def unique(rows):return list({r['item']:r for r in rows}.values())
def put(name,rows,chance=1,bonus=None):
    profiles[name]=dict(chance=chance,items=unique(rows))
    if bonus:profiles[name]['bonus']=bonus
# Broad ordinary supplies; common alternatives have equal weights.
put('village',seeds+food+parts+herbs)
put('easy',raw+parts+seeds+food+herbs)
put('medium',raw+parts+food+herbs+brews,1,'parts_bonus')
put('parts_bonus',machines,0.08)
put('farm',seeds+food+entries('farmersdelight','rope canvas',2))
put('kitchen',food+entries('expandeddelight','ground_salt ground_cinnamon cheese_slice asparagus chili_pepper',2))
put('workshop',raw+parts,1,'parts_bonus')
put('magic',herbs+brews+entries('herbalbrews','black_tea green_tea lavender_tea'),1,'magic_bonus')
put('magic_bonus',entries('hexalia','celestial_crystal athame briar_sickle'),0.06)
put('navigation',entries('farmersdelight','rope canvas',2)+entries('create','shaft cogwheel',2),1,'compass_bonus')
put('compass_bonus',entries('naturescompass','naturescompass',1,3)+entries('explorerscompass','explorerscompass',1,1),0.10)
put('water',entries('oceansdelight','cooked_stuffed_cod squid_rings honey_fried_kelp seagrass_salad guardian_soup')+entries('create','zinc_ingot copper_sheet iron_sheet',2)+entries('farmersdelight','rope canvas',3),1,'water_bonus')
put('water_bonus',entries('create','copper_diving_helmet copper_diving_boots copper_backtank mechanical_pump'),0.06)
obsidian=entries('obsidianequipmentrework','obsidian_helmet obsidian_chestplate obsidian_leggings obsidian_boots')
netherite=entries('minecraft','netherite_helmet netherite_chestplate netherite_leggings netherite_boots netherite_pickaxe netherite_sword',1,1)
put('gear_bonus',obsidian+netherite,0.04)
put('armoury',raw+parts+entries('create','brass_ingot iron_sheet',2),1,'gear_bonus')
put('hard',raw+food+brews+entries('create','brass_ingot golden_sheet',2),1,'gear_bonus')
put('nether',entries('nethersdelight','hoglin_loin propelpearl',2)+brews+entries('create','brass_ingot golden_sheet electron_tube railway_casing mechanical_press',1)+entries('brewery','dark_brew beer_nettle'),0.85,'gear_bonus')
put('end_bonus',entries('mythicupgrades','topaz_ingot aquamarine_ingot ametrine_ingot',1,3)+obsidian+netherite,0.10)
put('end',entries('betterend','crystal_shards',2)+entries('ends_delight','chorus_fruit_pie_slice chorus_flower_tea chorus_fruit_wine bubble_tea')+brews+entries('create','brass_ingot electron_tube precision_mechanism',1),1,'end_bonus')
routes=json.loads((R/'structure-routes.json').read_text())
changes=[]
for row in routes['routes']:
    id=row['target']; ns,path=id.split(':',1); words=set(re.split(r'[/_.-]',path))
    old=row['profile']; new=old
    # Correct dimensions by provider before assigning overworld themes.
    if ns in ('mes','betterend','ends_delight') or 'end_city' in path or ns=='structory_towers' and path=='end_tower':new='end'
    elif ns in ('mns','incendium','betterfortresses') or 'nether' in words or 'bastion' in words:new='nether'
    elif ns=='deeperdarker':new='hard'
    elif words & {'map','cartographer','navigation'}:new='navigation'
    elif old not in ('end','nether'):
        if words & {'witch','witches','magic','brewing','alchemist'}:new='magic'
        elif words & {'armoury','armory','weaponry','weapons','barracks'}:new='armoury'
        elif words & {'farm','farmer','botanist','forager','garden','greenhouse'}:new='farm'
        elif words & {'bakery','kitchen','food','tavern','butcher'}:new='kitchen'
        elif words & {'smith','weaponsmith','toolsmith','blacksmith','workshop','mineshaft','mineshafts','mine'}:new='workshop'
    if old!=new:changes.append({'table':id,'from':old,'to':new})
    row['profile']=new
if not any(r['target']=='minecraft:chests/end_city_treasure' for r in routes['routes']):routes['routes'].append({'target':'minecraft:chests/end_city_treasure','profile':'end'})
for p in profiles.values():
    assert p['items']
    if 'bonus' in p:assert p['bonus'] in profiles
(R/'structure-rewards.json').write_text(json.dumps(profiles,indent=2)+'\n')
(R/'structure-routes.json').write_text(json.dumps(routes,indent=2)+'\n')
(R/'reports/theme-pass.json').write_text(json.dumps({'changes':changes,'choices':{k:len(v['items']) for k,v in profiles.items()}},indent=2)+'\n')
print(f'{len(profiles)} profiles, {len(changes)} themed route changes, {len({e["item"] for p in profiles.values() for e in p["items"]})} unique rewards')
