def days_until_empty(C, l, amm = 0, day = 0): return day if min((amm or C) + l, C) - day <= 0 else days_until_empty(C, l, min((amm or C) + l, C) - day, day + 1) # "os one-liners do Miguel" :(
