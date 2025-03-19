import math

def main():
 print("--------------------------------------")
 print("Pythagorous Theorm")
 print("Formula : Hyp = Base^2 + Perp^2")
 print("--------------------------------------")
 
 base : float = float(input("Enter Base : "))
 perp : float = float(input("Enter Perpendicular : "))
 print(f"Base = {base}")
 print(f"Perpendicular = {perp}")
 hyp = math.sqrt(base**2 + perp**2)
 print(f"Hyp = ",hyp)

if __name__ == '__main__':
    main()
