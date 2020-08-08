



def validIPAddress(IP):    # pass the ip into fn

   print(IP)
   print("this is  count value",IP.count("."))           # counts the number of (.) splitting

   def isIPv4(s):
      try:
          if str(int(s)) == s and 0 <= int(s) <= 255:     # leading 0 can be remove by using int(s) function
               return s

      except:
         return False

   if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):  # iterated until the splitting is completed

      return " THIS IS IPv4 ADDRESS"

   return "invalid"
print(validIPAddress("192.119.12.0"))