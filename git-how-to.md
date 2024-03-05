SSH-key make and add it to your account
I use Linux where you can do it so easily.
You should to open a terminal, print

$ ssh-keygen -t ed25519 -C "your email"

$ shh-add

then print

$ cat ~/.ssh/id_ed25519.pub

and copy. Open github, sign in, go to settings and chose SHH and GPG-keys. After that click on "add new SHH" or smth like that. Parse your public-key andclick Add shh-key.
If you have another OS you can just join this site https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account.


How to clone a repository.

open terminal, chose a folder you want to save repository and print

$ git clone git@github.com:username/repository name.git

$ git init

for more info use your browser please.
