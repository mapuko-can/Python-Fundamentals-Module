def winning_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left = ticket[:10]
    right = ticket[10:]
    for symbol in winning_symbols:
        for uninterrupted_range in range(10, 5, -1):
            uninterrupted_symbols = symbol * uninterrupted_range
            if uninterrupted_symbols in left and uninterrupted_symbols in right:
                if uninterrupted_range == 10:
                    return f'ticket "{ticket}" - {uninterrupted_range}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_range}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(winning_ticket(ticket))








