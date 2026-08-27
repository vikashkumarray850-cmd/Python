# DLS Target Calculator

first_team_score = 250
first_team_overs = 50

second_team_overs = 40
resources_lost = 20

# Simple resource percentage
resources_available = 100 - resources_lost

# Calculate revised target
par_score = first_team_score * resources_available / 100

target = int(par_score) + 1

print("First Team Score:", first_team_score)
print("Second Team Overs:", second_team_overs)
print("Resources Available:", resources_available, "%")
print("DLS Revised Target:", target)