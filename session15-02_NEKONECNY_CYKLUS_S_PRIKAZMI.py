while True:
    try:
        print('VOLACO')
    except KeyboardInterrupt:
        cmd = input('ZADAJ PRIKAZ PROGRAMU :')
        if cmd == 'q':
            quit()
    finally:
        pass