# Exam

This exam is split into two parts:
- [Part 1: _Analyzing Mario Kart 8 World Records_](mario_kart_wr.md)
- [Part 2: _Solving an optimization problem with path-finding algorithms_](robots.md)

There are tests for all the questions that require precise answers. For these, you'll have to make
sure running the `pytest` command works.

> :bulb: **Note**
>
> in order to filter the tests for each part, you can run the following commands
> - for the first part
> ```shell
> pytest --verbose --tb no -k mario
> ```
> - for the second part
> ```shell
> pytest --verbose --tb no -k robots
> ```

Some other questions require you to plot results in figures. For these, you'll have to make sure
running the appropriate `python ...` command works and shows the results you want to show.

It is encouraged to not spend more than _45 minutes_ on each section. However, you are free to
fill them in any order you like and you can stop at any point in the middle of a section to go to
the next one.

If you do so, be careful not to leave invalid _Python_ code behind you.

> :warning: **Warning**
>
> some more rules to pay attention to
> - you are only allowed to use Matplotlib as an external module
> - you are not allowed to write _library_ code in other files, only write your code in provided
>   files

## Preparing your environment on the ISAE's computers

**The exam must be done on Linux, not on Windows**

Run the following steps:
- open a _Terminal_ on the computer (you can press the _Windows_ key and then type `Terminal`)
- clone this repository using the following command:
```bash
git clone https://gitlab.isae-supaero.fr/mae-ac/exam
```
- Load the _Anaconda_ module using the following command:
```bash
module load anaconda3/2024
```
- Activate the _Python_ environment using the following command:
```bash
source activate mae1-env
```
- Go inside the exam directory:
```bash
cd exam
```
- Run your editor or you IDE. For VSCode, run:
```bash
code .
```
- Now, in order to run your scripts or your tests, you need to open a `Terminal` in VSCode. You can
  do that by clicking on `Terminal` in the top menu and then `New
  Terminal`.
- To run a script, you can use the following command in the `VS CODE Terminal`:
```bash
python src/mario_kart_wr.py
# or
python src/robots.py
```
- To run the tests, you can use the following command in the `VS CODE Terminal`:
```bash
pytest --verbose --tb no -k mario
# or
pytest --verbose --tb no -k robots
```

Once it's done, you can start working on the exam.
Choose the part you want to start with and follow the instructions:
- [Part 1: _Analyzing Mario Kart 8 World Records_](mario_kart_wr.md)
- [Part 2: _Solving an optimization problem with path-finding algorithms_](robots.md)

## Upload your work to the LMS 
- open a terminal
- go into the folder containing your project
- use the `zip` command to compress your project
```shell
zip -r project.zip . -x "venv/**" ".git/**"
```
- upload the ZIP archive to the [LMS](https://lms.isae.fr/mod/assign/view.php?id=118693&action=editsubmission)

---
