
# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n===== Menu principal =====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: Quitter')
    print('===========================')

    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1':
            lister_todos()
        case '2':
            creer_todo()
        case '3':
            modifier_statut_todo()
        case '4':
            supprimer_todo()
        case 'q':
            print("Au revoir !")
        case _:
            print("Choix invalide.")
