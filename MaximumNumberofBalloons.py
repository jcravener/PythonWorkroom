
# LeetCode: 1189. Maximum Number of Balloons

def maxNumberOfBalloons(text: str) -> int:
    if not len(text):
        return 0
    
    ban_mult = 1
    lo_mult = 2
    ct = 0
    mult = []

    for c in 'banlo':
        if c in 'ban':
            ct = text.count(c) // ban_mult
        else:
            ct =  text.count(c) // lo_mult
        if ct == 0:
            return 0
        else:
            mult.append(ct)
    
    return min(mult)

s = 'nlaebolko'
s = 'loonbalxballpoon'
#s = 'leetcode'
#s = 'lloo'
s = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(maxNumberOfBalloons(s))