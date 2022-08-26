# def sum_mix(arr):
#     i=0
#     sum=0
#     while i <len(arr):
#         if arr[i]==str(arr[i]):
#             a=int(arr[i])
#             sum+=a
#         else:
#             sum+=arr[i]
#         i+=1
#     return sum
# arr=[1,"4","5",3,2]
# print(sum_mix(arr))

# # input
# # 1,"4","5",3,2
# # output
# #15




# def shout(text):
#     return text.upper()
 
# def whisper(text):
#     return text.lower()
 
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
 
# greet(shout)
# greet(whisper)


from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
