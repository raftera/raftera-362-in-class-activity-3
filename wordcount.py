def wordcount(string):
    if isinstance(string, str):
        count = 0
        for i in string:
            if i == " ":
                count += 1
        return count
    else:
        return -1