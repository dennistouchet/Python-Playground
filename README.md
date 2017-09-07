# Python-Playground

A place for me to put any scripts I write in Python.

	Folders Descriptions
* practice
* Environments
* \*

## Windows 10 - Py3 setup

### setup powershell user

		Set-ExecutionPolicy -Scope CurrentUser
		> Remote Signed

		Get-ExecutionPolicy -List

### install chocolatey

		iwr https:/chocolatey.org/install.ps1 -UserBasicParsing | iex

		choco upgrade chocolatey


### install nano

		choco install -y nano

### install python3

		choco install -y python3

		python -m pip install --upgrade pip

### setup venv

		> cd to desired Folder

		mkdir Environments
		cd Environments

		python -m venv my_env

		> to run in that environment

		my_env\Scriots\activate

		> to exit environment

		deactivate

### basic program

		nano hello.py

		> print("Hello, World!!!");

		ctrl + x ->	y -> Enter

		python hello.py

		>> Hello World!!!
