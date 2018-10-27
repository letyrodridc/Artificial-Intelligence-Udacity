import solution_letyrodri
import unittest

'''
    Unit tests made by @letyrodri
    Only works without diagonal version. 
    
    Uses solution_letyrodri.py
'''

class TestEliminate(unittest.TestCase):
    grid = dict({'F7': '2', 'B5': '123456789', 'B2': '123456789', 'E6': '123456789', 'F9': '123456789', 'G9': '123456789', 'E9': '8', 'H4': '2', 'D9': '123456789', 'I7': '3', 'C4': '8', 'B4': '3', 'H5': '123456789', 'F8': '123456789', 'C1': '123456789', 'A2': '123456789', 'E3': '123456789', 'D8': '123456789', 'B3': '123456789', 'F3': '6', 'C3': '1', 'D4': '1', 'I5': '1', 'C9': '123456789', 'H2': '123456789', 'I1': '123456789', 'H9': '9', 'G2': '123456789', 'H3': '123456789', 'F6': '8', 'G5': '123456789', 'E2': '123456789', 'G8': '123456789', 'D1': '123456789', 'D6': '2', 'G6': '9', 'C6': '6', 'G3': '2', 'H7': '123456789', 'A5': '2', 'G1': '123456789', 'I4': '123456789', 'B7': '123456789', 'I9': '123456789', 'F2': '123456789', 'C8': '123456789', 'D5': '123456789', 'B6': '5', 'C2': '123456789', 'E7': '123456789', 'E1': '7', 'I2': '123456789', 'C5': '123456789', 'F4': '7', 'G7': '5', 'D3': '8', 'F1': '123456789', 'D2': '123456789', 'B1': '9', 'B9': '1', 'I3': '5', 'B8': '123456789', 'A3': '3', 'A1': '123456789', 'A7': '6', 'E4': '123456789', 'A9': '123456789', 'E8': '123456789', 'I8': '123456789', 'A4': '123456789', 'H6': '3', 'D7': '9', 'G4': '6', 'F5': '123456789', 'E5': '123456789', 'I6': '123456789', 'H1': '8', 'H8': '123456789', 'C7': '4', 'A6': '123456789', 'A8': '123456789'})
    solved_sudoku = {'F3': '6', 'B4': '3', 'F1': '1345', 'B7': '78', 'I8': '24678', 'C6': '6', 'C2': '257', 'C7': '4', 'G6': '9', 'B5': '47', 'H9': '9', 'G7': '5', 'E5': '34569', 'I3': '5', 'D7': '9', 'H3': '47', 'I4': '4', 'F6': '8', 'A9': '57', 'B3': '47', 'E1': '7', 'A4': '49', 'I9': '2467', 'I2': '4679', 'D9': '34567', 'G3': '2', 'C5': '79', 'A6': '147', 'H7': '17', 'B9': '1', 'C4': '8', 'F4': '7', 'E9': '8', 'B2': '24678', 'F7': '2', 'C8': '23579', 'B1': '9', 'H2': '1467', 'A8': '5789', 'A5': '2', 'D3': '8', 'C9': '2357', 'G5': '478', 'A2': '4578', 'E8': '13456', 'E6': '4', 'E2': '123459', 'A1': '45', 'I5': '1', 'D6': '2', 'F8': '1345', 'C3': '1', 'G9': '47', 'I1': '46', 'I7': '3', 'G1': '134', 'E4': '459', 'G8': '1478', 'D4': '1', 'E3': '49', 'F2': '13459', 'E7': '1', 'D1': '345', 'G2': '1347', 'C1': '25', 'H6': '3', 'A3': '3', 'B8': '278', 'H4': '2', 'F5': '3459', 'A7': '6', 'B6': '5', 'G4': '6', 'D8': '34567', 'F9': '345', 'H5': '457', 'H8': '1467', 'D5': '3456', 'I6': '47', 'H1': '8', 'D2': '345'}

    def test_eliminate(self):
        self.assertEqual(solution_letyrodri.eliminate(self.grid), self.solved_sudoku)

class TestOnlyChoice(unittest.TestCase):
    grid = dict({'B8': '278', 'G8': '1478', 'C5': '79', 'I4': '4', 'E7': '1', 'C8': '23579', 'E5': '34569', 'H5': '457', 'H7': '17', 'F4': '7', 'B5': '47', 'A4': '49', 'C3': '1', 'A5': '2', 'B3': '47', 'B7': '78', 'C7': '4', 'C9': '2357', 'F5': '3459', 'G9': '47', 'D3': '8', 'A3': '3', 'F3': '6', 'I9': '2467', 'G6': '9', 'I7': '3', 'H2': '1467', 'I1': '46', 'I6': '47', 'E1': '7', 'H6': '3', 'E8': '13456', 'A2': '4578', 'G5': '478', 'D1': '345', 'D6': '2', 'E9': '8', 'E4': '459', 'E3': '49', 'E2': '123459', 'A6': '147', 'G7': '5', 'A8': '5789', 'D5': '3456', 'H4': '2', 'G1': '134', 'I2': '4679', 'F9': '345', 'H1': '8', 'B9': '1', 'C4': '8', 'D9': '34567', 'B6': '5', 'F8': '1345', 'G2': '1347', 'C6': '6', 'B4': '3', 'H9': '9', 'A7': '6', 'I5': '1', 'F2': '13459', 'I8': '24678', 'D8': '34567', 'F7': '2', 'I3': '5', 'H8': '1467', 'G3': '2', 'D7': '9', 'D4': '1', 'G4': '6', 'F6': '8', 'B1': '9', 'C1': '25', 'B2': '24678', 'H3': '47', 'E6': '4', 'A9': '57', 'C2': '257', 'A1': '45', 'D2': '345', 'F1': '1345'})
    solved_sudoku = {'B8': '278', 'C5': '79', 'I4': '4', 'E7': '1', 'C8': '23579', 'E5': '34569', 'H5': '5', 'F4': '7', 'B5': '47', 'C3': '1', 'F5': '3459', 'D3': '8', 'A3': '3', 'I6': '47', 'G6': '9', 'I7': '3', 'H2': '1467', 'I1': '6', 'A4': '49', 'E1': '7', 'A2': '4578', 'D8': '34567', 'H7': '17', 'G7': '5', 'B4': '3', 'H1': '8', 'B9': '1', 'C4': '8', 'F9': '345', 'D4': '1', 'I5': '1', 'G3': '2', 'D7': '9', 'G4': '6', 'F6': '8', 'E3': '9', 'D6': '2', 'F8': '1345', 'C2': '257', 'H8': '1467', 'G8': '1478', 'C1': '2', 'D1': '345', 'F1': '1345', 'B6': '5', 'A5': '2', 'B3': '47', 'C7': '4', 'C9': '2357', 'G9': '47', 'I9': '2467', 'B1': '9', 'B7': '8', 'A9': '57', 'F3': '6', 'E8': '13456', 'G5': '8', 'B2': '6', 'E9': '8', 'E4': '5', 'A6': '1', 'A8': '5789', 'D5': '3456', 'H4': '2', 'G1': '134', 'I2': '9', 'E2': '2', 'D9': '34567', 'G2': '1347', 'C6': '6', 'H9': '9', 'A7': '6', 'H3': '47', 'F2': '13459', 'I8': '8', 'F7': '2', 'I3': '5', 'A1': '45', 'H6': '3', 'E6': '4', 'D2': '345'}

    def test_only_choice1(self):
        self.assertEqual(solution_letyrodri.only_choice(self.grid), self.solved_sudoku)        

class TestSearch(unittest.TestCase):
    grid = dict({'B3': '123456789', 'F2': '123456789', 'B5': '123456789', 'E5': '8', 'E9': '123456789', 'A7': '8', 'I7': '123456789', 'E4': '123456789', 'G1': '123456789', 'E1': '123456789', 'I5': '123456789', 'H4': '2', 'F1': '123456789', 'H1': '5', 'A1': '4', 'H7': '123456789', 'F9': '123456789', 'F6': '123456789', 'H6': '123456789', 'H2': '123456789', 'B6': '123456789', 'H9': '123456789', 'A2': '123456789', 'I4': '123456789', 'I6': '123456789', 'D2': '2', 'H5': '123456789', 'C6': '123456789', 'G3': '123456789', 'A5': '123456789', 'F5': '1', 'G2': '123456789', 'C3': '123456789', 'D3': '123456789', 'A3': '123456789', 'C4': '7', 'C2': '123456789', 'I3': '4', 'C5': '123456789', 'B4': '123456789', 'F7': '123456789', 'D4': '123456789', 'G7': '123456789', 'D6': '123456789', 'G8': '7', 'D9': '123456789', 'I8': '123456789', 'F3': '123456789', 'F8': '123456789', 'I1': '1', 'B9': '123456789', 'H8': '123456789', 'E3': '123456789', 'D8': '6', 'D5': '123456789', 'E6': '123456789', 'I2': '123456789', 'B1': '123456789', 'C7': '123456789', 'B8': '123456789', 'I9': '123456789', 'D1': '123456789', 'G9': '123456789', 'E2': '123456789', 'A4': '123456789', 'C9': '123456789', 'A9': '5', 'C8': '123456789', 'B7': '123456789', 'H3': '123456789', 'F4': '123456789', 'A8': '123456789', 'G5': '123456789', 'G4': '6', 'A6': '123456789', 'C1': '123456789', 'D7': '123456789', 'E8': '123456789', 'G6': '3', 'B2': '3', 'E7': '4'})
    solved_sudoku = {'H3': '3', 'G3': '9', 'D1': '8', 'C7': '3', 'A3': '7', 'B6': '8', 'F4': '9', 'A4': '3', 'G5': '4', 'C3': '8', 'I2': '6', 'G6': '3', 'A8': '2', 'E7': '4', 'I7': '2', 'D6': '7', 'F6': '2', 'I6': '5', 'H1': '5', 'A2': '1', 'D7': '1', 'C6': '4', 'B8': '4', 'H8': '8', 'C9': '6', 'C5': '2', 'D5': '3', 'E3': '1', 'D3': '5', 'I5': '7', 'A9': '5', 'C8': '1', 'B5': '5', 'B3': '2', 'I3': '4', 'D2': '2', 'E5': '8', 'A1': '4', 'A7': '8', 'B1': '6', 'C1': '9', 'E9': '2', 'H5': '9', 'E2': '9', 'A6': '9', 'I4': '8', 'H7': '6', 'F3': '6', 'H6': '1', 'E8': '3', 'I8': '9', 'I9': '3', 'F8': '5', 'B9': '7', 'H4': '2', 'F9': '8', 'F7': '7', 'G2': '8', 'A5': '6', 'B4': '1', 'E4': '5', 'G1': '2', 'F2': '4', 'D8': '6', 'D4': '4', 'G7': '5', 'D9': '9', 'G8': '7', 'E1': '7', 'G4': '6', 'C2': '5', 'E6': '6', 'G9': '1', 'H2': '7', 'B2': '3', 'I1': '1', 'F5': '1', 'C4': '7', 'H9': '4', 'F1': '3', 'B7': '9'}

    def test_search(self):
        self.assertEqual(solution_letyrodri.search(self.grid), self.solved_sudoku)        

class Test95Sudokus(unittest.TestCase):
    grid = [] 
    solved_sudoku = []
    filename_sudoku = "tests/norvig_top95.txt"
    filename_sudoku_solutions = "tests/norvig_top95_solutions_str.txt"

    def _readfile(self,filename, container):
        with open(filename, 'r') as f:
            for read_data in f:
                container.append(read_data.replace('\n',''))

    def test_95Sudokus(self):
        self._readfile(self.filename_sudoku, self.grid)
        self._readfile(self.filename_sudoku_solutions, self.solved_sudoku)
        
        for i,g in enumerate(self.grid[0:10]):
            print(i)
            self.assertEqual(solution_letyrodri.solve(g), solution_letyrodri.grid_values(self.solved_sudoku[i]))        

def auxiliar_process():
    filename = "tests/norvig_top95_solutions.txt" 
    
    line = 1
    block = False
    s = ''
    with open(filename, 'r') as f:
        for read_data in f:

            if line == 14 or ((line - 14) % 26) == 0:
                block = True

            if block and (line == 25 or ((line - 14) % 26) == 11):
                block = False

            if block:
                s = s+(((read_data.replace('\n','')).replace('+','')).replace('|','')).replace('-','')     
                s = s.replace(' ','')

            if len(s) > 0 and not block:
                print(s)
                s = ''         

            line = line+1
        
if __name__ == '__main__':
    unittest.main()
    