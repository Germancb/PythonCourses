text = "   hello world!   "
print(f"Original: '{text}'")

stripped_text = text.strip()
print(f"strip(): '{stripped_text}'")

rstripped_text = text.rstrip()
print(f"rstrip(): '{rstripped_text}'")

text2 = "abcdeffedcba"
stripped_text2 = text2.strip('abc')
print(f"strip() with chars: '{stripped_text2}'")

rstripped_text2 = text2.rstrip('abc')
print(f"rstrip() with chars: '{rstripped_text2}'")
# In summary, choose strip() when you need to remove characters from both ends of a string
#  and rstrip() when you only need to remove characters from the end of the string.