# OFLUX, the terminal messenger
## Project Idea
**Project Name: Oflux**

So bascially i will be discussing all the routes, all the commands of ofux.py and all other information regarding this project in this markdown file. I am writing this before starting the project and I felt like unlike other project I have to start this project in some structured way, right. So i thought of making this readme file, So i did.

## Discussing the commands of oflux.py
First of all I was thinking, I should discuss all the commands of ofux the termial messenger so i can make appropreate routes.
- First it should be like user types ofux, it starts then using select command, one receiver to message is selected by the sender.
- Using list command, a list of all the receivers should be opened up with there reg numbers.
- Auth will be done using API key.
- For that there will be command, register
    ```
    register "username"
    Output: Status: Success
    Your api token: API_TOKEN_HERE
    You dont need to save your api token as it has been already saved at ./.auth
    ```
- For permanent deleting account : Permanetly-Delete-Account "username" "API-TOKEN" "link of auth file"
- Listen "Username" this command will open a websocket connection to listen all the incomming messages.
- It can be also like ofux select baltej "heyy brother"
- For sending a file, it will be like, ofux select baltej "file:file-link"
- Search user for searching the user by username or regnumber --username or --regnum 
- regnum for checking your own regnum
- all commands till now
```
select
list
register
Permanetly-Delete-Account
searchuser or su
regnum
```

## Discussing the routes
### select 
- ./send/yourapitoken/usernameToSendTo/message (or post message)
- ./receive/yourapitoken/
- ./register/username
- ./deleteAccount/yourapitoken/username
- ./searchUser/search-string/
- ./listReceivers/yourapitoken/

