# Imposter

Imposter is a tool to generate fake git commit history with customizable profiles. It allows you to create a realistic-looking commit history for various types of developers, such as weekend warriors, workday committers, and more.

## Prerequisites

- Python 3.12 or higher
- Poetry (for dependency management)
- Git

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/imposter.git
   cd imposter
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

You can run Imposter using Poetry:

```
poetry run imposter --repo-path /path/to/your/repo --days 30 --profile workday-andy
```

### Options:

- `--repo-path`: Path to the git repository (required)
- `--days`: Number of days to generate history for (default: 30)
- `--profile`: Commit profile to use (default: workday-andy)

Available profiles:
- weekend-warrior
- workday-andy
- grind-dont-stop
- does-not-sleep
- early-bird
- lunch-break-learner
- weekend-procrastinator

## Examples

1. Generate 60 days of commit history for a weekend warrior:
   ```
   poetry run imposter --repo-path /path/to/your/repo --days 60 --profile weekend-warrior
   ```

2. Create a month of workday commits:
   ```
   poetry run imposter --repo-path /path/to/your/repo --days 30 --profile workday-andy
   ```

3. Simulate a developer who doesn't sleep for a week:
   ```
   poetry run imposter --repo-path /path/to/your/repo --days 7 --profile does-not-sleep
   ```

## Disclaimer

This tool was made for fun, and is for educational and testing purposes only. Do not use it to misrepresent your actual work or contributions.
