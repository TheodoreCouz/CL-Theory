v = ["a", "e", "i", "o", "u", "y"]
c = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]


def decomp(word, p=False):
    in_stem = True
    in_mid = False
    res = ["", [], ""]
    buffer = ""

    for letter in word:
        if (letter.lower() not in c+v): raise ValueError("Bad word!")
        if (in_stem and not in_mid):
            if (letter in c): buffer += letter
            else:
                res[0] = buffer
                buffer = letter
                in_mid = True
        else:
            if (in_mid and in_stem):
                if (letter in c): in_stem = False
                buffer += letter
            elif (in_mid and not in_stem):
                if (letter in c): buffer += letter
                else:
                    in_stem = in_mid = True
                    res[1].append(buffer)
                    buffer = letter

    if (in_stem and not in_mid): res[0] = buffer
    elif (buffer[-1] in c): res[1].append(buffer)
    else: res[2] = buffer
    
    s = f"[{res[0]}]"
    for i in res[1]:
        s = f"{s}({i})"
    s = f"{s}[{res[2]}]"
    if (p): print(s)
    return res

def get_m(word):
    return len(decomp(word)[1])

def apply_rule(word, condition, rem, repl=""):
    if (condition(word[:len(word)-len(rem)])):
        new_word = word[:len(word)-len(rem)]+repl
        return new_word
    else: return word

def m_bigger_than_0(word): return get_m(word)>0

def at_least_one_v(word):
    for letter in word:
        if letter in v: return True
    return False

if __name__ == "__main__":
    # words = ["tree", "by", "trees", "trouble", "oats", "troubles", "OEEaten"]
    # for i in words: 
    #     decomp(i, p=True)
    print(apply_rule("feed", m_bigger_than_0, "eed", "ee")) #should print <feed>
    print(apply_rule("agreed", m_bigger_than_0, "eed", "ee")) #should print <agree>
    print(apply_rule("plastered", at_least_one_v, "ed")) #should print <plaster>
    print(apply_rule("bled", at_least_one_v, "ed")) #should print <bled>
    print(apply_rule("motoring", at_least_one_v, "ing")) #should print <motor>
    print(apply_rule("sing", at_least_one_v, "ing")) #should print <sing>