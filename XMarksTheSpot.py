# Printing board of horizontal and vertical squares
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# create a variable position to have input from user
position = input("Where do you want to put the treasure? ")
# create variable for horizontal and decrease by 1 because index starts with 0
horizontal = int(position[0]) - 1
# create variable for vertical and decrease by 1 because index starts with 0
vertical = int(position[1]) - 1
# Selecting vertical row
selected_row = (map[vertical])
# Selecting horizontal row and the location of X
selected_row[horizontal] = "X"
# Final result printing output
print(f"{row1}\n{row2}\n{row3}")
