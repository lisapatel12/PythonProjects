# Driver: Adit Prabhu(U72452636)
#Navigator : Lisa Patel (U5014070)
import random

#current position of hare

print("ON YOUR MARK... GET SET...\nGO!!!!!! \nAND THEY'RE OFF!")

def hare_position(pos):
    next_pos = random.choices(['s' ,'bh', 'bs', 'sh', 'ss'],weights =(0.2,0.2,0.1,0.3,0.2))

    if next_pos == ["s"]:
        return pos
    elif next_pos == ["bh"]:
        return min(pos+7,50)
    elif next_pos == ["bs"]:
        return max(1,pos-10)
    elif next_pos == ["sh"]:
        return min(pos+1,50)
    elif next_pos == ["ss"]:
        return max(pos-2,1)

#current position of tortoise
def tortoise_position(pos):
    next_pos = random.choices(["fp", "s", "sp"], weights =(0,5,0.2,0.3))
    
    if next_pos == ["s"]:
        return max(0,pos-5)
    elif next_pos ==  ["fp"]:
        return min(pos+3,50)
    elif next_pos == ["sp"]:
        return pos

#Current position of distance between T and H so race progress
def display_track(curr_hare,curr_tortoise):
    for i in range(1,51):
        if i == curr_hare:
            print("H", end = "")
            continue
        if i == curr_tortoise:
            print("T", end = "")
        else:
            print(" ", end = "")

    print()

def main():
    track = [" "]*51
    time = 0
    #initalsing the variables to 1
    curr_hare = 1
    curr_tortoise = 1

    while curr_hare < 50 and curr_tortoise < 50:
        #Curr_variable shows the current position
        curr_hare = hare_position(curr_hare)
        curr_tortoise = hare_position(curr_tortoise)
        time+=1
        #display_track displays the track
        display_track(curr_hare,curr_tortoise)

    if curr_hare == 50:
        print("Hare wins. Yay")
    elif curr_tortoise == 50:
        print("Tortoise wins!! Yay!")
    print(f"Time of race : {time} seconds")#ending comments
main()
