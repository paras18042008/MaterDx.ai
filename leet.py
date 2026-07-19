class Solution(object):
    def romanToInt(self, s):

        l=list(s)

        values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
       }

               
        n=len(l)
        c=0

        for i in range(n):
            if (i+1)<n:

                if l[i]<l[i+1]:
                    t=l[i]
                    c=c+ (values[t]-1)
                else:
                    t=l[i]
                    c= c + values[t]

            else:
                t=l[i]
                c= c + values[t]


        return c