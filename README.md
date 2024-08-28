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
poetry run imposter --repo-path /path/to/your/repo --start-date 2023-01-01 --end-date 2023-12-31 --profile workday-andy
```

### Options:

- `--repo-path`: Path to the git repository (required)
- `--start-date`: Start date for generating history (format: YYYY-MM-DD) (required)
- `--end-date`: End date for generating history (format: YYYY-MM-DD) (required)
- `--profile`: Commit profile to use (default: workday-andy)

Available profiles:
- weekend-warrior
- workday-andy
- early-bird
- lunch-break-learner
- night-owl
- sporadic

## Examples

1. Generate commit history for a weekend warrior from March 1, 2023 to June 30, 2023:
   ```
   poetry run imposter --repo-path /path/to/your/repo --start-date 2023-03-01 --end-date 2023-06-30 --profile weekend-warrior
   ```

2. Create a year of workday commits for 2023:
   ```
   poetry run imposter --repo-path /path/to/your/repo --start-date 2023-01-01 --end-date 2023-12-31 --profile workday-andy
   ```

## Using the Justfile

If you have `just` installed, you can use the provided Justfile for common tasks:

1. Install dependencies:
   ```
   just install
   ```

2. Run Imposter with default settings (workday-andy profile for the last 30 days):
   ```
   just run /path/to/your/repo
   ```

3. Run Imposter with custom settings:
   ```
   just run /path/to/your/repo 2023-01-01 2023-12-31 night-owl
   ```

4. Clean up project files:
   ```
   just clean
   ```

5. Build the project:
   ```
   just build
   ```

6. Update dependencies:
   ```
   just update
   ```

## Customizing Profiles

You can customize existing profiles or create new ones by modifying the `profiles.py` file. Each profile defines parameters such as minimum and maximum daily commits, work days, work hours, and the probability of committing on a given day.

## Disclaimer

This tool is created for educational and testing purposes only. Do not use it to misrepresent your actual work or contributions.
