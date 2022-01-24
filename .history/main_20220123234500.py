def fizzBuzz(n):
  """
  :type n: int
  :rtype: List[str]
  """
  output = []
  for i in range (1,n):   
   if(i%3 ==0 and i%5 ==0):
      output.append('FizzBuzz')     
   elif(i % 3 == 0 ):
      output.append('Fizz')
   elif(i%5 == 0):
      output.append('Buzz')

   elif (i % 3 !=0):
      output.append(i)
   elif (i % 5 !=0):
      output.append(i)
  
  print('Output: ', output)


fizzBuzz(15)