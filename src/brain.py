from pathlib import Path
from menu import display_menu, get_user_choice
from datetime import datetime 


# ==========================================================
# TroubleLog v0.2
# KTT Homelab Project
# ==========================================================

SOURCE_DIRECTORY = Path(__file__).resolve().parent
PROJECT_DIRECTORY = SOURCE_DIRECTORY.parent
LOGS_DIRECTORY = PROJECT_DIRECTORY / "logs"

created_timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M-%S")
last_updated_timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S")
exact_time = datetime.now().time()


def directory_info():
    print(f"Source Directory: {SOURCE_DIRECTORY}")
    print(f"Project Directory: {PROJECT_DIRECTORY}")
    print(f"Logs Directory: {LOGS_DIRECTORY}")
    print(f"Created Timestamp: {created_timestamp}")

directory_info()
start_time = datetime.now().time()
print(f"TroubleLog started at {start_time}")

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
                f"\nService Log {log_number} already exists for machine {machine} and was created on {created_timestamp} and was last updated on {last_updated_timestamp}. Please choose a different log number."
            )

        else:

            title = input("Title: ").strip()
            status = input("Status: ").strip()
            summary = input("Summary: ").strip()
            timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S")
            log_content = f"""# Service Log {log_number}

## Machine

{machine}

## Title

{title}

## Created
{created_timestamp}

## Status

{status}

## Summary

{summary}

## Last Updated
{last_updated_timestamp}

"""

            with open(file_path, "w", encoding="utf-8") as log_file:
                log_file.write(log_content)

            print(
                f"\nService Log {log_number} created successfully "
                f"for machine {machine} on {created_timestamp}."
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
                f"for machine {machine} on {created_timestamp} and was last updated on {last_updated_timestamp}."
            )

    # ======================================================
    # UPDATE SERVICE LOG
    # ======================================================

    elif choice == "3":

        machine = input("Enter Machine Name: ").strip().lower()
        log_number = input("Enter Service Log Number: ").strip()

        last_updated_timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S")

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

**Time Updated Last**
{last_updated_timestamp}

### Notes

{update_notes}

"""

            with open(file_path, "a", encoding="utf-8") as log_file:
                log_file.write(update_content)

            print(
                f"\nService Log {log_number} updated successfully "
                f"for machine {machine} on {last_updated_timestamp}."
            )

        else:

            print(
                f"\nService Log {log_number} was not found "
                f"for machine {machine} on {created_timestamp} and was last updated on {last_updated_timestamp}."
            )

    # ======================================================
    # EXIT
    # ======================================================

    elif choice == "4":

        print("\nClosing TroubleLog...")
        print(f"TroubleLog closed at {last_updated_timestamp}.")
        break

    # ======================================================
    # INVALID MENU CHOICE
    # ======================================================

    else:

        print(
            "\nInvalid menu selection. "
            "Please choose an option from 1-4."
        )