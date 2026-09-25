def transpose(mat: list[list[float | int]]) -> list[list]:
    """Меняет строки и столбцы местами. Пустая матрица [] → []. Если матрица «рваная» (строки разной длины) — ValueError."""

    if len(mat) == 0:
        return []
    
    if not all(len(mat[i]) == len(mat[0]) for i in range(1, len(mat))):
        raise ValueError
    
    n, m = len(mat), len(mat[0])
    result = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][i] = mat[i][j]

    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждой строке. Если матрица «рваная» (строки разной длины) — ValueError."""

    if len(mat) == 0:
        return 0
    
    if not all(len(mat[i]) == len(mat[0]) for i in range(1, len(mat))):
        raise ValueError
    
    return [sum(row) for row in mat]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Сумма по каждому столбцу. Если матрица «рваная» (строки разной длины) — ValueError."""

    if len(mat) == 0:
            return 0
        
    if not all(len(mat[i]) == len(mat[0]) for i in range(1, len(mat))):
        raise ValueError
        
    n, m = len(mat), len(mat[0])

    return [sum(mat[i][j] for i in range(n)) for j in range(m)]