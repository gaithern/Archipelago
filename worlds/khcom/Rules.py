from BaseClasses import CollectionState, MultiWorld, LocationProgressType
from .Locations import get_locations_by_category

#def has_room_of_beginnings(state: CollectionState, player: int, floor_num) -> bool:
#    return state.has("Key of Beginnings F" + floor_num, player)
#
#def has_room_of_guidance(state: CollectionState, player: int, floor_num) -> bool:
#    return state.has_all({"Key of Beginnings F" + floor_num, "Key of Guidance F" + floor_num}, player)
#
#def has_room_of_truth(state: CollectionState, player: int, floor_num) -> bool:
#    return state.has_all({"Key of Beginnings F" + floor_num, "Key of Guidance F" + floor_num, "Key to Truth F" + floor_num}, player)

def has_x_worlds(state: CollectionState, player: int, num_of_worlds) -> bool:
    locations = 0
    if has_item(state, player,"World Card Wonderland"):
        locations = locations + 1
    if has_item(state, player,"World Card Olympus Coliseum"):
        locations = locations + 1
    if has_item(state, player,"World Card Monstro"):
        locations = locations + 1
    if has_item(state, player,"World Card Agrabah"):
        locations = locations + 1
    if has_item(state, player,"World Card Halloween Town"):
        locations = locations + 1
    if has_item(state, player,"World Card Atlantica"):
        locations = locations + 1
    if has_item(state, player,"World Card Neverland"):
        locations = locations + 1
    if has_item(state, player,"World Card Hollow Bastion"):
        locations = locations + 1
    if has_item(state, player,"World Card 100 Acre Wood"):
        locations = locations + 1
    if has_item(state, player,"World Card Twilight Town"):
        locations = locations + 1
    if has_item(state, player,"World Card Destiny Islands"):
        locations = locations + 1
    if has_item(state, player,"World Card Castle Oblivion"):
        locations = locations + 1
    if locations > num_of_worlds:
        return True
    return False

def has_item(state: CollectionState, player: int, item) -> bool:
    return state.has(item, player)

def set_rules(multiworld: MultiWorld, player: int):
    #Location rules.
    #Keys
    multiworld.get_location("F01 Traverse Town Room of Rewards (Attack Cards Lionheart)"         , player).access_rule = lambda state: has_item(state, player,"Key to Rewards Traverse Town")
    multiworld.get_location("F03 Olympus Coliseum Room of Rewards (Attack Card Metal Chocobo)"   , player).access_rule = lambda state: has_item(state, player,"Key to Rewards Olympus Coliseum")
    multiworld.get_location("F09 Hollow Bastion Room of Rewards (Characters I Mushu)"            , player).access_rule = lambda state: has_item(state, player,"Key to Rewards Hollow Bastion")
    multiworld.get_location("F09 Hollow Bastion Room of Rewards (Magic Cards Mushu)"             , player).access_rule = lambda state: has_item(state, player,"Key to Rewards Hollow Bastion")
    
    multiworld.get_location("Heartless Air Pirate"                                               , player).access_rule = lambda state: has_item(state, player,"World Card Neverland")
    multiworld.get_location("Heartless Air Soldier"                                              , player).access_rule = lambda state: has_item(state, player,"World Card Monstro") or has_item(state, player,"World Card Agrabah") or has_item(state, player,"World Card Halloween Town") or has_item(state, player,"World Card Destiny Islands")
    multiworld.get_location("Heartless Aquatank"                                                 , player).access_rule = lambda state: has_item(state, player,"World Card Atlantica")
    multiworld.get_location("Heartless Bandit"                                                   , player).access_rule = lambda state: has_item(state, player,"World Card Agrabah")
    multiworld.get_location("Heartless Barrel Spider"                                            , player).access_rule = lambda state: has_item(state, player,"World Card Monstro") or has_item(state, player,"World Card Agrabah") or has_item(state, player,"World Card Neverland") or has_item(state, player,"World Card Destiny Islands")
    multiworld.get_location("Heartless Bouncywild"                                               , player).access_rule = lambda state: has_item(state, player,"World Card Olympus Coliseum")
    multiworld.get_location("Heartless Creeper Plant"                                            , player).access_rule = lambda state: has_item(state, player,"World Card Wonderland") or has_item(state, player,"World Card Halloween Town") or has_item(state, player,"World Card Destiny Islands")
    multiworld.get_location("Heartless Crescendo"                                                , player).access_rule = lambda state: has_item(state, player,"World Card Wonderland") or has_item(state, player,"World Card Neverland") or has_item(state, player,"World Card Destiny Islands")
    multiworld.get_location("Heartless Darkball"                                                 , player).access_rule = lambda state: has_item(state, player,"World Card Atlantica") or has_item(state, player,"World Card Neverland") or has_item(state, player,"World Card Destiny Islands") or has_item(state, player,"World Card Castle Oblivion")
    multiworld.get_location("Heartless Defender"                                                 , player).access_rule = lambda state: has_item(state, player,"World Card Hollow Bastion") or has_item(state, player,"World Card Castle Oblivion")
    multiworld.get_location("Heartless Fat Bandit"                                               , player).access_rule = lambda state: has_item(state, player,"World Card Agrabah")
    multiworld.get_location("Heartless Gargoyle"                                                 , player).access_rule = lambda state: has_item(state, player,"World Card Halloween Town")
    multiworld.get_location("Heartless Green Requiem"                                            , player).access_rule = lambda state: has_item(state, player,"World Card Monstro") or has_item(state, player,"World Card Agrabah") or has_item(state, player,"World Card Castle Oblivion")
    multiworld.get_location("Heartless Large Body"                                               , player).access_rule = lambda state: has_item(state, player,"World Card Wonderland") or has_item(state, player,"World Card Olympus Coliseum")
    multiworld.get_location("Heartless Neoshadow"                                                , player).access_rule = lambda state: has_item(state, player,"World Card Castle Oblivion")
    multiworld.get_location("Heartless Pirate"                                                   , player).access_rule = lambda state: has_item(state, player,"World Card Neverland")
    multiworld.get_location("Heartless Powerwild"                                                , player).access_rule = lambda state: has_item(state, player,"World Card Olympus Coliseum")
    multiworld.get_location("Heartless Screwdiver"                                               , player).access_rule = lambda state: has_item(state, player,"World Card Atlantica")
    multiworld.get_location("Heartless Sea Neon"                                                 , player).access_rule = lambda state: has_item(state, player,"World Card Atlantica")
    multiworld.get_location("Heartless Search Ghost"                                             , player).access_rule = lambda state: has_item(state, player,"World Card Monstro") or has_item(state, player,"World Card Atlantica")
    multiworld.get_location("Heartless Tornado Step"                                             , player).access_rule = lambda state: has_item(state, player,"World Card Monstro") or has_item(state, player,"World Card Hollow Bastion") or has_item(state, player,"World Card Destiny Islands")
    multiworld.get_location("Heartless Wight Knight"                                             , player).access_rule = lambda state: has_item(state, player,"World Card Halloween Town")
    multiworld.get_location("Heartless Wizard"                                                   , player).access_rule = lambda state: has_item(state, player,"World Card Hollow Bastion") or has_item(state, player,"World Card Castle Oblivion")
    multiworld.get_location("Heartless Wyvern"                                                   , player).access_rule = lambda state: has_item(state, player,"World Card Hollow Bastion") or has_item(state, player,"World Card Castle Oblivion")
    multiworld.get_location("Heartless Yellow Opera"                                             , player).access_rule = lambda state: has_item(state, player,"World Card Monstro") or has_item(state, player,"World Card Agrabah") or has_item(state, player,"World Card Neverland") or has_item(state, player,"World Card Castle Oblivion")
    
    # Region rules.
    multiworld.get_entrance("Floor 2"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Wonderland")
    multiworld.get_entrance("Floor 3"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Olympus Coliseum")
    multiworld.get_entrance("Floor 4"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Monstro")
    multiworld.get_entrance("Floor 5"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Agrabah")
    multiworld.get_entrance("Floor 6"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Halloween Town")
    multiworld.get_entrance("Floor 7"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Atlantica")
    multiworld.get_entrance("Floor 8"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Neverland")
    multiworld.get_entrance("Floor 9"                                                            , player).access_rule = lambda state: has_item(state, player,"World Card Hollow Bastion")
    multiworld.get_entrance("Floor 10"                                                           , player).access_rule = lambda state: has_item(state, player,"World Card 100 Acre Wood")
    multiworld.get_entrance("Floor 11"                                                           , player).access_rule = lambda state: has_item(state, player,"World Card Twilight Town") and has_x_worlds(state, player, 5)
    multiworld.get_entrance("Floor 12"                                                           , player).access_rule = lambda state: has_item(state, player,"World Card Destiny Islands") and has_x_worlds(state, player, 7)
    multiworld.get_entrance("Floor 13"                                                           , player).access_rule = lambda state: has_item(state, player,"World Card Castle Oblivion") and has_x_worlds(state, player, 9)
    
    
    
    # Win condition.
    multiworld.completion_condition[player] = lambda state: state.has_all({"Friend Card Donald", "Friend Card Goofy", "Friend Card Aladdin", "Friend Card Ariel", "Friend Card Beast", "Friend Card Jack", "Friend Card Peter Pan"}, player)
