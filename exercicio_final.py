from contato import Contact
from agenda import ContactBook

agenda = ContactBook()

while True:
    print(f"\n ------ Menu Agenda de Contatos ------"
          '''
            1. Adicionar Contato
            2. Remover Contato
            3. Listar Contatos
            4. Pesquisar Contato
            5. Sair
          ''')

    choice = input("Escolha uma opção:\n")

    if choice == "1":
        name = input("Digite o nome:\n")
        phone = input("Digite o telefone:\n")
        email= input("Digite o email:\n")

        contact = Contact(name, phone, email)
        agenda.add_contact(contact)
        print("Contato adicionado com sucesso!\n")
        print(contact)

    elif choice == "2":
        name = input("Informe o nome do contato que deseja remover:\n")
        contact = agenda.search_contact(name)
        if contact:
            agenda.remove_contact(contact)
            print("Contato removido com sucesso!")

    elif choice == "3":
        agenda.display_contacts()

    elif choice == "4":
        name = input("Informe o nome do contato que deseja encontrar:\n")
        agenda.search_contact(name)

    elif choice == "5":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção incorreta, selecione uma opção válida.\n")
        continue


