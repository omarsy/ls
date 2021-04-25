Feature: Ls

    @linux
    @windows
    Scenario: Lists all files of a specified folder
        When we create a file with the name another_file on the 18/09/19 01:55 and which has these permissions 777
        When we create a file with the name some_file on the 19/09/19 01:55 and which has these permissions 744
        Then executes this command python3 ls.py ./data returns this
            | Output       |
            | another_file |
            | some_file    |
    @linux
    @windows
    Scenario: Lists all files beginning with a given prefix
        When we create a file with the name another_file on the 18/09/19 01:55 and which has these permissions 744
        When we create a file with the name some_file on the 19/09/19 01:55 and which has these permissions 744
        When we create a file with the name prefixed_file on the 19/09/19 02:55 and which has these permissions 744
        Then executes this command python3 ls.py ./data/prefix returns this
            | Output        |
            | prefixed_file |
    @windows
    Scenario: ls has an option "-l" to display the mode and the creation date of the files
        When we create a file with the name another_file on the 18/09/19 01:55 and which has these permissions 666
        When we create a file with the name some_file on the 19/09/19 01:55 and which has these permissions 666
        Then executes this command python3 ls.py ./data -l returns this
            | Output                                  |
            | rw-rw-rw- 2019-09-18 01:55 another_file |
            | rw-rw-rw- 2019-09-19 01:55 some_file    |