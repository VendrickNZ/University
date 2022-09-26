def lcs(s1, s2):
   """finds longest common substring integer"""
   rows = len(s1)
   columns = len(s2)

   table = [[0 for i in range(columns)] for j in range(rows)]
   if len(table) == 0:
      return ""
   for i in range(rows):
      for j in range(columns):
         if i or j == 0:
               table[i][j] = 0
         if s1[i] == s2[j]:
               table[i][j] = table[i-1][j-1] + 1
         elif s1[i] != s2[j]:
               table[i][j] = max(table[i][j-1], table[i-1][j])
   result = backtrack(table, s1, s2)
   result =  "".join(result)
   return result

def backtrack(table, a, b):
   """backtracks through LCS table to find string solution"""
   i = len(table) - 1
   j = len(table[0]) - 1
   result = []
   while i >= 0 and j >= 0:
      if a[i] == b[j]:
         result.insert(0, a[i])
         i -= 1
         j -= 1
      elif a[i] != b[j]:
         if max(table[i - 1][j], table[i][j-1]) == table[i-1][j]:
               if i > 0:
                  i -= 1
               else:
                  j -= 1
         else:
               if j > 0:
                  j -= 1
               else:
                  i -= 1
   return result

	
def line_edits(a, b, na=None, nb=None, cache=None):
   if na is None:
      na = len(a)
      nb = len(b)
   if cache is None:
      cache = {}
   if (na, nb) in cache:
      return cache[(na, nb)]
   if na == 0 or nb == 0:
      cache[(na, nb)] = max(na, nb)
   elif a[na - 1] == b[nb - 1]:
      value = line_edits(a, b, na - 1, nb - 1, cache)
      cache[(na, nb)] = value
   else:
      delete_cost = 1 + line_edits(a, b, na - 1, nb, cache)
      insert_cost = 1 + line_edits(a, b, na, nb - 1, cache)
      replace_cost = 1 + line_edits(a, b, na - 1, nb - 1, cache)
      value = min([delete_cost, insert_cost, replace_cost])
      cache[(na, nb)] = value
   return cache[(na, nb)]


print(line_edits("GACTGCGACTGC", "ATCTCCGATCTCCG"))
# s1 = "Line1\nLine2\nLine3\nLine4\n"
# s2 = "Line1\nLine3\nLine4\nLine5\n"
# table = line_edits(s1, s2)
# for row in table:
#    print(row)