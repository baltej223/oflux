## Note: Its under construction right now.
## Contributions will be appreciated.
---

# **Messaging Application (oflux)**

This project allows you to send and receive messages through text files. You can interact with other users by editing `.txt` files, and messages are sent and received in real-time.

## A Quick sneak peek
![JOHN](https://raw.githubusercontent.com/baltej223/oflux/refs/heads/examples/2.png)
![MARIE](https://raw.githubusercontent.com/baltej223/oflux/refs/heads/examples/1.png)

### **Key Features**:
- **Real-time messaging** via WebSockets (no polling needed).
- **Automatic message sending** after saving a file.
- **Simple text file-based interface** for chatting.
- **Registration system** to create users and link them with unique IDs.

---

## **Requirements**

Before you can run the project, you need to install Python and some libraries. Here are the steps:

### 1. **Install Python**
   - You can download and install Python from [here](https://www.python.org/downloads/).
   - After installation, verify that Python is installed by running this command in the terminal or command prompt:
     ```bash
     python --version
     ```

### 2. **Install Required Python Libraries**
   This project uses some additional Python libraries. To install them, run this command in the terminal:
   
   ```bash
   pip install websocket-client requests
   ```

---

## **Setting Up the Project**

### 1. **Clone the Repository**

First, you need to clone this project to your computer. If you don't have Git installed, you can manually download the project as a ZIP file.

To clone the repository, use this command in the terminal:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the URL of the project if it's hosted on a Git platform (like GitHub).

---

## **How to Register a New User**

1. **Run `register.py`**: This will register a new user and generate a unique ID (UID).

   - Open the terminal and navigate to the `scripts` folder inside your project directory.
   - Run the command:
     ```bash
     python scripts/register.py <your-username>
     ```
     Replace `<your-username>` with your desired username. For example:
     ```bash
     python scripts/register.py john
     ```

   - After successful registration, your UID will be saved to a file (`auth/.my_uid`), and a mapping between your username and UID will be stored in `scripts/uid_map.json`.

---

## **How to Chat**

### 1. **Start a Conversation**

Once you're registered, create a new `.txt` file for your chat. The filename should be the username of the person you're chatting with. For example, if you're chatting with someone named John, create a file named `john.txt` in the root folder of the project.

You can create the file manually or use any text editor. 

### 2. **Send a Message**

- Open the `.txt` file you created (e.g., `john.txt`) in any text editor (or use Neovim for an advanced editor).
- Add your message at the bottom of the file. It will look like this:
  ```
  John: Hey there!
  You: Hey! What's up?
  ```
- **Save the file**. Once saved, your message will automatically be sent to the recipient.

### 3. **Receive Messages**

You’ll automatically receive messages from others in your `.txt` chat file as well. The `autoreceivemessage.py` script will listen for new messages through a WebSocket and add them to the file.

---

## **Running the Application**

There are two main Python scripts that handle message sending and receiving:

### **1. Sending Messages: `autosendmessage.py`**

After you’ve written a message in the `.txt` file, it’s automatically sent to the server when you save the file. To enable this:

1. Open your `.txt` file (e.g., `john.txt`) in Neovim.
2. **Save the file** using `:w`.
3. The message is sent, and the file is updated.

### **2. Receiving Messages: `autoreceivemessage.py`**

To receive new messages:

1. **Run this script** in the terminal:
   ```bash
   python scripts/autoreceivemessage.py <your-chat-file>.txt
   ```
   Replace `<your-chat-file>.txt` with the name of the file you want to receive messages for (e.g., `john.txt`).

2. This script will automatically listen for messages and append them to your file.

---

## **Neovim Integration (Optional)**

For a more seamless experience, you can configure Neovim to automatically send and receive messages when you save or open a chat file.

In your `init.vim` or `init.lua` file (Neovim configuration), add the following lines to automate message sending and receiving.

**In `init.vim`**:

```vim
autocmd BufWritePost *.txt silent! !python3 scripts/autosendmessage.py %
autocmd BufRead *.txt silent! !python3 scripts/autoreceivemessage.py %
```

**In `init.lua`**:

```lua
vim.api.nvim_create_autocmd("BufWritePost", {
  pattern = "*.txt",
  command = "silent! !python3 scripts/autosendmessage.py %",
})

vim.api.nvim_create_autocmd("BufRead", {
  pattern = "*.txt",
  command = "silent! !python3 scripts/autoreceivemessage.py %",
})
```

---

## **Troubleshooting**

- **No messages are being sent**: Ensure that you have run `register.py` to create your user and that the `UID` is properly saved.
- **File not found errors**: Make sure the `.txt` file exists and you are passing the correct filename when running the scripts.
- **WebSocket connection issues**: Ensure your backend WebSocket server is running and is accessible at the correct URL (`wss://your-backend.com/ws`).

---

## **Contributing**

Feel free to contribute to this project! If you find a bug or want to add a feature, open an issue or submit a pull request.

---

## **License**

This project is open source and available under the [MIT License](LICENSE).

---


# So now how to use it with nvim??

Absolutely! You can configure Neovim so that your custom message automation (like running `autosendmessage.py` and `autoreceivemessage.py`) only runs when you're inside the `oflux` project folder.

Here's how you can do it cleanly:

---

## ✅ **Recommended Approach: Use `ftplugin` or project-specific config**

### **Step-by-step for folder-specific automation**

### 📁 Your folder structure:

```
~/
├─ oflux/
│  ├─ scripts/
│  ├─ john.txt
│  └─ etc...
```

### 🔧 Method 1: Use `.nvim.lua` or `.nvimrc` in the project folder (cleanest)

Neovim now supports local config files safely using `:set exrc` and `:set secure`.

#### ✅ 1. Enable local config support in your global `init.lua` or `init.vim`:

```lua
-- init.lua
vim.o.exrc = true
vim.o.secure = true
```

#### ✅ 2. Create a `.nvim.lua` file inside your `oflux/` directory:

```lua
-- oflux/.nvim.lua

-- Only run these autocommands in the oflux directory
local function ends_with(str, ending)
  return str:sub(-#ending) == ending
end

local file = vim.fn.expand("%:p")

-- Only apply to .txt files
if ends_with(file, ".txt") then
  vim.api.nvim_create_autocmd("BufWritePost", {
    pattern = "*.txt",
    command = "silent! !python3 scripts/autosendmessage.py %",
  })

  vim.api.nvim_create_autocmd("BufRead", {
    pattern = "*.txt",
    command = "silent! !python3 scripts/autoreceivemessage.py %",
  })
end
```

#### 🔐 Neovim will ask:
> “Do you want to allow running local config file `.nvim.lua`?”

Type `y` (just once per folder, it's safe since you wrote it).

---

### ✅ Alternate: Detect project folder in your global `init.lua`

If you don’t want to use `.nvim.lua`, add this to your `init.lua` instead:

```lua
-- init.lua

-- Autocommands only in 'oflux' folder
vim.api.nvim_create_autocmd({"BufWritePost", "BufRead"}, {
  pattern = "*.txt",
  callback = function(args)
    local cwd = vim.fn.getcwd()
    if cwd:match("oflux$") then
      if args.event == "BufWritePost" then
        vim.cmd("silent! !python3 scripts/autosendmessage.py " .. args.file)
      elseif args.event == "BufRead" then
        vim.cmd("silent! !python3 scripts/autoreceivemessage.py " .. args.file)
      end
    end
  end
})
```

---

## ⚠️ Note

- Make sure you're **opening Neovim from inside the `oflux/` folder**, e.g.:
  ```bash
  cd ~/oflux
  nvim john.txt
  ```

---

