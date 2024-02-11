## CyberChallenge.IT 2022 - Programming test

Date: 11/02/2024

Difficulty: Easy

Status: Solved

# Password Protection Officer (ppo)

For us at CC (Coste Challenge), password protection is very important, for this reason we want you as
our new PPO (Password Protection Officer).

The password policy for our website is very hard to verify, in particular, when a user is changing it, the
new password should follow all these requirements:

1. The new password must be at least 8 characters long.
2. The new password must be at most 16 characters long.
3. The new password must contains both lowercase and uppercase letters.
4. The new password must contains at least one digit and one special character.
5. The new password must not contain two consecutive identical characters.
6. The new password must not be derivable by deleting, substituting or adding exactly one character
    from the old password.

Write a program that, given a list of pairs of new and old passwords, returns if the new passwords follows
all the requirements.

## Input data

The first line of the input contains the integer **N** , the number of password checks to perform.

The following **N** lines contains two space-separated strings each, the new password and the old password
respectively.

## Output data

The output must contains _N_ lines, one for each password checking. Each line should contains 1 if the
new password is valid, 0 otherwise.

## Scoring

For each of the subtasks, the following constraints are met:

- Subtask 1 (30 points): If the password is not valid, it violates one of the requirements from 1 to 3.
- Subtask 2 (30 points): If the password is not valid, it violates one of the requirements from 1 to 5.
- Subtask 3 (40 points): If the password is not valid, it violates one of the requirements from 1 to 6.


## Examples

```
input output
```
```
9
short abcdEFGH1234 !*-?
veryverylongpassw abcdEFGH1234 !*-?
ALLUPPER abcdEFGH1234 !*-?
UpperLower abcdEFGH1234 !*-?
P4ssword! abcdEFGH1234 !*-?
bcdEFGH1234 !*-? abcdEFGH1234 !*-?
xabcdEFGH1234 !*-? abcdEFGH1234 !*-?
xbcdEFGH1234 !*-? abcdEFGH1234 !*-?
?3 CuR3P4s?w0rd abcdEFGH1234 !*-?
```
```
0 
0 
0 
0 
0 
0 
0 
0
1
```

## Explanation

- In the test case number 1 the new password violates the requirement number 1.
- In the test case number 2 the new password violates the requirement number 2.
- In the test case number 3 the new password violates the requirement number 3.
- In the test case number 4 the new password violates the requirement number 4.
- In the test case number 5 the new password violates the requirement number 5.
- In the test case number 6 the new password violates the requirement number 6, as the password is
    obtained by deleting one character from the old password.
- In the test case number 7 the new password violates the requirement number 6, as the password is
    obtained by substituting one character from the old password.
- In the test case number 8 the new password violates the requirement number 6, as the password is
    obtained by adding one character from the old password.
- In the test case number 9 the new password follows all the given requirements.


