from pathlib import Path
# ==========================================================
# TroubleLog v0.1
# KTT Homelab Project
# ==========================================================

while True:

    print("\n===================================")
    print("          TroubleLog v0.1")
    print("===================================")
    print("1. Create Service Log")
    print("2. Read Service Log")
    print("3. Update Service Log")
    print("4. Exit")

    choice = input("\nSelect an option: ").strip()

    # ======================================================
    # CREATE SERVICE LOG
    # ======================================================

    if choice == "1":

        log_number = input("Enter Service Log Number: ").strip()

        filename = "service-log-" + log_number + ".md"

        file_path = "../logs/" + filename

        if Path(file_path).exists():

            print(f"\nService Log {log_number} already exists.")

        else:

            title = input("Title: ").strip()
            status = input("Status: ").strip()
            summary = input("Summary: ").strip()

            log_content = f"""# Service Log {log_number}

## Title

{title}

## Status

{status}

## Summary

{summary}
"""

            with open(file_path, "w", encoding="utf-8") as log_file:
                log_file.write(log_content)

            print(f"\nService Log {log_number} created successfully.")

    # ======================================================
    # READ SERVICE LOG
    # ======================================================

    elif choice == "2":

        log_number = input("Enter Service Log Number: ").strip()

        filename = "service-log-" + log_number + ".md"

        file_path = "../logs/" + filename

        if Path(file_path).exists():

            with open(file_path, "r", encoding="utf-8") as log_file:

                contents = log_file.read()

            print("\n===================================")
            print(contents)
            print("===================================")

        else:

            print(f"\nService Log {log_number} was not found.")

    # ======================================================
    # UPDATE SERVICE LOG
    # ======================================================

    elif choice == "3":

        log_number = input("Enter Service Log Number: ").strip()

        filename = "service-log-" + log_number + ".md"

        file_path = "../logs/" + filename

        if Path(file_path).exists():

            update_status = input("Updated Status: ").strip()
            update_notes = input("Update Notes: ").strip()

            update_content = f"""

----------------------------------------

## Service Log Update

**Updated Status**

{update_status}

### Notes

{update_notes}

"""

            with open(file_path, "a", encoding="utf-8") as log_file:
                log_file.write(update_content)

            print(f"\nService Log {log_number} updated successfully.")

        else:

            print(f"\nService Log {log_number} was not found.")

    # ======================================================
    # EXIT
    # ======================================================

    elif choice == "4":

        print("\nClosing TroubleLog...")
        break

    # ======================================================
    # INVALID MENU CHOICE
    # ======================================================

    else:

        print("\nInvalid menu selection. Please choose an option from 1-4.")