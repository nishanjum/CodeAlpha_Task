import re

def extract_emails(input_file_path, output_file_path):
    # Standard regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        # Read content from the source file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Find all matching emails
        found_emails = re.findall(email_pattern, content)
        
        # Remove duplicate emails by converting the list to a set
        unique_emails = sorted(list(set(found_emails)))

        if unique_emails:
            # Write the extracted emails to the output file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for email in unique_emails:
                    output_file.write(email + '\n')
            print(f"Success! Extracted {len(unique_emails)} unique email(s) to '{output_file_path}'.")
        else:
            print("No email addresses were found in the source file.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found. Please create it first.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Execution ---
if __name__ == "__main__":
    INPUT_FILE = "contacts.txt"
    OUTPUT_FILE = "extracted_emails.txt"
    
    # Quick creation of a dummy file for demonstration purposes
    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        f.write("Hello, contact me at john.doe@example.com or support@company.org. Cheers!")

    extract_emails(INPUT_FILE, OUTPUT_FILE)