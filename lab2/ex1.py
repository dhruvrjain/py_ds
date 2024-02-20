price=4.95
for i in range(0,25,5):
    base_price=price+i
    print("Original: $%.2f | Discounted: $%.2f"%(base_price,base_price*.4))
    # print("Original: $%.2f | Discounted: $%.2f"%(price+i*5,(price+i*5)*.4))