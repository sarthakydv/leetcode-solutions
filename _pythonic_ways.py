numbersList = [1, 2, 3]
str_list = ["one", "two"]
numbers_tuple = ("ONE", "TWO", "THREE", "FOUR")

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)
for index, (value, val) in enumerate(result):
    print(index)
    print(index, "   ", value, "   ", val)

result = zip(numbersList, str_list, numbers_tuple)


for index, (v1, v2, v3) in enumerate(result):
    print(index, v3)

# Converting to set
result = zip(numbersList, str_list, numbers_tuple)
result_set = set(result)
print(result_set)

# Converting to list
result = zip(numbersList, str_list, numbers_tuple)
result_list = list(result)
print(result_list)

stocks = ["reliance", "infosys", "tcs"]
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)


# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))

zipped = zip(players, scores)
# unzipping values
playerz, scorez = zip(*zipped)

# printing initial lists
print(playerz)
print(scorez)
