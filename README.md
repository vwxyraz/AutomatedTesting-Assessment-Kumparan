# Kumparan - QA Intern Assessment : Automation Testing

**Author :** Vyra Fania Adelina

## Introduction
This project helps verifies the functionality of a feature from the website (https://kumparan.com/) for the user to see news article, 
post a comment on an article, register a new account and login to an existing account. This project performed by an automated testing using Python Selenium.
The functionality of a feature identifies as the test case, which obtained by analyzing the requirement of the system for the above.

### Test Case
The following is the test cases used to testing :

| Test Case ID | Test Case | Expected Output | Script |
| --- | --- | --- | --- |
TC-001 |	Check user can read the news |	The system could display the selected news with no errors | [`check-news-pages.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-news/check-news-pages.py) |
TC-002 |	Check user can like the news |	The color of the button will change | [`check-like-news.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-news/check-like-news.py) |
TC-003 |	Check user can share the news |	The system will show a pop up for more and show a window to facebook/twitter/line/whatsapp | [`check-share-news.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-news/check-share-news.py) |
TC-004 |	Check user can copy URL	| The system will show a notice that the URL copied successfully | [`check-share-news.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-news/check-share-news.py) |
TC-005 |	Check user can report the news	| The system will direct user to the report page | [`check-report-news.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-news/check-report-news.py) |
TC-006 |	Check user can see the comments	| The system will direct user to the comment section | [`check-news-comment.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-news/check-news-comment.py) |
TC-007 |	Check user can see images |	The system will show a pop up of the image | |
TC-008 |	Check user can see related posts through the topic	| The system will direct user to a topic page with list news articles or The system will direct user to a topic page with list news articles | |
TC-009 |	Check user can see Tim Editor |	The system will show the writer, reporter, and editor of the article | |
TC-010 |	Check user can see the publisher account	| The system will direct user to the account page | |
TC-011 |	Check user can write a comment with sign in |	The system will show the user's comment on the section | |
TC-012 |	Check user can write a comment without sign in |	The system will direct user to the login page | |
TC-013 |	Check user register with valid email |	The system will direct user to the email verification page | [`check-register-email.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-register-func/check-register-email.py) |
TC-014 |	Check user register with invalid email |	The system will show notice the email id is invalid | [`check-register-email.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-register-func/check-register-email.py) |
TC-015 |	Check user register with valid password	| The system will direct user to the homepage with an account signed in | [`check-create-pass.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-register-func/check-create-pass.py) |
TC-016 |	Check user register with invalid password	| The system will show notice the password is invalid (less than 8 character, not a combination of lowercase, uppercase, and number) | [`check-create-pass.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-register-func/check-create-pass.py) |
TC-017 |	Check user register with invalid Ulangi Password	| The system will show notice Ulangi Password is not the same as Password | [`check-create-pass.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-register-func/check-create-pass.py) |
TC-018 |	Check user can see the password	| The system will show the password | [`check-see-pass.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-see-pass.py) |
TC-019 |	Check user login with valid email id and password	| The system will direct user to the homepage with an account signed in | [`check-login-email.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-email.py) |
TC-020 |	Check user login with valid email id and invalid password	| The system will show notice the email or password is wrong | [`check-login-email.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-email.py) |
TC-021 |	Check user login with invalid email id and valid password	| The system will show notice the email or password is wrong | [`check-login-email.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-email.py) |
TC-022 |	Check user login with invalid email id and invalid password	| The system will show notice the email or password is wrong | [`check-login-email.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-email.py) |
TC-023 |	Check user login when forgot password	| The system will direct user to Lupa Password page | [`check-forgot-pass.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-forgot-pass.py) |
TC-024 |	Check user register/login with Facebook	| The system will show a window for Facebook sign in | [`check-login-fb.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-fb.py) |
TC-025 |	Check user register/login with Google	| The system will how a window for Google Account sign in | [`check-login-google.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-google.py) |
TC-026 |	Check user register/login with phone number	| The system will direct user to the verification page | [`check-login-phone.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-phone.py) |
TC-027 |	Check user register/login with the correct Kode OTP	| The system will direct user to the homepage with an account signed in | |
TC-028 |	Check user register/login with the false Kode OTP	| The system will show notice that Kode OTP is false | [`check-login-phone.py`](https://github.com/vwxyraz/AutomatedTesting-Assessment-Kumparan/blob/main/check-login-func/check-login-phone.py) |

The blank spot in script means it needs to be test manually. But if you have any solution don't hesitate to reach me

### Documentation and Reports
If you want to see more documentation about this project feel free to check out this link [Documentation and Reports](https://drive.google.com/drive/folders/1UYw83j5st-7GIBMpnsWYHwzd03Jc9Hzd?usp=sharing)


#### Disclaimer
This project is not in active development
