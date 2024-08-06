# SDET Coding Challenge

## Task intro
LoanPro has built a new, state of the art calculator that’s set to revolutionize the world of basic arithmetic operations. As part of the team that built it, your job is to build the right tools, tests, processes and procedures to guarantee correctness. Your software developer peers tell you that it appears to be working OK for all intended purposes; there’s even some unit tests providing coverage, so their confidence level is high. As a Software Developer Engineer in Testing you think it’s great there’s unit test coverage, but would like to perform other types of testing as well before releasing to the public.

* If you use automation tools or custom code, provide the source code and instructions on how to run those

## Running the tests


https://github.com/user-attachments/assets/819e4b9a-8f91-4877-a04b-82670779354d



There's two ways for running the tests:
### With Python 
Having python and docker installed in any OS, pull or download the repository.
From the root folder execute it with: 

`python -m pytest -r A -n auto tests/`


### With Docker
There's an available image of the repository with all the tests already there. This method might run into
some docker-in-docker issues but I was able to run it successfully on MacOS (silicon) but not on Linux (arm64).

`docker pull nalurralde/loanpro-challenge:latest` 

Execute it with:

`docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker nalurralde/loanpro-challenge:latest` (might take ~1 minute to start)

## Expected output
The execution should run the pytest tests (~210) and some of them should fail.

Failure is expected, as it's a real issue with the app.

*Last run resulted in 4 failed and 213 passed tests.* 
