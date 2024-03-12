# How To Work With Multiple Github Accounts on a single Machine

Let suppose I have two github accounts, **<https://github.com/maple-office>** and **<https://github.com>/maple-personal**. Now i want to setup my mac to easily talk to both the github accounts.

> NOTE: This logic can be extended to more than two accounts also.

The setup can be done in 5 easy steps:

## Reference

[how-to-work-with-multiple-github-accounts](https://dev.to/terieyenike/how-to-work-with-multiple-github-accounts-3eh9)

## Steps

- [Step 1](#step-1) : Create SSH keys for all accounts
- [Step 2](#step-2) : Add SSH keys to SSH Agent
- [Step 3](#step-3) : Add SSH public key to the Github
- [Step 4](#step-4) : Create a Config File and Make Host Entries
- [Step 5](#step-5) : Cloning GitHub repositories using different accounts

## Step 1

### Create SSH keys for all accounts

First make sure your current directory is your **.ssh** folder.

```sh
     cd ~/.ssh
```

Syntax for generating unique ssh key for ann account is:

```sh
     ssh-keygen -t rsa -C "your-email-address" -f "github-username"
```

here,

**-C** stands for comment to help identify your ssh key

**-f** stands for the file name where your ssh key get saved

#### Now generating SSH keys for my two accounts

```sh
     ssh-keygen -t rsa -C "my_office_email@gmail.com" -f "github-maple-office"
     ssh-keygen -t rsa -C "my_personal_email@gmail.com" -f "github-maple-personal"
```

Notice here **maple-office** and **maple-work** are the username of my github accounts corresponding to **<my_office_email@gmail.com>** and **<my_personal_email@gmail.com>** email ids respectively.

After entering the command the terminal will ask for passphrase, leave it empty and proceed.

> Now after adding keys , in your .ssh folder, a public key and a private will get generated.
> The public key will have an extention **.pub** and private key will be there without any extention both having same name which you have passed after **-f** option in the above command. (in my case **github-maple-office** and **github-rahu-personal**)

## Step 2

### Start SSH agent

In Windows PowerShell (run as admin):

```sh
# Check the current status of ssh-agent:
Get-Service | ?{$_.Name -like '*ssh-agent*'} | select -Property Name, StartType, Status

# Enable the Service if it is disabled:
Set-Service -Name ssh-agent -StartupType Manual

# Start the Service:
Start-Service ssh-agent

# Add your key as before:
ssh-add <path to the key>
```

### Add SSH keys to SSH Agent

Now we have the keys but it cannot be used until we add them to the SSH Agent.

```sh
     ssh-add -K ~/.ssh/github-maple-office
     ssh-add -K ~/.ssh/github-maple-personal
```

You can read more about adding keys to SSH Agent [here.](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Step 3

### Add SSH public key to the Github

For the next step we need to add our public key (that we have generated in our previous step) and add it to corresponding github accounts.

For doing this we need to:

1. Copy the public key

    We can copy the public key either by opening the github-maple-office.pub file in vim and then copying the content of it.

    ```sh
        vim ~/.ssh/github-maple-office.pub
        vim ~/.ssh/github-maple-personal.pub
    ```

    OR

    We can directly copy the content of the public key file in the clipboard.

    ```sh
        pbcopy < ~/.ssh/github-maple-office.pub
        pbcopy < ~/.ssh/github-maple-personal.pub
    ```

2. Paste the public key on Github

   - Sign in to Github Account
   - Goto **Settings** > **SSH and GPG keys** > **New SSH Key**
   - Paste your copied public key and give it a Title of your choice.

   _**OR**_

   - Sign in to Github
   - Paste this link in your browser (<https://github.com/settings/keys>) or click [here](https://github.com/settings/keys)
   - Click on **New SSH Key** and paste your copied key.

## Step 4

### Create a Config File and Make Host Entries

The **~/.ssh/config** file allows us specify many config options for SSH.

If **config** file not already exists then create one (make sure you are in **~/.ssh** directory)

```sh
     touch config
```

The commands below opens config in your default editor....Likely TextEdit, VS Code.

```sh
     open config
```

Now we need to add these lines to the file, each block corresponding to each account we created earlier.

```config
     #maple-office account
     Host github.com-maple-office
          HostName github.com
          User git
          IdentityFile ~/.ssh/github-maple-office

     #maple-personal account
     Host github.com-maple-personal
          HostName github.com
          User git
          IdentityFile ~/.ssh/github-maple-personal
```

## Step 5

### Cloning GitHub repositories using different accounts

So we are done with our setups and now its time to see it in action. We will clone a repository using one of the account we have added.

Make a new project folder where you want to clone your repository and go to that directory from your terminal.

For Example:
I am making a repository on my personal github account and naming it **TestRepo**
Now for cloning the repo use the below command:

 ```git
     git clone git@github.com-{your-username}:{owner-user-name}/{the-repo-name}.git

     [e.g.] git clone git@github.com-maple-personal:maple-personal/TestRepo.git
 ```

## Finally

From now on, to ensure that our commits and pushes from each repository on the system uses the correct GitHub user — we will have to configure **user.email** and **user.name** in every repository freshly cloned or existing before.

To do this use the following commands.

```git
     git config user.email "my_office_email@gmail.com"
     git config user.name "maple Pandey"
     
     git config user.email "my-personal-email@gmail.com"
     git config user.name "maple Pandey"
```

Pick the correct pair for your repository accordingly.

To push or pull to the correct account we need to add the remote origin to the project

```git
     git remote add origin git@github.com-maple-personal:maple-personal
     
     git remote add origin git@github.com-maple-office:maple-office
```

Now you can use:

```git
     git push
     
     git pull
```
