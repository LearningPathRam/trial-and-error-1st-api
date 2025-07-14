from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

@require_GET
def luckynumber_form(request):
    return render(request, "luckynumber/luckynumber_form.html")

def result_page(request):
    name = request.GET.get("name", "")
    if not name:
        return JsonResponse({"error": "Name is required."}, status=400)
    return luckynumber(request, name)

def luckynumber(request, name):
    def calculate_name_number(name: str) -> int:
        # Simple numerology: A=1, B=2, ..., Z=26, ignore non-letters, sum digits until single digit
        name = name.upper()
        total = sum((ord(char) - ord("A") + 1) for char in name if char.isalpha())
        while total > 9:
            total = sum(int(digit) for digit in str(total))
        return total

    return JsonResponse(
        {
            "message": f"Hello, {name}! Your lucky number is {calculate_name_number(name)}."
        }
    )
