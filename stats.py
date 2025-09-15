
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    counts = {}
    for t in text:
        key = t.lower()
        if key.isalpha() is False:
            continue
        if counts.get(key, 0):
            counts[key] += 1
        else:
            counts[key] = 1
    return(counts)

def gen_report(text):
    report = char_count(text)
    sorted_by_count = dict(sorted(report.items(), key=lambda item: item[1], reverse=True))
    for item in sorted_by_count.items():
        print(f"{item[0]}: {item[1]}")
