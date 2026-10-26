
from ingest import ingest_documents
from chat import chat


def main():
    print("\n========== DOCUMENT RAG ==========")

    while True:
        print("\n1. Ingest documents")
        print("2. Chat with documents")
        print("3. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            try:
                ingest_documents()
            except Exception as error:
                print(f"\nIngestion failed: {error}")
        elif choice == "2":
            try:
                chat()
            except Exception as error:
                print(f"\nChat failed: {error}")
        elif choice == "3":
            print("\nThank you for using Document RAG!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
