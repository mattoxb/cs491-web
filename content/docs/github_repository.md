---
title: "Viewing Your Grades"
date: 2024-01-09T16:07:09-06:00
menutitle: "Your Grades"
weight: 5
draft: false
imageEffects.lightbox: false
---

Almost everything we assign will be on Prairielearn, and your grades will be visible there, but it's also nice to be able to
calculate your total score and see what letter grade corresponds to it.  We will use the [[github.com]] service to post your
grade breakdown.

If you've never used github before, don't worry; you don't need to know anything about it to get started.  Skip ahead to the
[procedure](#procedure) section and follow the instructions there.  If you are curious about the technical details, what is happening
is you will create a github account if you don't already have one, and associate your university netid with it.  Then we will
create a repository in a special github organization that is unique to you and only accessible by you and the course staff.
Every morning we will run a script that will populate the repository with the current snapshot of your grades.

## Procedure

Please note that **this is a multi-step process**!  If you do not follow **all** the steps then nothing will happen.

1. Access the [magic repository creator link](https://edu.cs.illinois.edu/create-gh-repo/sp24_cs491cap) to get started.
   You will see a web page with the following content:
   
   ![](images/log_in_to_github.png?lightbox=false)


2. Click on the "Log in to GitHub.com".  This will open a new page; follow the instructions.  If you already have a
   github account, log in as you normally would.  If you do not have a github account already, create one here.  It's
   worth creating a name you like, since you will almost certainly use github in future classes and in the professional
   world.

3. Once you are done, return to the original page and click "I've logged in!".  You will see a new page in respone:

   ![](images/join_org.png)
   
   This is an invitation to join the UIUC Coursework organization on github.  Click on "Join org: Illinos-cs-coursework".
   
4. This will take you to github again, with the following page:

   ![](images/single_sign_on.png)

   Click on "Continue".  You will be authenticated via UIUC's login systems, and probably have to interact with the dreaded Duo
   authentication app.
   
   Once that is done, you will probably see a page named something like `sp24_cs101_NETID`, where `NETID` is your actual netid.
   
   This is your repository for CS 101.  Bookmark the page so you can view your grades later.  **You will not see any grades right away.**
   This page is populated by a script that the staff runs twice a day.  Check again in about 12 hours and you should see something then.
   
