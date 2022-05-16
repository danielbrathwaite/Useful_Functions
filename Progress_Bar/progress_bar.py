
def progress_bar(comp, total, barlength=30, fill='-', nofill=' ', color=Fore.YELLOW):
    filledLength = int(barlength * comp // total)
    bar = fill * filledLength + nofill * (barlength - filledLength)
    percent=comp*100//total
    print(color+f'\rProgress: |{bar}| {percent}% Complete', end='\r')
    if comp==total:
        print(Fore.GREEN+f'\rProgress: |{bar}| {percent}% Complete', end='\r')
        print(Fore.RESET)
