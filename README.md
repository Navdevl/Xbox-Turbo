
# Xbox Turbo
Get the gamertag you want for Xbox

## Public vs Private:
The private version is as fast as you need.

 - If you wish to discuss details of the private version, feel free to
   message me on discord with the following hashtag.
    - #xboxtubo
   
 - My discord
    - nubonix#3648

## Requirements:
 - Download chromedriver via https://chromedriver.storage.googleapis.com/73.0.3683.20/chromedriver_win32.zip
   - unzip the chromedriver to your desired destination
   - edit main.py with your desired editor and set the destination path for chromedriver on line 28.
     -  Yes, you must include the **r** so that python knows its a real string.
     - An example path would look like:
       - r"C:/Users/Nubonix/python_programming/webdrivers/chrome/version73/chromedriver.exe"
 - Must have accessed https://account.xbox.com/ChangeGamerTag at least
   once (recently), with the email you wish to claim the gamertag with.
   - Must have an email that is associated with the email above so that it can be used for validation / verification INSTEAD of a phone number.
 - `pip install selenium`
## Usage

    python main.py --email="myusername@hotmail.com" --password="myhotmailpassword" --screen_name="the_gamer_tag_to_monitor_then_claim"

## Possible Future Updates

 - [ ] Phone verification
 - [ ] Automatic recognition of the verification code
