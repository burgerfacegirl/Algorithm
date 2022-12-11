fixed_cost,variable_cost,price = map(int,input().split())



if variable_cost < price:
    print(fixed_cost//(price-variable_cost)+1)
elif variable_cost >= price:
    print(-1)
        
    