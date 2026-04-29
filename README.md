##                                               md5 hash cracker

მარტივი Python  სკრიპტი, რომელიც ახორციელებს Wordlist შეტევას `rockyou.txt` ბაზის გამოყენებით.
პროექტის მთავარი  მიზანი იყო რეალური მაგალითის  საშუალებით მენახა როგორ მუშაობს პაროლების გატეხვის პროცესი კიბერუსაფრთხოებაში.

###                      ამ პროექტის საშუალებით მე ვისწავლე:
 1.როგორ გარდაიქნმნება ჩვენი პაროლები ჰაშირების საშუალებით რიცხვებისა და ასოების უნიკალურ კომბინაციად.
 2.როგორ შეგვიძლია დიდ მონაცემთა ბაზებში ოპტიმირებულად ვეძებოთ მონაცემები.
 კოდი დავტესტე  kali linux-ის გარემოში, სადაც ვეცადე მომეძებნა პაროლები `rockyou.txt` ბაზაში.


###                 პროექტზე მუშაობისას გადავაწყდი რამდენიმე პრობლემას:
 1. თავდაპირველ ვერსიაში ვიყენებდი utf-8 სტანდარტს, რამაც სამწუხაროდ ვერ შეძლო ფაილიდან ინფორმაციის სწორად ამოკითხვა, რის გამოც მომიწია შემეცვალა იგი და გამომეყენებინა უფრო  'rb'(Read Binary) რეჟიმი latin-1 დეკოდირებით.
 2. ტერმინალშივე ვამოწმებდი სხვადასხვა პაროლების ჰეშებს, თუმცა ამის მიუხედავად მაინც შემექმნა პრობლემა, პირველ რიგში იმიტომ რომ ამ პაროლებს ჰქონდათ უხილავი დაბოლოებები (\n,\r), ეს პრობლემა გადავჭერი ხაზების ხელით გასუფთავების (manual stripping) ფუნქციის დამატებით.ჰაშირება არის ძალიან სპეციფიური, პატარა ცვლილებაც კი მთლიან ჰეშს ცვლის,რადგან დიდი შანსი იყო მართლწერაშ შეცდომა დაგვეშვა. მომიწია კოდში ახალი ლოგიკის დამატება, რომელიც გვატყობინებს თუ სკრიპტი იპოვის საჭირო პაროლს, მაგრამ განსხვავებული ჰეშით, რამაც საგრძნობლად გაამარტივა ძებნის პროცესი.


###                      გამოყენების წესები:
 1. Make sure you have a wordlist (default path is for Kali Linux: `/usr/share/wordlists/rockyou.txt`).
 2. Update the `target_hash` variable in `hash.py` with the hash you want to crack.
 3. Run the script:
   ```bash
   python3 hash.py

--------------------------------------------------------------------------------------------------------------------------------------
##                                                   English Version


## MD5 Hash Cracker

A simple Python script that performs a wordlist attack using rockyou.txt. The main goal of this project was to explore how password cracking works in real-world cybersecurity scenarios.

##           Through this project, I learned:

1. How passwords are transformed into unique alphanumeric strings through hashing.
2. How to efficiently process and search through massive datasets.

The script was tested in a Kali Linux environment using the standard rockyou.txt wordlist.

##           Challenges & Solutions:

1. Encoding Issues: My initial version used utf-8, which failed to read some parts of the wordlist correctly. I resolved this by switching to 'rb' (Read Binary) mode combined with latin-1 decoding for better stability.

2. Hidden Characters: Even when a hash seemed correct in the terminal, the script sometimes failed to find a match. I discovered that hidden line endings (\n, \r) were altering the MD5 results. I fixed this by implementing a manual stripping function to clean each line before hashing.

3. Diagnostic Logic: Hashing is extremely sensitive—even a tiny change in spelling or a single space changes the entire hash. To make debugging easier, I added logic that alerts me if the script finds the correct password but with a different hash. This helped significantly in identifying formatting errors.

##           Usage:
Make sure you have a wordlist (Default path: /usr/share/wordlists/rockyou.txt).

Update the target_hash variable in hash.py with the hash you want to crack.

Run the script:

Bash
python3 hash.py

