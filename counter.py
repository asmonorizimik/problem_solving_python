# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}




# data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# i=0
# d={}
# sum=0
# while i<len(data):
#     d1=data[i]
#     if d1['item']=='item1':
#         sum+=d1['amount']
#         d[d1['item']]=sum
#     elif d1['item']=='item2':
#         sum1=d1['amount']
#         d[d1['item']]=sum1
#     else:
#         d[d1['item']]=d1['amount']
#     i+=1
# print(d)


