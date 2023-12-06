import json

def show_notes(notes):
    print("Your notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def add_note(notes, new_note):
    notes.append(new_note)
    print("Note added!")

def delete_note(notes, index):
    if 1 <= index <= len(notes):
        deleted_note = notes.pop(index - 1)
        print(f"Note deleted: {deleted_note}")
    else:
        print("Incorrect index")

def notes_app():
    notes = []

    while True:
        print("\n1. View notes")
        print("2. Add a note")
        print("3. Delete note")
        print("4. Go out")

        choice = input("Choose an action: ")

        if choice == '1':
            show_notes(notes)
        elif choice == '2':
            new_note = input("Enter a new note: ")
            add_note(notes, new_note)
        elif choice == '3':
            index = int(input("Enter the index of the note to be deleted: "))
            delete_note(notes, index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Incorrect choice")

if __name__ == "__main__":
    notes_app()
