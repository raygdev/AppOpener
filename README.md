# AppOpener


## Usage
This small app is meant to serve a specific purpose for
my current job. Using Pyautogui to automate tasks for me
and for my co-workers! It will be run as an executionable
on other computers at work using pyinstaller and windows
powershell. The shell will open the required apps by running
the `Start-Process` command allowing for the applications, and
a browser instance to open. The python executionable will sleep
to wait for applications to complete loading. After loading is
complete, the system will prompt the user for 2 different usernames
and passwords. Those will be used to log them into their accounts.

The only things required for us will be to run the powershell script, provide the usernames and passwords,
and everything else will be done automatically.

## The Problem
Our jobs require that we use multiple applications that require us to
perform the same menial task of logging in to each one. This isn't so
bad when you only have to do this once per day. Unfortunately it's not
once a day for us. 

We have a problematic app that we rely on to be able to do our jobs.
We have to use this tool for diagnostic procedures, to read data, trouble
codes, and other relevant information to do the job. The problem is that the
app crashes multiple times a day (on-going for over a year now). This wouldn't
be so bad if the app would reopen regularly, but attempting to relaunch the
application prompts that an instance of it is still open... causing the launch to fail.
The instance can be found and shut down manually, but doing so will cause other issues with 
the application. The only option we have to get it to work right is to restart our computers MULTIPLE
TIMES A DAY. When we reboot, we have to click on this and click on that to get everything
open, wait, then input usernames and passwords in, ***over and over***, in multiple different windows.

This app is my solution (workaround) to that problem. This will allow us to input usernames
and passwords in one location without having to navigate and click around. It will free up some
of our time to be just a little more productive at work. Let machines do what they do, so that 
we can do what we do. I'm making this in hopes that it will
alleviate some headache and stress, not just for me, but for my co-workers as well!