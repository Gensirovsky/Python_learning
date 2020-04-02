def convert(s, numRows):
    if numRows == 1: return s
    else:
        result = [''] * numRows
        row, direction = 0, 1
        for _ in s:
            result[row] += _
            if row == 0: direction = 1
            elif row == numRows - 1: direction = -1
            row += direction
        return ''.join(result)