first=int(input())
sekond=int(input())
third=int(input())
if first==sekond==third:
    print(3)
elif first==sekond or sekond==third or first==third:
    print(2)
elif first!=sekond and sekond!=third and first!=third:
    print(0)