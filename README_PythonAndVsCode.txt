Setup Python environment within VsCode for notebook functionality (execute script blocks as ipynb files):
https://stackoverflow.com/questions/32671747/visual-studio-code-input-function-in-python


Tasks are intended for building your application. Since Python is interpreted, you don't need to use tasks.json at all to run/debug your Python code. Use the launch.json instead. I am using Don Jayamanne's Python extension for debugging and have configured the launch.json as follows:

1. Open the Command Palette (Ctrl + Shift + P) and write the command:
	`start without debugging`

2. Then select your Environment -> Click Python. This should create a launch.json file within a .vscode directory in the current directory.

3. Paste the following configuration json

{
"version": "0.2.0",
"configurations": [
    {
        "name": "Python",
        "type": "python",
        "request": "launch",
        "stopOnEntry": true,
        "pythonPath": "${config.python.pythonPath}",
        "program": "${file}",
        "debugOptions": [
            "WaitOnAbnormalExit",
            "WaitOnNormalExit",
            "RedirectOutput"
        ],
        "console": "integratedTerminal"
    }
]}

4. Save the file, open your python script in the editor and 'start without debugging' again. This should launch an integrated terminal where you can give input as well as see the output.

