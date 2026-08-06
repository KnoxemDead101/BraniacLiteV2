from pathlib import Path

from menu import display_menu, get_user_choice


# ==========================================================
# TroubleLog v0.2
# KTT Homelab Project
# ==========================================================

SOURCE_DIRECTORY = Path(__file__).resolve().parent
PROJECT_DIRECTORY = SOURCE_DIRECTORY.parent
LOGS_DIRECTORY = PROJECT_DIRECTORY / "logs"

print(f"Current File: {__file__}")
print(f"Project Directory: {PROJECT_DIRECTORY}")
print(f"Logs Directory: {LOGS_DIRECTORY}")

while True:

    display_menu()
    choice = get_user_choice()

    # ======================================================
    # CREATE SERVICE LOG
    # ======================================================

    if choice == "1":

        machine = input("Enter Machine Name: ").strip().lower()
        log_number = input("Enter Service Log Number: ").strip()

        machine_folder = LOGS_DIRECTORY / machine
        machine_folder.mkdir(parents=True, exist_ok=True)

        filename = f"service-log-{log_number}.md"
        file_path = machine_folder / filename

        if file_path.exists():

            print(
                f"\nService Log {log_number} already exists for machine "
                f"{machine}. Please choose a different log number."
            )

        else:

            title = input("Title: ").strip()
            status = input("Status: ").strip()
            summary = input("Summary: ").strip()

            log_content = f"""# Service Log {log_number}

## Machine

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

            print(
                f"\nService Log {log_number} created successfully "
                f"for machine {machine}."
            )

    # ======================================================
    # READ SERVICE LOG
    # ======================================================

    elif choice == "2":

        machine = input("Enter Machine Name: ").strip().lower()
        log_number = input("Enter Service Log Number: ").strip()

        machine_folder = LOGS_DIRECTORY / machine
        filename = f"service-log-{log_number}.md"
        file_path = machine_folder / filename

        if file_path.exists():

            with open(file_path, "r", encoding="utf-8") as log_file:
                contents = log_file.read()

            print("\n===================================")
            print(contents)
            print("===================================")

        else:

            print(
                f"\nService Log {log_number} was not found "
                f"for machine {machine}."
            )

    # ======================================================
    # UPDATE SERVICE LOG
    # ======================================================

    elif choice == "3":

        machine = input("Enter Machine Name: ").strip().lower()
        log_number = input("Enter Service Log Number: ").strip()

        machine_folder = LOGS_DIRECTORY / machine
        filename = f"service-log-{log_number}.md"
        file_path = machine_folder / filename

        if file_path.exists():

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

            print(
                f"\nService Log {log_number} updated successfully "
                f"for machine {machine}."
            )

        else:

            print(
                f"\nService Log {log_number} was not found "
                f"for machine {machine}."
            )

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

        print(
            "\nInvalid menu selection. "
            "Please choose an option from 1-4."
        )