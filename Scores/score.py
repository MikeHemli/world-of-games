def add_score(difficulty: int):
    try:
        f = open('scores.txt', 'r')
        number = int(f.read())
        new_score = (difficulty * 3) + 5
    except ValueError:
        print('The data stores in Scores.txt is not an instance of int, creating new counter..')
        new_score = (difficulty * 3) + 5
    except FileNotFoundError:
        print('The file does not exist... creating a new file...')
        new_score = (difficulty * 3) + 5
    # except NameError:
    #     print("There is a name error...")
    finally:
        f = open('scores.txt', 'w')
        f.write(str(new_score))
        f.close
