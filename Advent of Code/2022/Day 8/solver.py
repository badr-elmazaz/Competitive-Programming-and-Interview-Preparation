def get_input():
    with open("./input.txt") as f:
        return f.read().splitlines()



def solve1():
    inputs = get_input()
    #calculating the perimeter
    visible = (len(inputs)*2)+((len(inputs[0])-2)*2)
    for i in range(1, len(inputs)-1):
        for j in range(1, len(inputs[i])-1):
            current_tree = inputs[i][j]
            # check left
            l=j-1
            while(l>-1):
         
                left_tree = inputs[i][l]
                if left_tree >= current_tree:
                    break
                l-=1
            else:

                visible+=1
                continue
            # check right
            r=j+1
            while(r<len(inputs[i])):
              
                right_tree = inputs[i][r]
                if right_tree >= current_tree:
                    break
                r+=1
            else:
      
                visible+=1
                continue
            # check top
            t=i-1
            while(t>-1):
                
                top_tree = inputs[t][j]
                if top_tree >= current_tree:
                    break
                t-=1
            else:
           
                visible+=1
                continue
            # check bottom
            b=i+1
            while(b<len(inputs)):
                
                bottom_tree = inputs[b][j]
                if bottom_tree >= current_tree:
                    break
                b+=1
            else:
   
                visible+=1

    print("Part 1:", visible)


def solve2():
    inputs = get_input()
    best_scenic_score = 0
    for i in range(1, len(inputs)-1):
        for j in range(1, len(inputs[i])-1):
            current_tree = inputs[i][j]
            scenic_score=1
            # check left
            l=j-1
            count = 0
            while(l>-1):
                count+=1
                left_tree = inputs[i][l]
                if left_tree >= current_tree:
                    break
                l-=1
            scenic_score*=count
            # check right
            count = 0
            r=j+1
            while(r<len(inputs[i])):
                count += 1
                right_tree = inputs[i][r]
                if right_tree >= current_tree:
                    break
                r+=1
            scenic_score*=count
            # check top
            count = 0
            t=i-1
            while(t>-1):
                count += 1
                top_tree = inputs[t][j]
                if top_tree >= current_tree:
                    break
                t-=1
            scenic_score*=count
            # check bottom
            count = 0
            b=i+1
            while(b<len(inputs)):
                count += 1
                bottom_tree = inputs[b][j]
                if bottom_tree >= current_tree:
                    break
                b+=1
            scenic_score*=count
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score
        

    print("Part 2:", best_scenic_score)
        


if __name__ == "__main__":
    solve1()
    solve2()