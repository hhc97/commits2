import os


def commit(commit_no: int) -> None:
    os.system('git add --all')
    os.system(f"git commit -m {commit_no}")


if __name__ == '__main__':
    for i in range(2, 5000001):
        with open('commits.txt', 'w') as f:
            f.write(f'{i}')
        commit(i)
        if i % 1000 == 0:
            os.system('git push')
    os.system('git push')
