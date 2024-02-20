human_years=int(input())
dog_years=0
if human_years<1:
    print("Please enter a positive integer")
else:
    count=0
    while human_years>0:
        if count<2:
            dog_years+=10.5
            count+=1
        else:
            dog_years+=4
        human_years-=1
    print("The dog is %.1f years old in dog years."%dog_years)

# human = x
# 1,2 => 10.5
# 3,4,5...... => 4