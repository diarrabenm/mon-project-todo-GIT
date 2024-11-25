bonjours code todo
# Liste pour stocker les todos
todos = []

# Fonction pour lister les todos
def lister_todos():
    print('aucun todo disponible')
    if not todos:
        print("================")
    else:
        print("\n===== Liste des todos =====")
        for index, todo in enumerate(todos):
            print(f"{index + 1}. {todo['titre']} - Statut : {todo['statut']}")
        print("===========================")


# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todo = {
        "titre": titre,
        "statut": "À faire"  # Par défaut, le statut est "À faire"
    }
    todos.append(todo)
    print(f'Todo "{titre}" ajouté avec succès.')

# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    if not todos:
        print("Aucun todo disponible à modifier.")
        return

    lister_todos()
    try:
        choix = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if choix < 0 or choix >= len(todos):
            print("Numéro invalide.")
            return

        # Logique de changement de statut
        if todos[choix]["statut"] == "À faire":
            todos[choix]["statut"] = "Fait"
        elif todos[choix]["statut"] == "Fait":
            todos[choix]["statut"] = "À fair"  #Erreur volontaire sans le 'e'
        else:
            print("Statut inconnu, impossible de le changer.")
        
        print(f'Statut du todo "{todos[choix]["titre"]}" mis à jour : {todos[choix]["statut"]}')
    except ValueError:
        print("Veuillez entrer un numéro valide.")
 
# Fonction pour supprimer un todo
def supprimer_todo():
    if not todos:
        print("Aucun todo disponible à supprimer.")
        return

    lister_todos()
    try:
        choix = int(input("Entrez le numéro du todo à supprimer : ")) - 1
        if choix < 0 or choix >= len(todos):
            print("Numéro invalide.")
            return

        todo_supprime = todos.pop(choix)
        print(f'Todo "{todo_supprime["titre"]}" supprimé avec succès.')
    except ValueError:
        print("Veuillez entrer un numéro valide.")

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
    choix = input("=> Choix : ")
    match choix:
        case '1': lister_todos()
        case '2': creer_todo()
        case '3': modifier_statut_todo()
        case '4': supprimer_todo()
        case 'q': print("Au revoir !")
        case _: print("Choix invalide.")

