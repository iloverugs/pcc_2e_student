ordnl_nmbrs = list(range(1,10))

for ordnl_nmbr in ordnl_nmbrs:
    if ordnl_nmbr == 1:
        print(f'{ordnl_nmbr}st')
    elif ordnl_nmbr == 2:
        print(f'{ordnl_nmbr}nd')
    elif ordnl_nmbr == 3:
        print(f'{ordnl_nmbr}rd')
    else:
        print(f'{ordnl_nmbr}th')