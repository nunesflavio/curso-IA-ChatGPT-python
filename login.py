nomeUsuario = input("Qual o seu nome? ")
senhaUsuario = input("Qual a sua senha? ")

if nomeUsuario == 'Legion' and senhaUsuario == '123':
    print("Acesso liberado")
else:
    print("Acesso negado! Senha ou usuario incorretos")