**Python Read-Write Lock**

- HowTo:
    - Use:
        ```
        from RWLock import RWLock

        rwlock = RWLock()

        with rwlock.r_locked:
            # read info
        with rwlock.w_locked:
            # write info
        ```
    - Install:
        Just add repo link to requirements.txt file with *git+* ahead.
        For example: `git+https://git.pancir.it/egor.bakharev/ParsePy.git`

- Useful links:
    - https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock
    - https://gist.github.com/tylerneylon/a7ff6017b7a1f9a506cf75aa23eacfd6