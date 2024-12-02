# Fungsi untuk memeriksa apakah suatu karakter adalah operator
def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

# Fungsi untuk menetapkan prioritas operator
def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0

# Fungsi utama untuk mengonversi infix ke postfix
def infix_to_postfix(expression):
    # Inisialisasi stack kosong untuk operator
    stack = []
    # Inisialisasi list kosong untuk output postfix
    output = []
    
    # Iterasi melalui setiap karakter dalam ekspresi
    for char in expression:
        # Jika karakter adalah operand (angka atau huruf), tambahkan ke output
        if char.isalnum():
            output.append(char)
        # Jika karakter adalah '(', tambahkan ke stack
        elif char == '(':
            stack.append(char)
        # Jika karakter adalah ')', pop dari stack ke output sampai '(' ditemukan
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        # Jika karakter adalah operator
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    
    # Pop semua operator yang tersisa dalam stack ke output
    while stack:
        output.append(stack.pop())
    
    # Gabungkan list output menjadi string
    return ''.join(output)

# Contoh penggunaan
expression = "a+b*(c*d-e)"
postfix_expression = infix_to_postfix(expression)
print("Infix:    ", expression)
print("Postfix:  ", postfix_expression)
