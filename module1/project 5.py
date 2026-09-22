# ============================================================
# Classroom Points Calculator
# ============================================================
 
# --- Assignment Operator (=) ---
# Store the points earned by 5 classroom teams
team1 = 150
team2 = 78
team3 = 90
team4 = 130
team5 = 97
 
# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average points
total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("Total points       :", total)
print("Average per team   :", average)
 
# Each point gives 3 reward stars
stars_per_point = 3
reward_stars = total * stars_per_point
print("Total reward stars :", reward_stars)
 
# --- Floor Division (//) and Modulus (%) ---
# Pack reward stars into boxes of 30 stars each
boxes = reward_stars // 30
leftover = reward_stars % 30
 
print("Full boxes packed  :", boxes)
print("Leftover stars     :", leftover)
 
# --- Comparison Operators (>, <, ==, >=) ---
# Compare this week's points with last week's points
last_week = 450
 
print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)
 
# --- Assignment Operators (+=, -=) ---
# Bonus challenge adds 50 points to the total
total += 50
print("After bonus points :", total)
 
# 25 points are removed for missed tasks
total -= 25
print("After missed tasks :", total)
 
# Final reward box count after all changes
reward_stars = total * stars_per_point
boxes = reward_stars // 30
 
print("Final boxes packed :", boxes)
print("THANK YOU!")