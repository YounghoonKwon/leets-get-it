class Solution:
    def intToRoman(self, num: int) -> str:
        roman1 = ['I','X','C','M']
        roman5 = ['V','L','D']
        roman_result = []
        num_list = list(str(num))
        num_list.reverse()
        for i,v in enumerate(num_list):
            if v in ['1','2','3']:
                roman_result.append((roman1[i]*int(v)))
            elif v == '4':
                roman_result.append((roman1[i]+roman5[i]))
            elif v == '9':
                roman_result.append((roman1[i]+roman1[i+1]))
            elif int(v) >=5:
                roman_result.append((roman5[i]+(roman1[i]*(int(v)-5))))
            else:
                continue
        roman_result.reverse()
        return (''.join(roman_result))
