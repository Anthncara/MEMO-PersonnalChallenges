# https://youtu.be/RynYYIrFlJ8  complementary video from LMS

# Pipes '|' send the output of one command as input of another command.

tac                                  # output text reverse order

# sort                               # The sort filter will default to an alphabetical sort.
sort sample.txt
sort sample.txt > sorted-sample.txt
sort -r	                             # the flag returns the results in reverse order
sort -f	                             # the flag does case insensitive sorting
sort -n	                             # the flag returns the results as per numerical order

# uniq                               # With uniq you can remove duplicates from a sorted list.

sort sample.txt 
sort sample.txt | uniq                 # uniq sorted-sample.txt the same
uniq -d sample.txt

# grep 
grep unique sample.txt

grep -A 3 Monday sample.txt          # Shows after linez of specific command
grep -B 3 Monday sample.txt
grep -c unique sample.txt            #Counts letters  unique
grep -w unique sample.txt            #Only word unique
grep -wc unique sample.txt           #Counts words  unique
grep -v unique sample.txt            # except of unique
grep -cv unique sample.txt           # how many lines does not contain unique letters
grep -wcv unique sample.txt          # how many lines does not contain unique words
grep a sample.txt                   # just a letter

#wc                                   # counting words, lines and char is easy with wc command

wc -l tennis.txt                     # count lines in tennis.txt

wc -w tennis.txt                     # count words in tennis.txt

wc -c tennis.txt                     # count bytes in tennis.txt
wc -m tennis.txt                     # count bytes in tennis.txt

|                                    # we can write another command on first output

;                                   # bir satırda birden çok komut çalıştırmaya yarar. cat days.txt ; cat sample.txt
sleep 5                             # shell 5 sn bekler 
sleep 5 & cat sample.txt

$? --- sıfırdan farklı bir değer gelirse anlamalıyız ki son girdiğimiz komut hatalıdır.
echo $?


&& --- Logical AND olarak kullanılır. İki komutu && ile ayırırsak ilk komut çalıştıysa ikinci çalışır aksi halde çalışmaz.
cat file1.txt && cat file2.txt --- file1 eğer varsa ikinci komuta geçer aksi halde ikinci komut çalışmaz.

|| --- Logical AND olarak kullanılır. Eğer ilk komut çalışmazsa ikinciyi çalıştır. çalışırsa sadece birinci çalışır.
echo first || echo second ; echo third ---- fist ve third çıktısı verir.
zecho first || echo second ; echo third ----second ve third çıktısı verir.
rm file11 && echo it worked || echo it failed

\ --- escape sequence karakteridir. ayrıca bu karakter ile komutları satırlara ayırabiliriz.



tee                                  # we can copy first output with tee command to anouther file

cut                                  # The cut filter can select columns from files, depending on a delimiter or a count of bytes

cut -d: -f1-3 /etc/passwd | tail -3  # d means delimiter 
                                     # f means field

tr                                   # It is used for translating and deleting characters.

cat clarusway.txt | tr -d e          # delete all "e" char in the text

cat clarusway.txt | tr [a-z] [A-Z]   # change all lower char to upper char

cat clarusway.txt | tr [A-Z] [a-z]   # change all upper char to lower char






# comm                               # Comparing streams (or files) can be done with the comm. By default, comm will output three columns.

comm list1.txt list2.txt             # col 1 lines unique to list1, col2 lines unique to list2, col3 lines that appear in both files

# https://youtu.be/RynYYIrFlJ8 complementary video about filters
