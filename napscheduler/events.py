__all__ = ('EVENT_SCHEDULER_START', 'EVENT_SCHEDULER_SHUTDOWN',
           'EVENT_SCHEDULER_JOB_ADDED', 'EVENT_SCHEDULER_JOB_REMOVED',
           'EVENT_JOB_EXECUTED', 'EVENT_JOB_ERROR', 'EVENT_JOB_MISSED',
           'EVENT_ALL', 'SchedulerEvent', 'JobEvent')


EVENT_SCHEDULER_START = 1        # The scheduler was started
EVENT_SCHEDULER_SHUTDOWN = 2     # The scheduler was shut down
EVENT_SCHEDULER_JOB_ADDED = 4    # A job was added to a job store
EVENT_SCHEDULER_JOB_REMOVED = 8  # A job was removed from a job store
EVENT_JOB_EXECUTED = 16          # A job was executed successfully
EVENT_JOB_ERROR = 32             # A job raised an exception during execution
EVENT_JOB_MISSED = 64            # A job's execution was missed
EVENT_ALL = (EVENT_SCHEDULER_START | EVENT_SCHEDULER_SHUTDOWN |
             EVENT_SCHEDULER_JOB_ADDED | EVENT_SCHEDULER_JOB_REMOVED |
             EVENT_JOB_EXECUTED | EVENT_JOB_ERROR | EVENT_JOB_MISSED)


class SchedulerEvent(object):
    """
    An event that concerns the scheduler itself.

    :var code: the type code of this event
    """
    def __init__(self, code, job=None):
        self.code = code
        self.job = job

class JobEvent(SchedulerEvent):
    """
    An event that concerns the execution of individual jobs.

    :var job: the job instance in question
    :var scheduled_run_time: the time when the job was scheduled to be run
    :var retval: the return value of the successfully executed job
    :var exception: the exception raised by the job
    :var traceback: the traceback object associated with the exception
    """
    def __init__(self, code, job, scheduled_run_time, retval=None,
                 exception=None, traceback=None):
        SchedulerEvent.__init__(self, code)
        self.job = job
        self.scheduled_run_time = scheduled_run_time
        self.retval = retval
        self.exception = exception
        self.traceback = traceback
