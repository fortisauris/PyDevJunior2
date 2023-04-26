while True:
    try:
        print('VOLACO')
    except KeyboardInterrupt:  # Control C
        cmd = input('ZADAJ PRIKAZ PROGRAMU :')
        if cmd == 'q':
            quit()
    finally:
        pass