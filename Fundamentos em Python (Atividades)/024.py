#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").

#entrada de dados
Senha = input("Digite a senha: ").strip()
Senhafixa = "python123"

#lógica

if  Senha == Senhafixa:
    print("Senha correta")
elif Senhafixa == Senha.lower():
    print("Verifique o CapsLook")
else:
    print("Senha incorreta")


#correção

if  Senha == Senhafixa:
    print("Senha correta")
else:
    print("Senha incorreta")