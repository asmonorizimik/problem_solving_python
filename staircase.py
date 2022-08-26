# n=int(input())
# i=0
# while i<n:
#     j=0
#     while j<n:
#         if i+j>=n-1:
#             print("#",end='')
#         else:
#             print(" ",end='')
#         j+=1
#     i+=1
#     print()





def staircase(n):
    i=0
    while i<n:
        j=0
        while j<n:
            if i+j>=n-1:
                print("#",end='')
            else:
                print(" ",end='')
            j+=1
        i+=1
        print()

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)



     #
    ##
   ###
  ####
 #####
######

      #
     ##
    ###
   ####
  #####
 ######




# def staircase(n):
#     for i in range(0,n):
#         for j in range(0,n):
#             if i + j >= n-1:
#                 print("#",end='') 
#             else:
#                 print(" ",end='')
#         print("\r")

# if __name__ == '__main__':
#     n = int(input())

#     staircase(n)