entryAmount = float(input("Enter the amount"))
#risk = float(input("Enter the risk"))
#reward = float(input("Enter the reward"))

entryPrice = float(input("Enter the Entry Price"))
stopLossPrice = float(input("Enter the Stop-Loss Price"))

#rR = 3/1


"counter = 1"

for i in range(1,201,1):

    amount = entryAmount * i
    amountToken = amount/entryPrice

    stopPoint = amountToken * stopLossPrice
    
    loss = amount - stopPoint

    #if(loss=>risk+1 or loss <= )
    if(loss <= 20):
        print("loss: {} and leverage: {}".format(loss,i))

