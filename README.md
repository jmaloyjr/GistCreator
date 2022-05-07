# GistCreator


Quick script used to create github gists locally.

#### Usage

```gist -f mygist.py```

#### Setup

1. The script uses a shebang to be accessed anywhere on the machine it is running on. There is some quick setup to ensure you can call the script anywhere. 
    - Ensure the first line references the local path of your Python executable i.e `which python` output.
    - To make this an executable file run `chmod +x createGist.py`
    - Add the files directory to your path and add an alias (optional).


    ```
    export PATH=$PATH:$HOME/exc/gist
    alias gist="createGist.py"
    ```

2. To create gists using githubs CLI you need to create a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#using-a-token-on-the-command-line)
    - Ensure the access token has these scopes and permissions `gist, read:org, repo`
    - run `brew install gh` to install the CLI
    - run `pip install python-decouple` and create an `.env` file to store the Access Token
    - Save the access token in the file. eg.

    ```
    GH_TOKEN="<YOUR_TOKEN"
    ```