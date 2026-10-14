import math
from typing import List, Dict, Tuple
from helpers import time_to_ms, ms_to_time


def get_number_of_records(data) -> int:

    return len(data)

def get_tracks(data) -> List[str]:
    track_name_list = []
    for Tracks in data:
        if Tracks["Track"] in track_name_list:
            continue
        else:
            track_name_list.append(Tracks["Track"])

    return track_name_list


def get_fastest_track(data) -> str:
    time = []
    for i in range(len(data)):
        time.append(time_to_ms(data[i]["Time"]))

    indx=time.index(min(time))
    fastest_track = data[indx]["Track"]

    
    return fastest_track


def get_number_of_records_by_player(data) -> Dict[str, int]:
    world_records_by_player = {}

    for Tracks in data:
        if Tracks["Player"] in world_records_by_player:
            world_records_by_player[Tracks["Player"]]+=1
            continue
            
        else:
            world_records_by_player[Tracks["Player"]] = 1 
    
    return world_records_by_player


def get_player_with_most_records(data) -> str:
    world_records_by_player = get_number_of_records_by_player(data)

    max_key = max(world_records_by_player, key=world_records_by_player.get)

    
    return max_key


def get_most_common_characters_without_hc(data) -> List[Tuple[str, int]]:


    def get_number_of_records_by_character(data):
        world_records_by_character = {}
        
        for Tracks in data:
            print(Tracks["Character"])
            if Tracks["Character"] in world_records_by_character:
                world_records_by_character[Tracks["Character"]]+=1
                continue
                    
            else:
                world_records_by_character[Tracks["Character"]] = 1 
            
        return world_records_by_character





    world_records_by_player = get_number_of_records_by_character(data)
    
    
    for Tracks in data:
        
        if Tracks["Hybrid Controls Used"]=="true":
            world_records_by_player[Tracks["Character"]]-=1
    
    world_records_by_player = dict(sorted(world_records_by_player.items(), key=lambda item: item[1], reverse=True))
    world_records_by_player2 = world_records_by_player.copy()
    for people in world_records_by_player2:

        
        if world_records_by_player[people]==0:
            world_records_by_player.pop(people)
    export_list = []
    for key,value in world_records_by_player.items():
        export_list.append((key, value))
    
    #print(world_records_by_player)

            
   

    return export_list

def mean(numl):
  
    return ###

def stddev(numl):
   
    
    return ###     
    

if __name__ == "__main__":
    from datasets import MARIO_KART_WORLD_RECORDS_DATASET
    import matplotlib.pyplot as plt
    from helpers import mu_vline, sigma_vlines, time_to_ms, ms_to_time
    
    #print(get_number_of_records(MARIO_KART_WORLD_RECORDS_DATASET))
    #print((get_tracks(MARIO_KART_WORLD_RECORDS_DATASET)))
    #print((get_fastest_track(MARIO_KART_WORLD_RECORDS_DATASET)))
    #print((get_number_of_records_by_player(MARIO_KART_WORLD_RECORDS_DATASET)))
    #print((get_player_with_most_records(MARIO_KART_WORLD_RECORDS_DATASET)))
    print((get_most_common_characters_without_hc(MARIO_KART_WORLD_RECORDS_DATASET)))