# Envision-TicTacToe-Bot

Tic Tac Toe is one of the most played games. The game is played by two players, who take turns marking the spaces in a
three-by-three grid with ‘X’ (crosses) and ‘O’ (noughts). The player who succeeds in placing three of their marks consecutively in one column, row or diagonal is the winner. If both players play the best moves, the game ends in a draw.

This project aims to make two different types of bots to play this game. One of the types will be hardcoded. We will make agents that select their moves randomly, after considering moves to a depth of one, after considering moves to a depth of two and using the minimax algorithm. We will measure and compare success rates between these four agents, and a few games against a human.

The second type of bot will be a self-learning bot, which will learn how to optimize its playing style to make the best moves. We will not require to hard-code any instructions as to how to choose the next move. The model will play against another coded bot in order to learn what the best moves are, and improve itself.

<br>

## Contributing Guidelines

### Setting Up
- Fork the repo.
- Clone the forked repo using `git clone <repo-url>` to desired directory.

### Pull Requests
- For each new `submission`, `fix` or `feature` create a new branch named `<github-handle>-<explanatory-name>`.
    ```cmd
    git branch <branch-name>
    ```
- Switch to the new branch.
    ```cmd
    git checkout <branch-name>
    ```
- Make the changes in the new branch.
- Stage the changes for the next commit. To stage changes from specific files:
    ```cmd
    git add <filename>
    ```
    To stage all the changes at once:
    ```cmd
    git add .
    ```
    Use `git status` to track the changes made.
- Commit the changes.
    ```cmd
    git commit -m "<commit-message>"
    ```
- Push the changes to your forked repo. <br>
    If you're working on a new branch:
    ```cmd
    git push -u origin <branch-name>
    ```
    If the branch already exists:
    ```
    git push
    ```
- Create a `pull request`.

### Keep in Mind
- Use `meaningful small commits`. Refer to this [link](https://cbea.ms/git-commit/).
- `Remember to fetch` changes from the upstream repo before working on something.