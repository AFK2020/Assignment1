# Python program to find length of the
# longest valid substring

def maxLength(s):
    stack = []

    # Push -1 as the initial index to 
    # handle the edge case
    stack.append(-1) #in case we get closing parenthesis and when trying to pop we will get error so we place any dummy value
    max_len = 0

    # Traverse the string
    for i in range(len(s)):

        # If we encounter an opening parenthesis,
        # push its index
        if s[i] == '(':
            stack.append(i)
        else:

            # If we encounter a closing parenthesis, 
            # pop the stack
            stack.pop()

            # If stack is empty, push the current index
            # as a base for the next valid substring
            if not stack:
                stack.append(i) #in case our -1 was poped out so we put another dummy value so we don't pop from empty stack 
                #print(i,stack[-1])

            else:
              
                # Update maxLength with the current length 
                # of the valid parentheses substring
                #print(i)

                max_len = max(max_len, i - stack[-1])

    return max_len

if __name__ == "__main__":


    s = ")()()()))))()"
    #maxLength(s)
    print(maxLength(s))