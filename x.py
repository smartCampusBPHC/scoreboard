w, h = 6 ,5 
Matrix = [[0 for x in range(w)] for y in range(h)]
#Sports Names
Matrix[0][0] = 'Cricket'
Matrix[0][1] = 'Football'
Matrix[0][2] = 'Badminton(B)'
Matrix[0][3] = 'Badminton(G)'
Matrix[0][4] = 'Table Tennis(B)'
Matrix[0][5] = 'Table Tennis(G)'
#Status of Game
Matrix[1][0] = 'Yet To Start'
Matrix[1][1] = 'Yet To Start'
Matrix[1][2] = 'Yet To Start'
Matrix[1][3] = 'Yet To Start'
Matrix[1][4] = 'Yet To Start'
Matrix[1][5] = 'Ongoing'
#Team 1
Matrix[2][0] = 'BPHC'
Matrix[2][1] = 'BPHC'
Matrix[2][2] = 'BPHC'
Matrix[2][3] = 'BPHC'
Matrix[2][4] = 'BPHC'
Matrix[2][5] = 'BPHC'
#Team 2
Matrix[3][0] = 'BPHC' 
Matrix[3][1] = 'BPHC'
Matrix[3][2] = 'BPHC'
Matrix[3][3] = 'BPHC'
Matrix[3][4] = 'BPHC'
Matrix[3][5] = 'BPHC'

#Score String 

Matrix[4][0] = '245/3(20) and 112/3(12)'
Matrix[4][1] = '3-2'
Matrix[4][2] = '21-16, 12-1'
Matrix[4][3] = '21-11, 21-3'
Matrix[4][4] = '12-1,12-6,12-2'
Matrix[4][5] = '12-1,12-6,12-2'

for i in Matrix:
	for y in i:
		print y
