
# Lesson 9 Notes: Debugging

These are some notes for [Software Carpentry](https://software-carpentry.org/)'s tutorial [*Programming with Python*](http://swcarpentry.github.io/python-novice-inflammation/).  The web page for this lesson can be found [here](http://swcarpentry.github.io/python-novice-inflammation/09-debugging/).

## The Goal

> Debug **systematically**

## Know What It's Supposed to Do

You need to know when it *should* fail.  Try to figure out a scenario where

> given **these conditions** it should produce **that result**.

**The problem:** you often write scientific software *because* you **don't know what's going to happen**.

But you should be able to home in on some **extreme cases** where logic or a paper and pencil calculation should tell you what will happen.

### Checklist: Rules of Thumb

Try the following...

1. **Test with simplified data.**
    * Try something where you could calculate the answer by hand.

2. **Test a simplified case.**
    * This is the **assume a spherical elephant** case.

3. **Compare to an oracle.**
    * Match results to a trusted source, like
        * experimental data
        * an earlier program
        * etc.

4. **Check conservation laws.**
    * Make sure that **invariants stay invariant**, like
        * the total amount of mass
        * the total momentum
        * the total number of items, e.g. hospital patients, in the records
        * etc.

5. **Visualize.**
    * Great to see if there are obvious errors, but hard to compare two visualizations in general.

## Make It Fail Every Time

Find a **test case** that **guarantees failure**.

It's hard to debug an **intermittent failure**, since

* it takes time to repeat the failure, and
* you're likely to scroll past it.

This is also good for checking your code is **"plugged in"**, i.e. that you're calling the function you think you are, that you're testing the right version, etc.

## Make It Fail Fast

The faster the program fails,

* the less time you waste **finding the error**, and
* the less time you have to **lose focus**.

Shorten the **gaps between failures**: make sure there are **few lines of code** that could lead to failure.

## Change One Thing at a Time, For a Reason

Use changes to

* **gather information**
    * e.g. "does the bug remain if we change the order of loops?", or
* **test a fix**
    * e.g. "does the bug go away if we sort the input data?"

Make **one change at a time**, then **retest immediately**.  Run **all the tests**, to make sure your fix doesn't introduce a different bug.

## Keep Track of What You've Done

You're trying to make **systematic improvement**.  You need to know the **steps that got you to where you are**.

This especially helps when **asking for assistance.** You can be specific about what you've tried already.

**Pro-Tip: version control.** This helps you reset to a previous state if needed.

## Be Humble: Ask for Help

Asking for help can be useful because...

* **explaining your thoughts** to someone else can help spot inconsistencies
* you can avoid **confirmation bias**, since you *want* your program to work, but someone else isn't as invested

Take time to **learn from mistakes**:

* deepen your **knowledge of libraries**
* iron out **kinks in your model**

Training yourself to avoid certain mistakes will **save time in the long run.**


```python

```
