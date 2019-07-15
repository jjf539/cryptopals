#Exclusive or or exclusive disjunction is a logical operation that outputs true only when inputs differ (one is true, the other is false).

def fixed_xor(str1,str2):

  #convert hex strings to their integer equivalent
  int_str1 = int(str1,16)
  int_str2 = int(str2,16)

  #xor str1 against str2 with xor (^) operator
  xord = int_str1 ^ int_str2

  #convert xord variable back to hex, and strip of the first two characters (0x)
  #compare this value to the value given by the challenge
  if hex(xord)[2:] == "746865206b696420646f6e277420706c6179":
    print("Success!")
    return
  else:
    print("Failed...")


fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
