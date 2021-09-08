print("Hello World")

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = ((my_votes / total_votes) * 100:.2f)
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[2] == 'Denver':
    print(counties[1])
else:
    print(counties[0])

score = int(input("What is your score"))
if score >=90:
    print("Grade A")
elif score >=80:
    print("Grade B")
elif score >=70:
    print("Grade C")
elif score >=60:
    print("Grade D")
else:
    print("Fail")

    
      
