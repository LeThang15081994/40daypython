#hàm tính đệ quy
def dequy_calculation(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*dequy_calculation(n-1)
