from fastapi import FastAPI

app = FastAPI()


@app.get("/namenumber/{name}")
def namenumber(name: str):
    def calculate_name_number(name: str) -> int:
        # Simple numerology: A=1, B=2, ..., Z=26, ignore non-letters, sum digits until single digit
        name = name.upper()
        total = sum((ord(char) - ord("A") + 1) for char in name if char.isalpha())
        while total > 9:
            total = sum(int(digit) for digit in str(total))
        return total

    return {
        "message": f"Hello, {name}! Your name number is {calculate_name_number(name)}."
    }
