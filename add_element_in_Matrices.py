#! Adding element to matrix.

# row1 = [1,1,1]
# row2 = [1,1,1]
# row3 = [1,1,1]
# matrix = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = (input("Enter the position where to hide money : "))
# row = int( position[0])
# colm = int(position[1])
# selected_row = matrix[row-1]
# selected_row[colm-1] = 0
# print(f"{row1}\n{row2}\n{row3}")

row1 = ['😊','😊','😊']
row2 = ['😊','😊','😊']
row3 = ['😊','😊','😊']
matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Enter Row & Colm value :")
row = int(position[0])
colm = int(position[1])
selected_row = matrix[row-1]
selected_row[colm-1] = '🎁'
print(f"{row1}\n{row2}\n{row3}")