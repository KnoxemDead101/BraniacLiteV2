from pathlib import Path
from menu import display_menu, get_user_choice
# ==========================================================
# TroubleLog v0.1
# KTT Homelab Project
# ==========================================================

while True:

    display_menu()
    choice = get_user_choice()
    # ======================================================
    # CREATE SERVICE LOG
    # ======================================================

    if choice == "1":
        machine = input("Enter Machine Name: ").strip().lower()

        machine_folder = Path(f"../logs/{machine}")

        machine_folder.mkdir(parents=True, exist_ok=True)

        log_number = input("Enter Service Log Number: ").strip()

        filename = "service-log-" + log_number + ".md"

        file_path = machine_folder / filename

        if Path(file_path).exists():

            print(f"\nService Log {log_number} already exists " f"for machine {machine}. Please choose a different log number.")

        else:

            title = input("Title: ").strip()
            status = input("Status: ").strip()
            summary = input("Summary: ").strip()

            log_content = f"""# Service Log {log_number}

## Machine: 

{machine}

## Title

{title}

## Status

{status}

## Summary

{summary}
"""

            with open(file_path, "w", encoding="utf-8") as log_file:
                log_file.write(log_content)

            print(f"\nService Log {log_number} created successfully for machine {machine}.")

    # ======================================================
    # READ SERVICE LOG
    # ======================================================

    elif choice == "2":

        machine = input("Enter Machine Name: ").strip().lower()

        log_number = input("Enter Service Log Number: ").strip()

        filename = "service-log-" + log_number + ".md"

        machine_folder = Path(f"../logs/{machine}")
        file_path = machine_folder / filename

        if Path(file_path).exists():

            with open(file_path, "r", encoding="utf-8") as log_file:

                contents = log_file.read()

            print("\n===================================")
            print(contents)
            print("===================================")

        else:

            print(f"\nService Log {log_number} was not found for machine {machine}.")

    # ======================================================
    # UPDATE SERVICE LOG
    # ======================================================

    elif choice == "3":

        log_number = input("Enter Service Log Number: ").strip()

        filename = "service-log-" + log_number + ".md"

        machine = input("Enter Machine Name: ").strip().lower()
        machine_folder = Path(f"../logs/{machine}")
        file_path = machine_folder / filename

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

            print(f"\nService Log {log_number} updated successfully for machine {machine}.")

        else:

            print(f"\nService Log {log_number} was not found for machine {machine}.")

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