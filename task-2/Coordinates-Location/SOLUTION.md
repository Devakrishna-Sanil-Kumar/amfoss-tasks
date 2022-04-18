1. First, you need to create a directory and name it `Coordinates-Location` and go into that directory.

   mkdir Coordinates-Location

   cd Coordinates-Location

2. Now create a Directory called North and go into it, and implement the following step by step.

   mkdir North

   cd North

   - i. Create a file called NDegree.txt and answer the following question.

     - **a.** Find the discriminant of 2x^2-5x+2=0?

     - **b.** Add a degree(°) symbol to ***(a)*** (**Eg:** x°).

     - **c.** Now store the value of ***(b)*** in `NDegree.txt`.

       touch NDegree.txt
       echo "9°" > NDegree.txt

   - ii. Create a file called NMinutes.txt and answer the following questions.

     - **a.** What is the only prime number to end with the digit 5?

     - **b.** Add single quote(‘) to ***(a)*** (**Eg:** y’).

     - **c.** Now store the value of ***(b)*** in `NMinutes.txt`.

       touch NMinutes.txt         
       echo "5'" >  NMinutes.txt

   - iii. Create a file called NSeconds.txt and answer the following questions.

     - **a.** what is the largest even number that can not be written as the sum of two odd composite numbers?

     - **b.** Add “0.1” value to the value of ***(a)***.

     - **c.** Add Double quote(“) to ***(b)*** (**Eg:** Z’’).

     - **d.** Now store the value of ***(c)*** in `NSeconds.txt`.

       touch NSeconds.txt       
       echo "38.01\"" >  NSeconds.txt

   - **iv.** Make a file `NorthCoordinate.txt` formed from the combination of the files you had created in the above steps-***(i)***,***(ii)***,***(iii)***.

     touch NorthCoordinate.txt
     cat NDegree.txt NMinutes.txt NSeconds.txt > NorthCoordinate.txt

   - **v.** Copy the `NorthCoordinate.txt` to the `Coordinate-Location` directory and rename it as `North.txt` and delete the file created in step-***(iv)***.

     cp NorthCoordinate.txt ..

     cd ..

     mv NorthCoordinate.txt North.txt

     cd North

     rm -rf NorthCoordinate.txt

3. Keep going you have just completed finding half of the Location Coordinate![raised_hands](https://github.githubassets.com/images/icons/emoji/unicode/1f64c.png), now it's time to find the remaining half![grinning](https://github.githubassets.com/images/icons/emoji/unicode/1f600.png). Now again go to the `Coordinates-Location` directory.

   cd ..

4. Create a Directory called East go into it, and again implement the following step by step.

   mkdir East                      
   cd East 

   - i. Create a file called EDegree.txt and answer the following question.

     - **a.** what is the atomic number of Osmium?

     - **b.** Add a degree(°) symbol to ***(a)*** (**Eg:** x°).

     - **c.** Now store the value of ***(b)*** in `EDegree.txt`.

       touch EDegree.txt 
       echo "76°" > EDegree.txt

   - ii. Create a file called EMinutes.txt and answer the following question.

     - **a.** what is the highest score in a hand of cribbage game?

     - **b.** Add single quote(‘) to ***(a)*** (**Eg:** y’).

     - **c.** Now store the value of **(b)** in `EMinutes.txt`.

       touch EMinutes.txt
       echo "29'" > EMinutes.txt 

   - iii. Create a file called ESeconds.txt and answer the following question.

     - **a.** What is the minimum age for united states senators?

     - **b.** Add “0.8” value to the value of ***(a)***.

     - **c.** Add Double quote(“) to ***(b)*** (**Eg:** Z’’).

     - **d.** Now store the value of ***(c)*** in `ESeconds.txt`.

       touch ESeconds.txt

       echo "30.8\"" > ESeconds.txt

   - **iv.** Make a file called `EastCoordinate.txt` formed from the combination of files you created in the above steps-***(i)***,***(ii)***,***(iii)***

     touch EastCoordinate.txt
     cat EDegree.txt EMinutes.txt ESeconds.txt > EastCoordinate.txt

   - **v.** Copy the `EastCoordinate.txt` to the `Coordinate-Location` directory and rename it as `East.txt` and delete the file created in step-***(iv)***.

     cp EastCoordinate.txt ..                                      
     ➜rm -rf EastCoordinate.txt 
     cd ..                   
     mv EastCoordinate.txt East.txt

5. Make a file called `Location-Coordinate.txt` formed from the combination of `North.txt` and `East.txt` files in the `Coordinate-Location` directory.

   touch Location-Coordinate.txt
   cat North.txt East.txt > Location-Coordinate.txt
   
   

![](/home/devakrishna/Coordinates-Location/Screenshot from 2022-04-16 15-53-27.png)

