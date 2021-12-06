scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}


which_bites = snakes.union(spiders)
print(which_bites)

which_stings = vespas | scorpions
print(which_stings)

arachnids = spiders | scorpions
print(arachnids)