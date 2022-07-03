class Solution(object):
    def minimumSum(self, num):
        liste=[0]*4
        i=0
        while num!=0:
            liste[i]=num%10
            num=num//10
            i+=1
        liste=sorted(liste)
        new1=liste[0]*10+liste[3]
        new2=liste[1]*10+liste[2]
        return new1+new2