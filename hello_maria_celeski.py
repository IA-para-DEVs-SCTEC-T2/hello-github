def contar_emails_validos(lista_emails):
    """Conta quantos itens da lista são e-mails válidos (contêm '@' e '.')."""
    contador = 0
    for email in lista_emails:
        if "@" in email and "." in email:
            contador += 1
    return contador

emails = ["maria@gmail.com", "teste", "joao@empresa.com", "abc"]
print(contar_emails_validos(emails))
