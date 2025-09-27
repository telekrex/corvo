# Corvo
tiny [decentralized](https://en.wikipedia.org/wiki/Decentralization) project aggregator

<p align=center>
    <img src="docs/screenshot.png">
</p>

### Tiny? Decentralized?
- Runs locally, no login
- Projects live where they like
- Compatible with any storage solution
- Declaritively reproduced every run

### What is Corvo and what problem does it solve?
`.Corvo` is a format for documentation and issue tracking simultaneously in one file. Then `Corvo.exe` is an application that reads all the .corvo files it can find and gives you a GUI to visualize, with the goal of helping you make decisions and quickly navigate to relevant files.

*Why not just use Notion, Trello, GitHub Issues, Etc.?*
You could. You should. GitHub's CD/CI is awesome for collaboration. But if you're making software for fun, as an army of 1, this can be cumbersome.

Corvo is for local organization, for projects big and small, and can apply to non-software projects too. It is probably best for, but not limited to, hobbysts. If you prefer to interact with files on your hardware, read on!

### Decentralized management
Corvo doesn't change or interact directly with any of your files. It simply reads them where they are, and passes on the important details to the GUI. Say you have a device specifically for romance novels that you use Corvo to manage: when that device is unplugged, so are the projects. Plug it back in, and they're back. In this [decentralized](https://en.wikipedia.org/wiki/Decentralization) way, you can organize your projects with extreme flexibility.

### .Corvo format
Create a file named "yourprojectname.corvo". [Avoid using spaces](https://superuser.com/questions/29111/what-technical-reasons-exist-for-not-using-space-characters-in-file-names). This file contains the operations of your project. The first four lines of the file are Corvo's metadata:
```
Line 1: Title, spaces allowed here!
Line 2: Description, often for fun
Line 3: Status, what you're doing with this lately
Line 4: Tags, for filtering
```

After those lines, the rest of the file is free for you to arrange.

Lines that start with `/ ` (forward slash + space) are **actions** - these are tasks that are ready to execute. Lines that start with `. ` (period + space) are **thoughts** - these are anything that's not an action, but is still task-like. Such as a question that needs to be answered, an idea for a task that isn't fully developed, etc. The idea is that thoughts *become* tasks after some time in the oven.

Any other lines of text not starting with those is just treated as documentation, and since it doesn't matter where you put these lines, you can use them to extend some conversation around your thoughts and actions.

A Corvo file may look something like this:
```
My Awesome Project
An application that will help me do things
Currently exploring GUI frameworks
Software, Personal

/ Create a repository for sharing
/ Add .gitignore file
/ Settle on a name

. Name ideas: Kermit? Cool App? Ice Cream?
I think Kermit is a terrible name, but that's just an assumption.

. Need to figure out where to find GUI frameworks
```

### The GUI
Corvo.exe will search over the provided domains and spit out a quick view of any projects (.corvo files) it finds, thus a quick overview of all your projects, with the ability to filter them by tag. Corvo non-destructively adds tags "active" and "inactive" based on the number of actions it finds.

## Credits
Written by telekrex. I made this because I needed it. There are lots of tools out there with more features and better codebases. :)

## License
This project is released into the public domain. See the [LICENSE](LICENSE) file for details.