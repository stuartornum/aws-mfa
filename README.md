# aws-mfa
Get temporary AWS credential from a choice of multiple AWS accounts

# Setup
### Prerequisites 

You already have a `~/.aws/credentials` and `~/.aws/config file setup

Good example: https://boto3.amazonaws.com/v1/documentation/api/1.9.46/guide/configuration.html#assume-role-provider

### Commands
```bash
mkdir ~/.bin/
# Git clone this repo somewhere and "cd" into it
cp aws-mfa.sh ~/.bin/
cp aws-session-manager.py ~/.bin/
```

Edit your `~/.bash_profile` or `~/.zshrc` to include the `~/.bin` directory in your path, or just do the following:
 
```bash
# For bash

echo "export PATH=\"~/.bin:$PATH\"" >> ~/.bash_profile
echo "alias getaws='source aws-mfa.sh'" >> ~/.bash_profile
```
```bash
# For zsh

echo "export PATH=\"~/.bin:$PATH\"" >> ~/.zshrc
echo "alias getaws='source ~/.bin/aws-mfa.sh'" >> ~/.zshrc
```

# Run

You'll either need to open a new terminal or source the bash/zsh profile

```bash

getaws
```

The output will look something like below

```
############ Choose a profile ###########

0 - default
1 - dev
2 - staging
3 - preprod
4 - prod
5 - billing
Profile Number: 1
Enter MFA code for arn:aws:iam::000000000000:mfa/billybob:
## Credentials set! ##
```