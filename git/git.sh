ssh-keygen -t rsa -b 2048 -C '' -P '' -f key
git init
git config user.name user
git config user.email userid+user@users.noreply.github.com
git add .
git remote add origin git@github.com:user/repo.git
git remote add origin https://github.com/user/repo.git
GIT_SSH_COMMAND='ssh -i key' git push -u origin master
curl -s https://api.github.com/users/user | jq .id
