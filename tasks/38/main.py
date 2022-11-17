# Task 38 - Sing Along

numbers = [{
    "number": "TEN",
    "plural": True
}, {
    "number": "NINE",
    "plural": True
}, {
    "number": "EIGHT",
    "plural": True
}, {
    "number": "SEVEN",
    "plural": True
}, {
    "number": "SIX",
    "plural": True
}, {
    "number": "FIVE",
    "plural": True
}, {
    "number": "FOUR",
    "plural": True
}, {
    "number": "THREE",
    "plural": True
}, {
    "number": "TWO",
    "plural": True
}, {
    "number": "ONE",
    "plural": False
}, {
    "number": "NO",
    "plural": True
}]

for number in numbers:
    if number['plural']:
        print(f"{number['number']} green bottles hanging on the wall")
        if not number['number'] == "NO":
            print("And if one green bottle should accidentally fall,")
            print("There'll be...\n")
    else:
        print(f"{number['number']} green bottle hanging on the wall")
        print("And if one green bottle should accidentally fall,")
        print("There'll be...\n")
