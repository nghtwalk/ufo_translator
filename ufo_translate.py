import random


dialetos = {
    "marciano": {
        "a": "∆", "b": "ß", "c": "©", "d": "ↂ", "e": "ξ",
        "f": "ϝ", "g": "Ϭ", "h": "Ψ", "i": "ι", "j": "λ",
        "k": "Ҡ", "l": "⊢", "m": "♒", "n": "∏", "o": "◎",
        "p": "φ", "q": "ℚ", "r": "☼", "s": "Ϟ", "t": "✦",
        "u": "☉", "v": "√", "w": "ω", "x": "✕", "y": "¥",
        "z": "Ƶ", " ": "   "
    },
    "venusiano": {
        "a": "⚡", "b": "⍾", "c": "⊗", "d": "◇", "e": "∑",
        "f": "ϟ", "g": "¤", "h": "⌬", "i": "☯", "j": "♆",
        "k": "☣", "l": "∞", "m": "⧫", "n": "✡", "o": "◎",
        "p": "✪", "q": "☘", "r": "✺", "s": "⚔", "t": "☢",
        "u": "☄", "v": "✿", "w": "⍙", "x": "☘", "y": "✡",
        "z": "☠", " ": "   "
    },
    "galactico": {
        "a": "🜚", "b": "𐌁", "c": "☊", "d": "𐌃", "e": "✶",
        "f": "𐍆", "g": "𐌲", "h": "𐋅", "i": "꙰", "j": "𐌾",
        "k": "ꙮ", "l": "𐌻", "m": "𐌼", "n": "𐌽", "o": "𐍉",
        "p": "𐍀", "q": "𐌵", "r": "𐍂", "s": "𐍃", "t": "𐌕",
        "u": "𐌿", "v": "𐍊", "w": "𐍅", "x": "𐍇", "y": "𐍅",
        "z": "𐍆", " ": "   "
    }
}


extras = ["👽", "🚀", "🛸", "🌌", "💫", "🔮", "🪐", "⚛"]

def traduzir(frase, dialeto):
    traducao = ""
    tabela = dialetos.get(dialeto, dialetos["marciano"])
    for letra in frase.lower():
        if letra in tabela:
            simbolo = tabela[letra]
            
            if random.random() < 0.2:
                simbolo += random.choice(extras)
            traducao += simbolo
        else:
            traducao += letra
    return traducao

def decodificar(frase):
    
    respostas = [
        "Mensagem diz: 'Estamos chegando' 👾",
        "Traduzido: 'Paz e bananas para todos' 🍌",
        "Alerta: 'Prepare-se para o contato imediato' 🛸",
        "Mensagem confusa: 'O planeta é delicioso' 🌍🍴",
        "Interferência cósmica, impossível traduzir..."
    ]
    return random.choice(respostas)

# Programa principal
while True:
    print("\n👽 Bem-vindo ao UFO Translator 🚀")
    print("Dialetos disponíveis: marciano, venusiano, galactico")
    print("Escolha uma opção:")
    print("1 - Traduzir")
    print("2 - Decodificar")
    print("3 - Sair")

    escolha = input("> ").strip()

    if escolha == "1":
        dialeto = input("Escolha o dialeto: ").strip().lower()
        frase = input("Digite sua mensagem: ")
        print("\n🔮 Tradução alienígena:")
        print(traduzir(frase, dialeto))

    elif escolha == "2":
        frase = input("Cole o texto alienígena: ")
        print("\n📡 Tradução (aproximada):")
        print(decodificar(frase))

    elif escolha == "3":
        print("Encerrando comunicação intergaláctica... 🛸")
        break
    else:
        print("Opção inválida!")
