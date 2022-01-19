import re

from libvoikko import Voikko

# v = Voikko('fi-x-morphoid')
v = Voikko("fi")

# Replace all non letter characters with space
RE_WS_REPLACE = re.compile("[^\w]", re.UNICODE)
RE_FIND_COMPOUNDS = re.compile(r"\(([\w\+]+)\)", re.UNICODE)


def voikko_analyze(text):
    text = RE_WS_REPLACE.sub(" ", text)
    words = text.split(" ")
    # Strip spaces
    words = [x.strip() for x in words]
    # Remove empty items
    words = filter(None, words)
    # Loop all words and analyze them
    analyzed = []
    for word in words:
        aword = v.analyze(word)
        if aword:
            i = 0
            for f in aword:
                i += 1
                print(i, f)
                f["found"] = True
                f["original"] = word
                wordbases = RE_FIND_COMPOUNDS.findall(f.get("WORDBASES", ""))
                f["wordbase_list"] = [x for x in wordbases if not x.startswith("+")]
                analyzed.append(f)
        else:
            analyzed.append({"BASEFORM": word, "found": False, "original": word})
    return analyzed


def baseform_text(text):
    analyzed = voikko_analyze(text)
    wordlist = [x["BASEFORM"].lower() for x in analyzed]
    wordlist += [x["original"].lower() for x in analyzed]
    base_text = " ".join(set(wordlist))
    return base_text


if __name__ == "__main__":
    import sys

    words = sys.argv[1:]
    print(baseform_text(" ".join(words)))
