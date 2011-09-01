Not (so) Advanced Python Scheduler (NAPScheduler) is a fork from APScheduler
<http://bitbucket.org/agronholm/apscheduler/>. Its main intention is to serve
to my own purposes on a project I am working on.

I removed a lot a things I don't use and added some features I needed. Also removed
docs, examples, and maybe more, intentionally or not.

This is not aimed at competing with APScheduler, but if there are interest from others,
I may work on improving it on a different direction. Though I think APScheduler is
sufficient for most use cases.

Features
========

* No (hard) external dependencies
* Thread-safe API
* Excellent test coverage (tested on CPython 2.4 - 2.7, 3.1 - 3.2, Jython 2.5.2, PyPy 1.4.1 and 1.5)
* Configurable scheduling mechanisms (triggers):

  * Cron-like scheduling
  * Delayed scheduling of single run jobs (like the UNIX "at" command)
  * Interval-based (run a job at specified time intervals)


Documentation
=============

NAPScheduler has no specific documentation.


Source
======

The source for NAPScheduler can be browsed at `Github
<http://github.com/ecdpalma/napscheduler/>`_.

 
Reporting bugs and help
=======================

Please, use GitHub bug tracker.

