#include <algorithm>
#include <cctype>
#include <cmath>
#include <fcntl.h>
#include <iostream>
#include <locale>
#include <random>
#include <stdio.h>
#include <string>
#include <vector>
#ifdef _WIN32
#include <io.h>
#include <windows.h>
#endif
const std::string RESET = "\033[0m";    // what it says on the tin
const std::string BLACK = "\033[0;94m"; // white
const std::string WHITE = "\033[93m";   // black
const std::string ALPHA = "ABCDEFGH";
constexpr int MAX_DEPTH = 20;
int nodes = 0;
std::string killer[2][MAX_DEPTH];

void doWeirdTerminalStuff() {
#ifdef _WIN32
  // Windows UTF-8 setup
  SetConsoleOutputCP(CP_UTF8);
  setvbuf(stdout, nullptr, _IOFBF, 1000);
#endif

  // Set locale for all platforms
  std::locale::global(std::locale(""));
  std::cout.imbue(std::locale());
}
std::string getPieceName(char val) {
  switch (val) {
  case 'p':
    return "wPawn";
  case 'P':
    return "bPawn";
  case 'r':
    return "wRook";
  case 'R':
    return "bRook";
  case 'b':
    return "wBishop";
  case 'B':
    return "bBishop";
  case 'n':
    return "wknight";
  case 'N':
    return "bknight";
  case 'k':
    return "wKing";
  case 'K':
    return "bKing";
  case 'q':
    return "wQueen";
  case 'Q':
    return "bQueen";
  default:
    return "nEmpty";
  }
}

void displayPiece(std::string piece) {
  char clr = piece[0];
  piece.erase(0, 1);
  std::string type = piece;
  std::string icon;

  if (type == "King")
    icon = " ♔  ";
  else if (type == "Queen")
    icon = " ♕  ";
  else if (type == "Rook")
    icon = " ♖  ";
  else if (type == "Bishop")
    icon = " ♗  ";
  else if (type == "knight")
    icon = " ♘  ";
  else if (type == "Pawn")
    icon = " ♙  ";
  else
    icon = "    ";

  switch (clr) {
  case 'n':
    std::cout << RESET + icon + "|";
    break;
  case 'w':
    std::cout << WHITE + icon + RESET + "|";
    break;
  case 'b':
    std::cout << BLACK + icon + RESET + "|";
    break;
  }
}

void printFullBoard(std::string board) {
  for (int i = 0; i < board.length(); i++) {
    std::string pName = getPieceName(board[i]);
    if (i % 8 == 0) {
      std::cout << RESET << "\n\t-----------------------------------------\n"
                << 8 - (i / 8) << "\t|";
    }
    displayPiece(pName);
  }
  std::cout << "\n\n.          A    B    C    D    E    F    G    H";
}
char getState(std::string cell, std::string board) {
  int row = 8 - (cell[1] - '0');
  char letter = cell[0];
  int column = ALPHA.find(letter);
  int index = row * 8 + column;
  return board[index];
}

std::string getCellCode(int index) {
  int row = index / 8;
  int column = index % 8;
  char letter = ALPHA[column];
  return (std::string(1, letter) + std::string(1, '8' - row));
}

int getListPos(std::string cell) {
  int row = 8 - (cell[1] - '0');
  int column = ALPHA.find(cell[0]);
  int index = row * 8 + column;
  return index;
}

std::string getRowUpOrDown(std::string curCell, int amm) {
  int num = curCell[1] - '0';
  if (num + amm <= 8 && num + amm >= 1) {
    return std::string(1, '0' + (num + amm));
  }
  return "?";
}

std::string getColToRightOrLeft(std::string curCell, int amm) {
  size_t index = ALPHA.find(curCell[0]);
  if (index != std::string::npos && (index + amm <= 7) && (index + amm >= 0)) {
    return std::string(1, ALPHA[index + amm]);
  }
  return "?";
}

std::string movePiece(std::string nCell, std::string oCell, std::string board) {
  int oCellPos = getListPos(oCell);
  int nCellPos = getListPos(nCell);
  std::string piece = getPieceName(board[oCellPos]);
  if (piece == "wPawn" && nCell[1] == '8') {
    board[nCellPos] = 'q';
    board[oCellPos] = '.';
  } else if (piece == "bPawn" && nCell[1] == '1') {
    board[nCellPos] = 'Q';
    board[oCellPos] = '.';
  } else {
    board[nCellPos] = board[oCellPos];
    board[oCellPos] = '.';
  }
  return board;
}

int checkPieceAmm(char piece, std::string board) {
  return std::count(board.begin(), board.end(), piece);
}

// piece movesets... fun.

std::string pawnMoves(std::string curCell, std::string futCell,
                      bool showValidMoves, bool isAI, std::string board) {
  std::string takingMoves = "";
  std::string basicMoves = "";
  std::string validMoves = "";
  std::string pieceType = getPieceName(getState(curCell, board));
  char pieceClr = pieceType[0];
  pieceType.erase(0, 1);

  if (pieceClr == 'w') {
    basicMoves += (std::string(1, curCell[0]) + getRowUpOrDown(curCell, 1));
    takingMoves +=
        (getColToRightOrLeft(curCell, -1) + (getRowUpOrDown(curCell, 1)));
    takingMoves +=
        (getColToRightOrLeft(curCell, 1) + getRowUpOrDown(curCell, 1));
    if (curCell[1] == '2') {
      basicMoves += (std::string(1, curCell[0]) + getRowUpOrDown(curCell, 2));
    }
  }

  else if (pieceClr == 'b') {
    basicMoves += (std::string(1, curCell[0]) + getRowUpOrDown(curCell, -1));
    takingMoves +=
        (getColToRightOrLeft(curCell, -1) + (getRowUpOrDown(curCell, -1)));
    takingMoves +=
        (getColToRightOrLeft(curCell, 1) + getRowUpOrDown(curCell, -1));
    if (curCell[1] == '7') {
      basicMoves += (std::string(1, curCell[0]) + getRowUpOrDown(curCell, -2));
    }
  }

  for (int i = 0; i < basicMoves.length(); i += 2) {
    std::string cell =
        std::string(1, basicMoves[i]) + std::string(1, basicMoves[i + 1]);
    if (cell.find('?') == std::string::npos and
        getPieceName(getState(cell, board)) == "nEmpty") {
      validMoves.append(cell);
    }
  }

  for (int i = 0; i < takingMoves.length(); i += 2) {
    std::string cell =
        std::string(1, takingMoves[i]) + std::string(1, takingMoves[i + 1]);
    if (cell.find('?') == std::string::npos and
        getPieceName(getState(cell, board)) != "nEmpty" and
        getPieceName(getState(cell, board))[0] !=
            getPieceName(getState(curCell, board))[0]) {
      validMoves.append(cell);
    }
  }

  if (isAI) {
    return validMoves;
  }

  if (validMoves.length() == 0) {
    return "-2";
  } // no possible moves error

  if (showValidMoves == true) {
    std::cout << "\n\n\nValid moves are: ";
    for (int i = 0; i < validMoves.length(); i += 2) {
      std::cout << validMoves[i] << validMoves[i + 1] << ", ";
    }
    return "-1";
  } // redo player turn error (not an error but idc)

  if (validMoves.find(futCell) != std::string::npos) {
    board = movePiece(futCell, curCell, board);
  } else {
    return "0";
  } // invalid move error
  return board;
} // successful returns board

std::string kingMoves(std::string curCell, std::string futCell,
                      bool showValidMoves, bool isAI, std::string board) {
  std::string validMoves = "";
  std::string moves = "";
  moves += (std::string(1, curCell[0]) + getRowUpOrDown(curCell, 1));
  moves += (std::string(1, curCell[0]) + getRowUpOrDown(curCell, -1));
  moves += (getColToRightOrLeft(curCell, -1) + std::string(1, curCell[1]));
  moves += (getColToRightOrLeft(curCell, 1) + std::string(1, curCell[1]));
  moves += (getColToRightOrLeft(curCell, -1) + getRowUpOrDown(curCell, 1));
  moves += (getColToRightOrLeft(curCell, -1) + getRowUpOrDown(curCell, -1));
  moves += (getColToRightOrLeft(curCell, 1) + getRowUpOrDown(curCell, 1));
  moves += (getColToRightOrLeft(curCell, 1) + getRowUpOrDown(curCell, -1));

  for (int i = 0; i < moves.length(); i += 2) {
    std::string cell = std::string(1, moves[i]) + std::string(1, moves[i + 1]);
    if (cell.find('?') == std::string::npos) {
      if (getPieceName(getState(cell, board))[0] !=
          getPieceName(getState(curCell, board))[0]) {
        validMoves += cell;
      }
    }
  }
  if (isAI) {
    return validMoves;
  }

  if (validMoves.length() == 0) {
    return "-2";
  } // no possible moves error

  if (showValidMoves == true) {
    std::cout << "\n\n\nValid moves are: ";
    for (int i = 0; i < validMoves.length(); i += 2) {
      std::cout << validMoves[i] << validMoves[i + 1] << ", ";
    }
    return "-1";
  } // redo player turn error (not an error but idc)

  if (validMoves.find(futCell) != std::string::npos) {
    board = movePiece(futCell, curCell, board);
  } else {
    return "0";
  } // invalid move error
  return board;
} // successful returns board

std::string queenMoves(std::string curCell, std::string futCell,
                       bool showValidMoves, bool isAI, std::string board) {
  std::string moves = "";
  std::string validMoves = "";
  // rook moves
  for (int amm = 1; amm < 8; amm++) { // going vertically up
    std::string cell =
        (std::string(1, curCell[0]) + getRowUpOrDown(curCell, amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going vertically down
    std::string cell =
        (std::string(1, curCell[0]) + getRowUpOrDown(curCell, -amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going horizontally right
    std::string cell =
        (getColToRightOrLeft(curCell, amm) + std::string(1, curCell[1]));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going horizontally left
    std::string cell =
        (getColToRightOrLeft(curCell, -amm) + std::string(1, curCell[1]));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }
  // bishop moves
  for (int amm = 1; amm < 8; amm++) { // going up to right diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, amm) + getRowUpOrDown(curCell, amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going up to left diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, -amm) + getRowUpOrDown(curCell, amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going down to right diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, amm) + getRowUpOrDown(curCell, -amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going down to left diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, -amm) + getRowUpOrDown(curCell, -amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int i = 0; i < moves.length(); i += 2) {
    std::string cell = std::string(1, moves[i]) + std::string(1, moves[i + 1]);
    if (cell.find('?') == std::string::npos) {
      if (getPieceName(getState(cell, board))[0] !=
          getPieceName(getState(curCell, board))[0]) {
        validMoves += cell;
      }
    }
  }
  if (isAI) {
    return validMoves;
  }

  if (validMoves.length() == 0) {
    return "-2";
  } // no possible moves error

  if (showValidMoves == true) {
    std::cout << "\n\n\nValid moves are: ";
    for (int i = 0; i < validMoves.length(); i += 2) {
      std::cout << validMoves[i] << validMoves[i + 1] << ", ";
    }
    return "-1";
  } // redo player turn error (not an error but idc)

  if (validMoves.find(futCell) != std::string::npos) {
    board = movePiece(futCell, curCell, board);
  } else {
    return "0";
  } // invalid move error
  return board;
} // successful returns board

std::string bishopMoves(std::string curCell, std::string futCell,
                        bool showValidMoves, bool isAI, std::string board) {
  std::string moves = "";
  std::string validMoves = "";
  for (int amm = 1; amm < 8; amm++) { // going up to right diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, amm) + getRowUpOrDown(curCell, amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going up to left diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, -amm) + getRowUpOrDown(curCell, amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going down to right diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, amm) + getRowUpOrDown(curCell, -amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going down to left diagonally
    std::string cell =
        (getColToRightOrLeft(curCell, -amm) + getRowUpOrDown(curCell, -amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int i = 0; i < moves.length(); i += 2) {
    std::string cell = std::string(1, moves[i]) + std::string(1, moves[i + 1]);
    if (cell.find('?') == std::string::npos) {
      if (getPieceName(getState(cell, board))[0] !=
          getPieceName(getState(curCell, board))[0]) {
        validMoves += cell;
      }
    }
  }
  if (isAI) {
    return validMoves;
  }

  if (validMoves.length() == 0) {
    return "-2";
  } // no possible moves error

  if (showValidMoves == true) {
    std::cout << "\n\n\nValid moves are: ";
    for (int i = 0; i < validMoves.length(); i += 2) {
      std::cout << validMoves[i] << validMoves[i + 1] << ", ";
    }
    return "-1";
  } // redo player turn error (not an error but idc)

  if (validMoves.find(futCell) != std::string::npos) {
    board = movePiece(futCell, curCell, board);
  } else {
    return "0";
  } // invalid move error
  return board;
} // successful returns board

std::string rookMoves(std::string curCell, std::string futCell,
                      bool showValidMoves, bool isAI, std::string board) {
  std::string moves = "";
  std::string validMoves = "";
  // rook moves
  for (int amm = 1; amm < 8; amm++) { // going vertically up
    std::string cell =
        (std::string(1, curCell[0]) + getRowUpOrDown(curCell, amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going vertically down
    std::string cell =
        (std::string(1, curCell[0]) + getRowUpOrDown(curCell, -amm));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going horizontally right
    std::string cell =
        (getColToRightOrLeft(curCell, amm) + std::string(1, curCell[1]));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int amm = 1; amm < 8; amm++) { // going horizontally left
    std::string cell =
        (getColToRightOrLeft(curCell, -amm) + std::string(1, curCell[1]));
    if ((cell.find('?') == std::string::npos) &&
        (getPieceName(getState(cell, board))[0] !=
         getPieceName(getState(curCell, board))[0])) {
      moves += cell;
      char thingInCellClr = getPieceName(getState(cell, board))[0];
      if (thingInCellClr != 'n') {
        break;
      }
    } else {
      break;
    }
  }

  for (int i = 0; i < moves.length(); i += 2) {
    std::string cell = std::string(1, moves[i]) + std::string(1, moves[i + 1]);
    if (cell.find('?') == std::string::npos) {
      if (getPieceName(getState(cell, board))[0] !=
          getPieceName(getState(curCell, board))[0]) {
        validMoves += cell;
      }
    }
  }
  if (isAI) {
    return validMoves;
  }

  if (validMoves.length() == 0) {
    return "-2";
  } // no possible moves error

  if (showValidMoves == true) {
    std::cout << "\n\n\nValid moves are: ";
    for (int i = 0; i < validMoves.length(); i += 2) {
      std::cout << validMoves[i] << validMoves[i + 1] << ", ";
    }
    return "-1";
  } // redo player turn error (not an error but idc)

  if (validMoves.find(futCell) != std::string::npos) {
    board = movePiece(futCell, curCell, board);
  } else {
    return "0";
  } // invalid move error
  return board;
} // successful returns board

std::string knightMoves(std::string curCell, std::string futCell,
                        bool showValidMoves, bool isAI, std::string board) {
  std::string moves = "";
  std::string validMoves = "";

  moves += (getColToRightOrLeft(curCell, -1) + getRowUpOrDown(curCell, 2));
  moves += (getColToRightOrLeft(curCell, -1) + getRowUpOrDown(curCell, -2));
  moves += (getColToRightOrLeft(curCell, 1) + getRowUpOrDown(curCell, 2));
  moves += (getColToRightOrLeft(curCell, 1) + getRowUpOrDown(curCell, -2));
  moves += (getColToRightOrLeft(curCell, 2) + getRowUpOrDown(curCell, 1));
  moves += (getColToRightOrLeft(curCell, 2) + getRowUpOrDown(curCell, -1));
  moves += (getColToRightOrLeft(curCell, -2) + getRowUpOrDown(curCell, 1));
  moves += (getColToRightOrLeft(curCell, -2) + getRowUpOrDown(curCell, -1));
  for (int i = 0; i < moves.length(); i += 2) {
    std::string cell = std::string(1, moves[i]) + std::string(1, moves[i + 1]);
    if (cell.find('?') == std::string::npos) {
      if (getPieceName(getState(cell, board))[0] !=
          getPieceName(getState(curCell, board))[0]) {
        validMoves += cell;
      }
    }
  }
  if (isAI) {
    return validMoves;
  }

  if (validMoves.length() == 0) {
    return "-2";
  } // no possible moves error

  if (showValidMoves == true) {
    std::cout << "\n\n\nValid moves are: ";
    for (int i = 0; i < validMoves.length(); i += 2) {
      std::cout << validMoves[i] << validMoves[i + 1] << ", ";
    }
    return "-1";
  } // redo player turn error (not an error but idc)

  if (validMoves.find(futCell) != std::string::npos) {
    board = movePiece(futCell, curCell, board);
  } else {
    return "0";
  } // invalid move error
  return board;
} // successful returns board

std::string getOrDoMoves(std::string curCell, std::string futCell,
                         bool showValidMoves, bool isAI,
                         std::string board) { // UNFINISHED! DO NOT RUN
  std::string pType = getPieceName(getState(curCell, board));
  char pClr = pType[0];
  pType.erase(0, 1);
  std::string output;
  if (pType == "Pawn") {
    output = pawnMoves(curCell, futCell, showValidMoves, isAI, board);
  } else if (pType == "King") {
    output = kingMoves(curCell, futCell, showValidMoves, isAI, board);
  } else if (pType == "Queen") {
    output = queenMoves(curCell, futCell, showValidMoves, isAI, board);
  } else if (pType == "Rook") {
    output = rookMoves(curCell, futCell, showValidMoves, isAI, board);
  } else if (pType == "Bishop") {
    output = bishopMoves(curCell, futCell, showValidMoves, isAI, board);
  } else if (pType == "knight") {
    output = knightMoves(curCell, futCell, showValidMoves, isAI, board);
  } else {
    output = "-3";
  } // empty square error
  return output;
}

int getPositionalBonuses(char player, std::string board) {
  int addedVal = 0;
  for (int i = 0; i < board.length(); i++) {
    char piece = board[i];
    if (piece != 'n' && piece != 'N' && piece != 'p' && piece != 'P')
      continue;
    std::string pName = getPieceName(piece);
    if (pName[0] != player)
      continue;
    char pType = pName[1];
    if (pType == 'k') {
      int row = i / 8;
      int col = i % 8;
      int centerDistance = abs(3.5 - row) + abs(3.5 - col);
      addedVal += (7 - centerDistance);
    } else if (pType == 'p') {
      int row = i / 8;
      int col = i % 8;
      if (piece == 'p') {
        if (row == 1) {
          addedVal -= 30;
        } else {
          addedVal += ((row - 1) * 15);
        }
      } else if (piece == 'P') {
        if (row == 7) {
          addedVal -= 30;
        } else {
          addedVal += ((6 - row) * 15);
        }
      }
      if (col >= 3 && col <= 4) {
        addedVal += 20;
      }
    }
  }
  return addedVal;
}

int quietMoveScoreForSorting(std::string move, int depth) {
  int score = 0;
  if (depth >= 0 && depth < MAX_DEPTH) {
    if (move == killer[0][depth]) {
      score += 9000;
    } else if (move == killer[1][depth]) {
      score += 8000;
    }
  }
  // Add base score for pawn advances to make them more likely to move
  return score;
}
bool checkIfCheck(std::string board, char player) {
  std::string kingCell = "";
  for (int i = 0; i < board.length(); i++) {
    std::string piece = getPieceName(board[i]);
    if (piece[0] == player && piece[1] == 'K') {
      kingCell = getCellCode(i);
      break;
    }
  }
  if (kingCell.empty())
    return false;
  for (int i = 0; i < board.length(); i++) {
    std::string piece = getPieceName(board[i]);
    if (piece[0] == 'n' || piece[0] == player || piece[1] == 'K') {
      continue;
    }
    std::string moves = getOrDoMoves(getCellCode(i), "N1", false, true, board);
    if (moves.find(kingCell) != std::string::npos) {
      return true;
    }
  }
  return false;
}

int lookUpVal(std::string pName) {
  switch (pName[1]) {
  case 'P':
    return 100;
  case 'R':
    return 500;
  case 'B':
    return 330;
  case 'Q':
    return 900;
  case 'K':
    return 20000;
  case 'k':
    return 320;
  default:
    return 0;
  }
}

int boardValCalc(std::string board, char player, int count) {
  int tVal = 0;
  char otherPlayer;
  if (player == 'w') {
    otherPlayer = 'b';
  } else {
    otherPlayer = 'w';
  }
  for (int i = 0; i < board.length(); i++) {
    int val = lookUpVal(getPieceName(board[i]));
    char clr = getPieceName(board[i])[0];
    if (clr == player) {
      tVal += val;
    } else {
      tVal -= val;
    }
  }
  if (count >= 10) {
    if (checkIfCheck(board, player)) {
      tVal -= 50;
    }
    if (checkIfCheck(board, otherPlayer)) {
      tVal += 30;
    }
  }
  tVal += getPositionalBonuses(player, board);
  return tVal;
}

std::string simulate(std::string board, int d, char player, int alpha = -100000,
                     int beta = 100000, bool allowNullMove = false,
                     int count = 0) {
  nodes += 1;
  if (allowNullMove && d >= 4) {
    char otherPlayer = (player == 'b')
                           ? 'w'
                           : 'b'; // Give opponent a free turn with lower depth
    std::string nullResult =
        simulate(board, d - 2, otherPlayer, -beta, -beta + 1, false, count + 2);
    int nullScore = -std::stoi(nullResult.substr(4));
    if (nullScore >= beta) {
      return "----" + std::to_string(beta);
    }
  } // If even with free move opponent cant defend, this line is best prob
  std::string piecesToCheck = "";
  std::vector<std::string> piecesToCheckVec;
  std::string bestMove = "";
  for (int i = 0; i < board.length(); i++) {
    if (getPieceName(board[i])[0] == player) {
      piecesToCheckVec.push_back(getCellCode(i));
    }
  }
  std::shuffle(piecesToCheckVec.begin(), piecesToCheckVec.end(),
               std::mt19937{std::random_device{}()});
  for (int i = 0; i < piecesToCheckVec.size(); i++) {
    std::string capturingMoves = "";
    std::string quietMoves = "";
    std::string sortedMoves = "";
    std::vector<std::string> capturingList;
    std::vector<std::string> quietList;
    std::string cell = piecesToCheckVec[i];
    std::string moves = getOrDoMoves(cell, "N1", false, true, board);
    if (moves.length() != 0) {

      for (int j = 0; j < moves.length(); j += 2) {
        std::string cCell(1, moves[j]);
        cCell += moves[j + 1];
        if (getState(cCell, board) != '.') {
          capturingList.push_back(cCell);
        } else {
          quietList.push_back(cCell);
        }
      }
      std::sort(capturingList.begin(), capturingList.end(),
                [&](const std::string &a, const std::string &b) {
                  return boardValCalc(movePiece(a, cell, board), player,
                                      count) >
                         boardValCalc(movePiece(b, cell, board), player, count);
                });
      std::sort(quietList.begin(), quietList.end(),
                [&](const std::string &a, const std::string &b) {
                  return quietMoveScoreForSorting(a, d) >
                         quietMoveScoreForSorting(b, d);
                });

      for (int j = 0; j < capturingList.size(); j++) {
        sortedMoves += capturingList[j];
      }
      for (int j = 0; j < quietList.size(); j++) {
        sortedMoves += quietList[j];
      }
      int lenOfCaptureMoves = capturingList.size();
      int depth;
      for (int j = 0; j < sortedMoves.length(); j += 2) {
        if (lenOfCaptureMoves * 2 <= j) {
          depth = d - 1;
        } else {
          if (lenOfCaptureMoves == 0) {
            depth = d - 1;
          } else {
            depth = (d - static_cast<int>(round(static_cast<double>(j) /
                                                lenOfCaptureMoves)));
          }
        }
        std::string fCell(1, sortedMoves[j]);
        fCell += sortedMoves[j + 1];
        std::string nBoard = movePiece(fCell, cell, board);
        char otherPlayer;
        if (player == 'b') {
          otherPlayer = 'w';
        } else {
          otherPlayer = 'b';
        }
        if (checkPieceAmm((otherPlayer == 'w') ? 'k' : 'K', nBoard) == 0) {
          return cell + fCell + std::to_string(100000);
        }
        int score = 0;
        if (depth > 0) {
          std::string futureMove = simulate(nBoard, depth - 1, otherPlayer,
                                            -beta, -alpha, true, count + 1);
          score = -std::stoi(futureMove.substr(4));
        }

        else {
          score = boardValCalc(nBoard, player, count);
        }
        if (score > alpha || bestMove.length() == 0) {
          alpha = score;
          bestMove = (cell + fCell + std::to_string(score));
        }
        if (alpha >= beta) {
          if (j > lenOfCaptureMoves * 2 && depth >= 0 && depth < MAX_DEPTH) {
            killer[1][depth] = killer[0][depth];
            killer[0][depth] = cell + fCell;
          };
          return bestMove;
        }
      }
    }
  }
  return bestMove;
}

int main() {
  // setup
  doWeirdTerminalStuff();
  std::string board = "RNBQKBNRPPPPPPPP................................"
                      "pppppppprnbqkbnr"; // board

  int count = 0;
  bool listVals;
  std::cout << "Welcome to chess but bad and written in C++ by "
               "Krishna\n\nSettings:\n";
  bool aiON;
  std::cout << "1.)  AI on? (type 1 or 0):\t";
  std::cin >> aiON;
  std::cin.ignore();
  int d;
  if (aiON) {
    std::cout << "2.) Choose AI difficulty- baby (1), easy (2), medium (4), "
                 "hard (6) or extreme (7).\n    Hard (6) is recommended.Enter "
                 "the number you wish to play:\t";
    std::cin >> d;
    std::cin.ignore();
  }

  while (true) {
    listVals = false;
    std::string uInput;
    std::string curCell;
    std::string futureCell;
    char player = 'w';
    std::string word = "White";
    if (count % 2) {
      player = 'b';
      word = "Black";
      std::cout << "\n" << BLACK << word << "'s turn to play\n";
    } else {
      std::cout << WHITE << "\n" << word << "'s turn to play\n";
    }
    if (aiON && player == 'b') {
      std::cout << "AI is thinking...\n";
      nodes = 0;
      std::string aiMove =
          simulate(board, d, player, -100000, 100000, true, count);
      std::string originCell =
          std::string(1, aiMove[0]) + std::string(1, aiMove[1]);
      std::string cellToGoTo =
          std::string(1, aiMove[2]) + std::string(1, aiMove[3]);
      board = movePiece(cellToGoTo, originCell, board);
      std::cout << "Black played " << originCell << " to " << cellToGoTo
                << ". Searched " << nodes << " nodes.\n";
      count += 1;
      continue;
    }

    while (true) {
      printFullBoard(board);
      // add error validation for input misformatting
      if (player == 'w') {
        std::cout << WHITE
                  << "\n\nEnter move in form '<old square> to <new square>' or "
                     "'list <square>'\t";
      } else {
        std::cout << BLACK
                  << "\n\nEnter move in form '<old square> to <new square>' or "
                     "'list <square>'\t";
      }

      std::getline(std::cin, uInput);
      std::transform(uInput.begin(), uInput.end(), uInput.begin(), ::toupper);

      if (uInput.find("LIST") != std::string::npos) {
        listVals = true;
        futureCell = "N1";
        curCell = std::string(1, uInput[5]) + std::string(1, uInput[6]);
      }

      else {
        futureCell = std::string(1, uInput[6]) + std::string(1, uInput[7]);
        curCell = std::string(1, uInput[0]) + std::string(1, uInput[1]);
      }
      // try{getState(curCell,board)&getState(futureCell,board);}
      // catch(...){std::cout<<"\nSquare(s) not found!\n";}

      if (uInput.find("TO") == std::string::npos && listVals == false) {
        std::cout << "\nInvalid format!\n";
        continue;
      }

      if (getPieceName(getState(curCell, board))[0] != player) {
        std::cout << "\nYou can't move " << curCell
                  << ". It's not your piece!\n";
        continue;
      }
      break;
    }
    std::string result =
        getOrDoMoves(curCell, futureCell, listVals, false, board);
    if (result == "-3") {
      std::cout << futureCell << " is empty!";
      continue;
    } else if (result == "-2") {
      std::cout << "There are no possible moves for " << curCell;
      continue;
    } else if (result == "-1") {
      continue;
    } else if (result == "0") {
      std::cout << curCell << " to " << futureCell << " is an illegal move!";
      continue;
    } else {
      board = result;
      count += 1;
    }
    if (checkPieceAmm('K', board) == 0) {
      std::cout << "Black wins!";
      break;
    }
    if (checkPieceAmm('k', board) == 0) {
      std::cout << "White wins!";
      break;
    }
  }
  return 0;
}
