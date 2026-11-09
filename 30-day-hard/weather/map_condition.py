"""Map a weather condition string to the tracker's weather code."""
import sys

RULES = [
    ("rain", ("rain", "shower", "drizzle", "thunder", "storm")),
    ("fog", ("fog", "mist", "haze")),
    ("clouds", ("cloud", "overcast")),
    ("clear", ("sun", "clear", "fair")),
]

def map_condition(text: str) -> str:
    t = text.lower()
    for code, words in RULES:
        if any(w in t for w in words):
            return code
    return "clouds"

if __name__ == "__main__":
    print(map_condition(" ".join(sys.argv[1:])))
