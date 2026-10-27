# ================================
# DAILY ACTIVITY PLANNER
# ================================

# ---------- PART 1: homework time ----------
# Ask for the homework time in minutes.
# Turn the answer into a whole number with int().
hw_minutes = int(input("Enter homework time in minutes: "))

# ---------- PART 2: choose a plan ----------
# If the homework time is more than 60, set plan to "start homework now"
# and print "That is a long homework session."
# Otherwise, set plan to "finish homework quickly"
# and print "That is a short homework session."
if hw_minutes > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

# ---------- PART 3: free time ----------
# Ask: Is there free time after homework? (yes/no)
# If the answer is "yes", print a reminder to pick a hobby.
# If the answer is anything else, print nothing.
free_time_ans = input("Is there free time after homework? (yes/no): ")
if free_time_ans == "yes":
    print("Remember to pick a hobby!")

# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
# Print the homework minutes, the plan and the free time answer.
print(f"Homework minutes: {hw_minutes}")
print(f"Your plan: {plan}")
print(f"Free time available: {free_time_ans}")
