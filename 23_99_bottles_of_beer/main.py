
def bottle_song(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall,")
            print(f"{bottles} bottles of beer,")
        else:
            print(f"{bottles} bottle of beer on the wall")
            print(f"{bottles} bottle of beer,")
        print("Take one out,")
        print("Pass it around,")
        bottles -= 1
        if bottles > 1:
            print(f"{bottles} bottles of beer left on the wall")
        else: 
            print(f"{bottles} bottle of beer left on the wall")

            
        print("…cut for brevity…")
    print("No more beer!")


bottle_song(3)
