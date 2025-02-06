# Contributing to Poker Bot Arena

Thank you for considering contributing to Poker Bot Arena! We welcome contributions from everyone. By participating in this project, you agree to abide by our code of conduct.

## How to Contribute

### Fork the Repository

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/your-username/poker-bot-arena.git
   cd poker-bot-arena
   ```

### Fork the Submodule Repositories

1. Fork the submodule repositories on GitHub:
   - [poker-api](https://github.com/avikalpg/poker-api)
   - [poker-ui](https://github.com/avikalpg/poker-ui)
2. Update the submodules in your forked parent repository to point to your forks of the submodules:
   ```bash
   cd poker-bot-arena
   git submodule set-url interfaces/poker-api https://github.com/your-username/poker-api.git
   git submodule set-url interfaces/poker-ui https://github.com/your-username/poker-ui.git
   git submodule update --init --recursive
   ```

### Create a Branch

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b my-feature-branch
   ```

### Make Changes

1. Make your changes in the new branch.
2. If your changes affect the submodules, make sure to create a branch and update the submodules as well:
   ```bash
   cd interfaces/poker-api
   git checkout -b my-feature-branch
   # Make changes in poker-api
   git add .
   git commit -m "Description of changes in poker-api"
   git push origin my-feature-branch

   cd ../poker-ui
   git checkout -b my-feature-branch
   # Make changes in poker-ui
   git add .
   git commit -m "Description of changes in poker-ui"
   git push origin my-feature-branch
   ```

### Commit and Push

1. Commit your changes and push them to your forked repository:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin my-feature-branch
   ```

### Create a Pull Request

1. Go to the original repository on GitHub and create a pull request from your forked repository.
2. If your changes affect the submodules, also create pull requests for the submodules and update the submodules in the parent repository.

### Update Submodules in Parent Repository

1. If changes were made in the submodules, update the submodules in the parent repository:
   ```bash
   git submodule update --remote
   git add .
   git commit -m "Update submodules"
   git push origin my-feature-branch
   ```

2. Create a pull request in the parent repository to update the submodules.

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the expectations for contributing to this project.

Thank you for your contributions!
