import csp
from Output import sudokuSolver, sudokuGUI

#Possible number outputs for a Sudoku game: 1-9
sudo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Making sure that our individual boxes can only register the defined numbers
domains = sudokuSolver.solve(sudokuSolver(), sudokuSolver.randPuzzles(sudokuSolver()))
# domains = sudokuSolver.solve(sudokuSolver(), state)
# {
#      'A1':sudo, 'A2': sudo, 'A3': sudo, 'A4': sudo, 'A5': sudo, 'A6': sudo, 'A7': sudo, 'A8': sudo, 'A9': sudo,
#      'B1':sudo, 'B2': sudo, 'B3': sudo, 'B4': sudo, 'B5': sudo, 'B6': sudo, 'B7': sudo, 'B8': sudo, 'B9': sudo,
#      'C1':sudo, 'C2': sudo, 'C3': sudo, 'C4': sudo, 'C5': sudo, 'C6': sudo, 'C7': sudo, 'C8': sudo, 'C9': sudo,
#      'D1':sudo, 'D2': sudo, 'D3': sudo, 'D4': sudo, 'D5': sudo, 'D6': sudo, 'D7': sudo, 'D8': sudo, 'D9': sudo,
#      'E1':sudo, 'E2': sudo, 'E3': sudo, 'E4': sudo, 'E5': sudo, 'E6': sudo, 'E7': sudo, 'E8': sudo, 'E9': sudo,
#      'F1':sudo, 'F2': sudo, 'F3': sudo, 'F4': sudo, 'F5': sudo, 'F6': sudo, 'F7': sudo, 'F8': sudo, 'F9': sudo,
#      'G1':sudo, 'G2': sudo, 'G3': sudo, 'G4': sudo, 'G5': sudo, 'G6': sudo, 'G7': sudo, 'G8': sudo, 'G9': sudo,
#      'H1':sudo, 'H2': sudo, 'H3': sudo, 'H4': sudo, 'H5': sudo, 'H6': sudo, 'H7': sudo, 'H8': sudo, 'H9': sudo,
#      'I1':sudo, 'I2': sudo, 'I3': sudo, 'I4': sudo, 'I5': sudo, 'I6': sudo, 'I7': sudo, 'I8': sudo, 'I9': sudo,
# }

variables = domains.keys()



neighbors = {
    #A
    'A1': ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'B2',
           'B3', 'C2', 'C3'],
    'A2': ['A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'B1',
           'B3', 'C1', 'C3'],
    'A3': ['A1', 'A2', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'B1',
           'B2', 'C1', 'C2'],
    'A4': ['A1', 'A2', 'A3', 'A5', 'A6', 'A7', 'A8', 'A9', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'B5',
           'B6', 'C5', 'C6'],
    'A5': ['A1', 'A2', 'A3', 'A4', 'A6', 'A7', 'A8', 'A9', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'B4',
           'B6', 'C4', 'C6'],
    'A6': ['A1', 'A2', 'A3', 'A4', 'A5', 'A7', 'A8', 'A9', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'B4',
           'B5', 'C4', 'C5'],
    'A7': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A8', 'A9', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7', 'B8',
           'B9', 'C8', 'C9'],
    'A8': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A9', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8', 'B7',
           'B9', 'C7', 'C9'],
    'A9': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9', 'B7',
           'B8', 'C7', 'C8'],
    #B
    'B1': ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'A1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2',
           'A3', 'C2', 'C3'],
    'B2': ['B1', 'B3', 'B4', 'B5', 'B7', 'B7', 'B8', 'B9', 'A2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A1',
           'A3', 'C1', 'C3'],
    'B3': ['B1', 'B2', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'A3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A1',
           'A2', 'C1', 'C2'],
    'B4': ['B1', 'B2', 'B3', 'B5', 'B6', 'B7', 'B8', 'B9', 'A4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5',
           'A6', 'C5', 'C6'],
    'B5': ['B1', 'B2', 'B3', 'B4', 'B6', 'B7', 'B8', 'B9', 'A5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A4',
           'A6', 'C4', 'C6'],
    'B6': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B8', 'B9', 'A6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A4',
           'A5', 'C4', 'C5'],
    'B7': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B8', 'B9', 'A7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7', 'A8',
           'A9', 'C9', 'C9'],
    'B8': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B9', 'A8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8', 'A7',
           'A9', 'C7', 'C9'],
    'B9': ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'A9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9', 'A7',
           'A8', 'C7', 'C8'],
    #C
    'C1': ['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'A1', 'B1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A2',
           'A3', 'C2', 'C3'],
    'C2': ['C1', 'C3', 'C4', 'C5', 'C7', 'C7', 'C8', 'C9', 'A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'A1',
           'A3', 'C1', 'C3'],
    'C3': ['C1', 'C2', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'A3', 'B3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3', 'A1',
           'A2', 'C1', 'C2'],
    'C4': ['C1', 'C2', 'C3', 'C5', 'C6', 'C7', 'C8', 'C9', 'A4', 'B4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4', 'A5',
           'A6', 'C5', 'C6'],
    'C5': ['C1', 'C2', 'C3', 'C4', 'C6', 'C7', 'C8', 'C9', 'A5', 'B5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5', 'A4',
           'A6', 'C4', 'C6'],
    'C6': ['C1', 'C2', 'C3', 'C4', 'C5', 'C7', 'C8', 'C9', 'A6', 'B6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6', 'A4',
           'A5', 'C4', 'C5'],
    'C7': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C8', 'C9', 'A7', 'B7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7', 'A8',
           'A9', 'C8', 'C9'],
    'C8': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C9', 'A8', 'B8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8', 'A7',
           'A9', 'C7', 'C9'],
    'C9': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'A9', 'B9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9', 'A7',
           'A8', 'C7', 'C8'],
    #D
    'D1': ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'A1', 'B1', 'C1', 'E1', 'F1', 'G1', 'H1', 'I1', 'E2',
           'E3', 'F2', 'F3'],
    'D2': ['D1', 'D3', 'D4', 'D5', 'D7', 'D7', 'D8', 'D9', 'A2', 'B2', 'C2', 'E2', 'F2', 'G2', 'H2', 'I2', 'E1',
           'E3', 'F1', 'F3'],
    'D3': ['D1', 'D2', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'A3', 'B3', 'C3', 'E3', 'F3', 'G3', 'H3', 'I3', 'E1',
           'E2', 'F1', 'F2'],
    'D4': ['D1', 'D2', 'D3', 'D5', 'D6', 'D7', 'D8', 'D9', 'A4', 'B4', 'C4', 'E4', 'F4', 'G4', 'H4', 'I4', 'E5',
           'E6', 'F5', 'F6'],
    'D5': ['D1', 'D2', 'D3', 'D4', 'D6', 'D7', 'D8', 'D9', 'A5', 'B5', 'C5', 'E5', 'F5', 'G5', 'H5', 'I5', 'E4',
           'E6', 'F4', 'F6'],
    'D6': ['D1', 'D2', 'D3', 'D4', 'D5', 'D7', 'D8', 'D9', 'A6', 'B6', 'C6', 'E6', 'F6', 'G6', 'H6', 'I6', 'E4',
           'E5', 'F4', 'F5'],
    'D7': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D8', 'D9', 'A7', 'B7', 'C7', 'E7', 'F7', 'G7', 'H7', 'I7', 'E8',
           'E9', 'F8', 'F9'],
    'D8': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D9', 'A8', 'B8', 'C8', 'E8', 'F8', 'G8', 'H8', 'I8', 'E7',
           'E9', 'F7', 'F9'],
    'D9': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'A9', 'B9', 'C9', 'E9', 'F9', 'G9', 'H9', 'I9', 'E7',
           'E8', 'F7', 'F8'],
    #E
    'E1': ['E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'A1', 'B1', 'C1', 'D1', 'F1', 'G1', 'H1', 'I1', 'D2',
           'D3', 'F2', 'F3'],
    'E2': ['E1', 'E3', 'E4', 'E5', 'E7', 'E7', 'E8', 'E9', 'A2', 'B2', 'C2', 'D2', 'F2', 'G2', 'H2', 'I2', 'D1',
           'D3', 'F1', 'F3'],
    'E3': ['E1', 'E2', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'A3', 'B3', 'C3', 'D3', 'F3', 'G3', 'H3', 'I3', 'D1',
           'D2', 'F1', 'F2'],
    'E4': ['E1', 'E2', 'E3', 'E5', 'E6', 'E7', 'E8', 'E9', 'A4', 'B4', 'C4', 'D4', 'F4', 'G4', 'H4', 'I4', 'D5',
           'D6', 'F5', 'F6'],
    'E5': ['E1', 'E2', 'E3', 'E4', 'E6', 'E7', 'E8', 'E9', 'A5', 'B5', 'C5', 'D5', 'F5', 'G5', 'H5', 'I5', 'D4',
           'D6', 'F4', 'F6'],
    'E6': ['E1', 'E2', 'E3', 'E4', 'E5', 'E7', 'E8', 'E9', 'A6', 'B6', 'C6', 'D6', 'F6', 'G6', 'H6', 'I6', 'D4',
           'D5', 'F4', 'F5'],
    'E7': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E8', 'E9', 'A7', 'B7', 'C7', 'D7', 'F7', 'G7', 'H7', 'I7', 'D8',
           'D9', 'F9', 'F9'],
    'E8': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E9', 'A8', 'B8', 'C8', 'D8', 'F8', 'G8', 'H8', 'I8', 'D7',
           'D9', 'F7', 'F9'],
    'E9': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'A9', 'B9', 'C9', 'D9', 'F9', 'G9', 'H9', 'I9', 'D7',
           'D8', 'F7', 'F8'],
    #F
    'F1': ['F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'A1', 'C1', 'D1', 'E1', 'B1', 'G1', 'H1', 'I1', 'D2',
           'D3', 'E2', 'E3'],
    'F2': ['F1', 'F3', 'F4', 'F5', 'F7', 'F7', 'F8', 'F9', 'A2', 'C2', 'D2', 'E2', 'B2', 'G2', 'H2', 'I2', 'D1',
           'D3', 'E1', 'E3'],
    'F3': ['F1', 'F2', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'A3', 'C3', 'D3', 'E3', 'B3', 'G3', 'H3', 'I3', 'D1',
           'D2', 'E1', 'E2'],
    'F4': ['F1', 'F2', 'F3', 'F5', 'F6', 'F7', 'F8', 'F9', 'A4', 'C4', 'D4', 'E4', 'B4', 'G4', 'H4', 'I4', 'D5',
           'D6', 'E5', 'E6'],
    'F5': ['F1', 'F2', 'F3', 'F4', 'F6', 'F7', 'F8', 'F9', 'A5', 'C5', 'D5', 'E5', 'B5', 'G5', 'H5', 'I5', 'D4',
           'D6', 'E4', 'E6'],
    'F6': ['F1', 'F2', 'F3', 'F4', 'F5', 'F7', 'F8', 'F9', 'A6', 'C6', 'D6', 'E6', 'B6', 'G6', 'H6', 'I6', 'D4',
           'D5', 'E4', 'E5'],
    'F7': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F8', 'F9', 'A7', 'C7', 'D7', 'E7', 'B7', 'G7', 'H7', 'I7', 'D8',
           'D9', 'E9', 'E9'],
    'F8': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F9', 'A8', 'C8', 'D8', 'E8', 'B8', 'G8', 'H8', 'I8', 'D7',
           'D9', 'E7', 'E9'],
    'F9': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'A9', 'C9', 'D9', 'E9', 'B9', 'G9', 'H9', 'I9', 'D7',
           'D8', 'E7', 'E8'],
    #G
    'G1': ['G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'A1', 'C1', 'D1', 'E1', 'F1', 'B1', 'H1', 'I1', 'I2',
           'I3', 'H2', 'H3'],
    'G2': ['G1', 'G3', 'G4', 'G5', 'G7', 'G7', 'G8', 'G9', 'A2', 'C2', 'D2', 'E2', 'F2', 'B2', 'H2', 'I2', 'I1',
           'I3', 'H1', 'H3'],
    'G3': ['G1', 'G2', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'A3', 'C3', 'D3', 'E3', 'F3', 'B3', 'H3', 'I3', 'I1',
           'I2', 'H1', 'H2'],
    'G4': ['G1', 'G2', 'G3', 'G5', 'G6', 'G7', 'G8', 'G9', 'A4', 'C4', 'D4', 'E4', 'F4', 'B4', 'H4', 'I4', 'I5',
           'I6', 'H5', 'H6'],
    'G5': ['G1', 'G2', 'G3', 'G4', 'G6', 'G7', 'G8', 'G9', 'A5', 'C5', 'D5', 'E5', 'F5', 'B5', 'H5', 'I5', 'I4',
           'I6', 'H4', 'H6'],
    'G6': ['G1', 'G2', 'G3', 'G4', 'G5', 'G7', 'G8', 'G9', 'A6', 'C6', 'D6', 'E6', 'F6', 'B6', 'H6', 'I6', 'I4',
           'I5', 'H4', 'H5'],
    'G7': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G8', 'G9', 'A7', 'C7', 'D7', 'E7', 'F7', 'B7', 'H7', 'I7', 'I8',
           'I9', 'H9', 'H9'],
    'G8': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G9', 'A8', 'C8', 'D8', 'E8', 'F8', 'B8', 'H8', 'I8', 'I7',
           'I9', 'H7', 'H9'],
    'G9': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'A9', 'C9', 'D9', 'E9', 'F9', 'B9', 'H9', 'I9', 'I7',
           'I8', 'H7', 'H8'],
    #H
    'H1': ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'A1', 'C1', 'D1', 'E1', 'F1', 'G1', 'B1', 'I1', 'G2',
           'G3', 'I2', 'I3'],
    'H2': ['H1', 'H3', 'H4', 'H5', 'H7', 'H7', 'H8', 'H9', 'A2', 'C2', 'D2', 'E2', 'F2', 'G2', 'B2', 'I2', 'G1',
           'G3', 'I1', 'I3'],
    'H3': ['H1', 'H2', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'A3', 'C3', 'D3', 'E3', 'F3', 'G3', 'B3', 'I3', 'G1',
           'G2', 'I1', 'I2'],
    'H4': ['H1', 'H2', 'H3', 'H5', 'H6', 'H7', 'H8', 'H9', 'A4', 'C4', 'D4', 'E4', 'F4', 'G4', 'B4', 'I4', 'G5',
           'G6', 'I5', 'I6'],
    'H5': ['H1', 'H2', 'H3', 'H4', 'H6', 'H7', 'H8', 'H9', 'A5', 'C5', 'D5', 'E5', 'F5', 'G5', 'B5', 'I5', 'G4',
           'G6', 'I4', 'I6'],
    'H6': ['H1', 'H2', 'H3', 'H4', 'H5', 'H7', 'H8', 'H9', 'A6', 'C6', 'D6', 'E6', 'F6', 'G6', 'B6', 'I6', 'G4',
           'G5', 'I4', 'I5'],
    'H7': ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H8', 'H9', 'A7', 'C7', 'D7', 'E7', 'F7', 'G7', 'B7', 'I7', 'G8',
           'G9', 'I9', 'I9'],
    'H8': ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H9', 'A8', 'C8', 'D8', 'E8', 'F8', 'G8', 'B8', 'I8', 'G7',
           'G9', 'I7', 'I9'],
    'H9': ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'A9', 'C9', 'D9', 'E9', 'F9', 'G9', 'B9', 'I9', 'G7',
           'G8', 'I7', 'I8'],
    #I
    'I1': ['I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'A1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'B1', 'G2',
           'G3', 'H2', 'H3'],
    'I2': ['I1', 'I3', 'I4', 'I5', 'I7', 'I7', 'I8', 'I9', 'A2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'B2', 'G1',
           'G3', 'H1', 'H3'],
    'I3': ['I1', 'I2', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'A3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'B3', 'G1',
           'G2', 'H1', 'H2'],
    'I4': ['I1', 'I2', 'I3', 'I5', 'I6', 'I7', 'I8', 'I9', 'A4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'B4', 'G5',
           'G6', 'H5', 'H6'],
    'I5': ['I1', 'I2', 'I3', 'I4', 'I6', 'I7', 'I8', 'I9', 'A5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'B5', 'G4',
           'G6', 'H4', 'H6'],
    'I6': ['I1', 'I2', 'I3', 'I4', 'I5', 'I7', 'I8', 'I9', 'A6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'B6', 'G4',
           'G5', 'H4', 'H5'],
    'I7': ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I8', 'I9', 'A7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'B7', 'G8',
           'G9', 'H9', 'C9'],
    'I8': ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I9', 'A8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'B8', 'G7',
           'G9', 'H7', 'H9'],
    'I9': ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'A9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'B9', 'G7',
           'G8', 'H7', 'H8'],
}
# def eliminateVariables(variablesTD):
#     for x in variablesTD:
#         domains.pop(x)



def constraints(A, a, B, b):
    if A == B:      # ex: A1 == A1
        return True

    if a == b:      # ex: A1 == 1 while A2 == 1
        return False

    return True
solverMethod = csp.CSP(variables, domains, neighbors, constraints)

myCSPs = [
    {'csp': solverMethod,
    # 'select_unassigned_variable':csp.mrv,
    }
]