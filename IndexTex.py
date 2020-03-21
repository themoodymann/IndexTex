# Written by Roger Wattenhofer

import os, glob, re

keywords = ["\\\\begin\\{definition\\}\\[(.*)\\]", "\\\\begin{theorem}\\[(.*)\\]", "\\\\emph\\{(.*)\\}", "\\\\caption\\{(.*)\\}"]
# possibly others: section, chapter, lemma, etc., feel free to update here


os.chdir("./input")
for file in glob.glob("*.tex"):
    texFile = open(file, 'r').read()
    for keyword in keywords:
        stopSymbol = keyword[-1]
        newText = ""
        last = 0
        for found in re.finditer(keyword, texFile):
            start = found.start()+len(keyword)-keyword.count("\\")-4
            end = texFile.find(stopSymbol, start)
            indexWord = texFile[start:end].lower()
            print(indexWord)
            newText = newText + texFile[last:end + 1] + "\\index{" + indexWord + "}"
            last = end+1
    newText = newText + texFile[last:]
    texFile = newText
    with open("../output/"+file, "w") as writefile:
        writefile.write(texFile)

# possibly the whole replacement can be simplified with some regex lambda magic, e.g.
# re.sub(keyword, lambda match : '\\begin\{definition\}\[' + match.group(1) + '\]\index\{' + match.group(1).lower() + '\}', str)
