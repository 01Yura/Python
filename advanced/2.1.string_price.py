string = input()
kopeiki = len(string) * 60
price = str(kopeiki//100) + " р. " + str(kopeiki%100) + " коп."
print(price)