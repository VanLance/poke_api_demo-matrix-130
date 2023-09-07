def attendance_award(astring):
  return astring.count('A') < 2 and 'LLL' not in astring

print(attendance_award("PPALLP"),True)
print(attendance_award("PPALLL"),False)