def dao_nguoc_list(chuoi):
    return chuoi[::-1]
input_list = input("mời nhập chuỗi cần đảo ngược:")
numbers = list(map(int,input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)

print(" List đảo ngược là: ",list_dao_nguoc)