# 1918 - 후위 표기식 (Gold 3)
import sys
entire = sys.stdin.readline().rstrip()
stack = []
ans = ''
for c in entire:
  if c.isalpha():
    ans += c
  else:
    if c == '(':
      stack.append(c)
    elif c == '*' or c == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        ans += stack.pop()
      stack.append(c)
    elif c == '+' or c == '-':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.append(c)
    elif c == ')':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.pop()

while stack:
  ans += stack.pop()

print(ans)
