APPLES = .50
BREAD = 1.50
CHEESE = 2.25
numApples = 3
numBread = 4
numCheese = 2
prcApples = 3 * APPLES
prcBread = 4 * BREAD
prcCheese = 2 * CHEESE
strApples = 'Apples'
strBread = 'Bread'
strCheese = 'Cheese'

total = prcBread + prcBread + prcApples
print(f'{"My Grocery List":^30s}')
print(f'{"="*30}')
print(f'{strApples}\t{numApples:10d}\t\t${prcApples:>5.2f}')
print(f'{strBread}\t{numBread:10d}\t\t${prcBread:>5.2f}')
print(f'{strCheese}\t{numCheese:10d}\t\t${prcCheese:>5.2f}')
print(f'{"Total:":>19s}\t\t${total:>4.2f}')
