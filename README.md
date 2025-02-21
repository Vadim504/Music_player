## `git init` - 
## `git add .` - добавить изменения
## `git commit -am '+ something'` -  закомитить изменения
## `git push origin main` - отправить все изменения в main

## Создать в папке с ключом ssh файл config.txt загрузить код
Host github.com
    IdentityFile "Путь к файлу с ключом"
    User git

## `ssh -T git@github.com` - проверка подключения к git
## `Start-Service ssh-agent` - запуск ssh агента
## `ssh-add -l` - проверка наличия ключа в ssh агенте
## `echo ".ssh/" >> .gitignore` - добавить файл ssh в gitignore

