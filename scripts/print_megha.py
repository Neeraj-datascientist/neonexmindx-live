txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()
cards = [c for c in txt.split('<article class="trainer-card"') if 'Megha' in c]
if cards:
    print(cards[0][:1000])

