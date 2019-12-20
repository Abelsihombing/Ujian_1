# # Soal 1
# def Hashtag(string):
#     kata = []
#     kata2 = []
#     kata1 = string.split()
#     # kata2 = kata1.title()
#     # kata3 = kata2.replace(',')
#     for i in kata1:
#         kata1 = i.capitalize()
#         kata.append(kata1)

# Hashtag('Hello there how are you doing')

# Soal 2
# def create_phone_number(number):
#     list1 = []
#     for num in number:
#         list1.append("".join(str(num)))
#     p = list1

#     a = "".join(p[0:3])
#     b = "".join(p[3:6])
#     c = "".join(p[6:10])
      
#     print("({}) {}-{}".format(a, b, c))
    
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# Soal 3
# def sort_odd_even(num):
#     genap = []
#     ganjil = []

#     for item in num:
#         if item % 2 == 0:
#             genap.append(item)
#         else:
#             ganjil.append(item)

#     genap.sort(reverse = True)
#     ganjil.sort()
#     return genap+ganjil

# print(sort_odd_even([5,3,2,8,1,4]))

# # Soal 4
# def hollowTriangle(n) : 
#     k = 0
#     for i in range(1,n+1) : 
#         for j in range(i,n) : 
#             print('_ ', end='_') 
          
#         while (k != (2 * i - 1)) : 
#             if (k == 0 or k == 2 * i - 2) : 
#                 print('#', end='') 
#             else : 
#                 print(' _ ', end ='_') 
#             k = k + 1
#         k = 0; 
#         print ("")  
          
#     for i in range(0, 2 * n -1) : 
#         print ('#', end = '') 
  
# hollowTriangle(6) 
