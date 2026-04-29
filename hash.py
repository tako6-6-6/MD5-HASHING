import hashlib
import time

def find_hash():
    # The MD5 we're looking for
    target_hash = "898d97521782019d009268f7f4625695"
    
    # Path for Kali Linux (rockyou.txt location)
    wordlist_path = "/usr/share/wordlists/rockyou.txt" 
    
    print(f"[*] Target: {target_hash}")
    print(f"[*] Wordlist: {wordlist_path}")
    print("-" * 30)
    
    start_time = time.time()
    count = 0
    
    try:
        # Using 'rb' mode to handle large file bytes correctly
        with open(wordlist_path, 'rb') as file:
            for line in file:
                count += 1
                
                # Clean the word from newline and carriage return symbols
                password = line.decode('latin-1', errors='ignore').replace('\r', '').replace('\n', '').strip()
                
                # Create hash from current word
                guess_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
                
                # Compare current hash with our target
                if guess_hash == target_hash:
                    duration = time.time() - start_time
                    print("\nFOUND!")
                    print(f"Password: {password}")
                    print(f"Line number: {count}")
                    print(f"Time: {duration:.4f} seconds")
                    return

                # Check if we hit the word but hash is different (for debugging)
                if password == "tbilisi1":
                    print(f"\n[!] Found 'tbilisi1' but hash was: {guess_hash}")

                # Progress indicator
                if count % 1000000 == 0:
                    print(f"[*] Processed {count // 1000000}M lines...")

        print(f"\n[-] Password not found in {count} lines.")

    except Exception as e:
        print(f"[!] Error occurred: {e}")

if __name__ == "__main__":
    # Start the script and measure performance
    # This project was tested on Kali Linux with the rockyou wordlist.
    # The main challenge was handling hidden \r\n characters which changed the hash.
    find_hash()