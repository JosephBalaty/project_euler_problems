# use a recursive function to find the max of multiplying 2 3 digit numbersr
# that create a palindrome as the product.

# components needed
#   Determine whether a result is a palindrome
#       Turn the result into a string and reverse it, and check if it's equal to the original result.
#   Find the maximum result possible

left = 999
right = 999
pals = {}


def isPal(result):
    if result in pals:
        return pals[result]
    if (str(result) == str(result)[::-1]):
        pals[result] = True
        return True
    else:
        pals[result] = False
        return False


def max_pal():
    l = 0
    r = 0
    max_p = -1

    for i in range(left, l, -1):
        for j in range(right, r, -1):
            res = i * j
            if (isPal(res)):
                if res > max_p:
                    max_p = res
    return max_p


print(max_pal())
