
__author__ = "El Mazaz Badr"


import os
from collections import deque, defaultdict



THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file(path: str) -> list[int]:
    with open(path) as f:
        return f.readlines()

def get_inner_bags(bag: str) -> set[str]:
    #dim coral bags contain 1 shiny maroon bag, 2 bright orange bags, 3 clear lavender bags.
    inner_bags = {" ".join(inner_bag.strip().split(" ")[1:3]) for inner_bag in bag.split("contain")[1].split(",") if "other bags." not in " ".join(inner_bag.strip().split(" ")[1:3])}
    return inner_bags


def get_inner_bags2(bags: str) -> set[str]:
    #dim coral bags contain 1 shiny maroon bag, 2 bright orange bags, 3 clear lavender bags.
    #{bag.strip().split("contain")[1].strip():{"".join(x.split(" ")[1:3]):int(x.split(" ")[0]+"0")} for bag in bags for x in bag.strip().split("contain")[1].split(",") if "other bags." not in x}
    r = defaultdict(lambda: [])
    for bag in bags:
        k,inner_bags = bag.split("contain")
        k=" ".join(k.strip().split(" ")[:-1])
        for x in inner_bags.split(","):
            if "other bags." in x:
                r[k.strip()] = []
            else:
                r[k.strip()].append({" ".join(x.strip().split(" ")[1:3]):int(x.strip().split(" ")[0])})
    return dict(r)
            
    


def solve_part_one():
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    bags = {}
    
    for bag in inputs:
        bag_color = bag.split("bags")[0].strip()
        inner_bags = get_inner_bags(bag)
        bags[bag_color] = inner_bags
        
    expanded_bags = set()
    bags_with_target_bag = set()
    
        
    for bag in bags:
        back_propagation = deque()
        back_propagation.append(bag)
        r = expand(bag, bags, expanded_bags, bags_with_target_bag, back_propagation)
        if r:
            expanded_bags, bags_with_target_bag = r
                
    solution = len(bags_with_target_bag)
    
    print("SOLUTION:", bags_with_target_bag)
    
    print("Solution Part 1:", solution)

def expand(bag_to_expand: str, bags: dict, expanded_bags: set, bags_with_target_bag: set, back_propagation: deque) -> tuple:
    TARGET_BAG = "shiny gold"
    print("Bags with target:", bags_with_target_bag)
    
    print("EXPANDING:", bag_to_expand)
    
    # bag already expanded
    if bag_to_expand in expanded_bags:
        if bag_to_expand in bags_with_target_bag:
            bags_with_target_bag.add(bag_to_expand)
            bags_with_target_bag=bags_with_target_bag.union({z for z in back_propagation})
            back_propagation = deque()
        print(bag_to_expand, "ALREADY EXPANDED")
        return expanded_bags, bags_with_target_bag
    
    # empty bag
    if len(bags[bag_to_expand]) == 0:
        print(bag_to_expand, "EMPTY")
        expanded_bags.add(bag_to_expand)

    # bag contains target bag
    if TARGET_BAG in bags[bag_to_expand]:
        print(bag_to_expand, "CONTAINS TARGET")
        bags_with_target_bag.add(bag_to_expand)
        print("Back", back_propagation)
        bags_with_target_bag=bags_with_target_bag.union({x for x in back_propagation})
        back_propagation = deque()

        
    for to_expand in bags[bag_to_expand]:
        back_propagation.append(to_expand)
        r = expand(to_expand, bags, expanded_bags, bags_with_target_bag, back_propagation)
        if r:
            expanded_bags, bags_with_target_bag = r
        back_propagation.pop()
        expanded_bags.add(bag_to_expand)
        
    print("END")
    return expanded_bags, bags_with_target_bag
        
    
def expand2(bag_to_expand: str, bags: dict, n: int) -> int:
    print("EXPANDING:", bag_to_expand)
    
    if len(bags[bag_to_expand]) == 0:
        print(bag_to_expand, "EMPTY")
        return 0
    
    for to_expand in bags[bag_to_expand]:
        print("Number of current bag:", list(to_expand.values())[0])
        n+=list(to_expand.values())[0] + list(to_expand.values())[0] * expand2(list(to_expand.keys())[0], bags, n)
    return n
        
      

def solve_part_two():
    TARGET_BAG = "shiny gold"
    inputs = get_file(os.path.join(THIS_DIR, "input.txt"))
    solution = 0
    
    bags = get_inner_bags2(inputs)
    print(bags)
        
    
    
    r = expand2(TARGET_BAG, bags, 0)    
    if r:
        n = r
                
    solution = n
    
    print("Solution Part 1:", solution)


def main():
    #solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()