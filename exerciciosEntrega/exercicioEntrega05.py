#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def tirarVogais(frase):
    frase = frase.lower().strip()
    vogais = 'aeiouáàãâéèêíóòôõúù'
    qntVogais = 0
    for i in frase: 
        if i in vogais: 
            qntVogais += 1 
            frase = frase.replace(i, "")
    print(f'Esta é a frase sem vogais: {frase}')
    print(f'Foram retiradas {qntVogais} vogais')


tirarVogais('Olá, meu nome é igor')
