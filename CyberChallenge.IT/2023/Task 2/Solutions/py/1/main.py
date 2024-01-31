from collections import namedtuple


def main():
    # m = num of players
    # n = total tasks (flags)
    # s = total submissions
    # Time Complexity:  O(n + max(m, s))
    # Space Complexity: O(n + max(m, s))

    m, n, s = map(int, input().split())

    # task_is as key in the hashtable 'tasks'
    tasks = {}
    Task = namedtuple("Task", ["id", "flag", "points"])

    while n:
        task = input().split()
        task = Task(int(task[0]), task[1], int(task[2]))
        tasks[task.id] = task
        n -= 1

    Submission = namedtuple(
        "Submission", ["player_id", "task_id", "flag_submitted", "timestamp"]
    )

    # user_id as key in the hashtable 'users'
    users = {}

    while s:
        submission = input().split()
        submission = Submission(
            int(submission[0]), int(submission[1]), submission[2], int(submission[3])
        )
        # skip invalid and wrong flags
        if (
            not submission.task_id in tasks
            or submission.flag_submitted != tasks[submission.task_id].flag
        ):
            s -= 1
            continue
        # skip if user already submitted a valid flag for this task
        if submission.player_id in users:
            if not submission.flag_submitted in users[submission.player_id]:
                users[submission.player_id][
                    submission.flag_submitted
                ] = submission.timestamp
                # update total score
                users[submission.player_id]["score"] += tasks[submission.task_id].points

            # update timestamp if user submitted a flag for this task before, we care only about the first valid submission
            elif (
                users[submission.player_id][submission.flag_submitted]
                > submission.timestamp
            ):
                users[submission.player_id][
                    submission.flag_submitted
                ] = submission.timestamp
        else:
            # first time user submits a flag
            users[submission.player_id] = {
                submission.flag_submitted: submission.timestamp,
                "score": tasks[submission.task_id].points,
            }

        s -= 1

    scoreboard = []

    # create a list of tuples (player_id, score, timestamp)
    for user_id in range(1, m + 1):
        if user_id not in users:
            scoreboard.append((user_id, 0, 0))
        else:
            # get last valid submission timestamp
            max_timestamp = -1
            for submission in users[user_id]:
                if submission != "score":
                    max_timestamp = max(max_timestamp, users[user_id][submission])

            scoreboard.append((user_id, users[user_id]["score"], max_timestamp))

    # sort by score (desc), timestamp (asc) and player_id (asc)
    scoreboard.sort(key=lambda winner: (-winner[1], winner[2], winner[0]))

    for user_id in scoreboard:
        print(user_id[0], user_id[1])


if __name__ == "__main__":
    main()
