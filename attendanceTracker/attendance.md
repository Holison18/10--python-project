# Attendance Tracker

## Overview

This is an Attendance Tracker Python script that helps educational institutions track and manage student attendance for various subjects. It allows you to input the number of absentees for a specific subject, and it can send warning messages to students and staff based on attendance thresholds.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Required Python libraries: `openpyxl` for Excel file handling and `smtplib` for sending emails.

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/Holison18/10--python-project/tree/a93fb11c2eb0d2ded28b8b2800918dc6785c06d4/attendanceTracker
   ```

2. Change to the project directory:

   ```shell
   cd AttendanceTracker
   ```

3. Install the required Python libraries:

   ```shell
   pip install openpyxl
   ```

## Usage

To use the Attendance Tracker, follow these steps:

1. Run the script:

   ```shell
   python attendancTracker.py
   ```

2. Select the subject you want to track attendance for.

3. Input the number of absentees for that subject.

4. Input the roll numbers of the absent students when prompted.

5. The script will track attendance and send warning messages to students and staff as needed.

## Features

- Track attendance for multiple subjects.
- Send warning messages to students and staff based on attendance thresholds.
- Email notifications using SMTP (Gmail).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name:

   ```shell
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```shell
   git commit -m "Add your feature"
   ```

4. Push your changes to your forked repository:

   ```shell
   git push origin feature/your-feature-name
   ```

5. Open a Pull Request on the original repository.


