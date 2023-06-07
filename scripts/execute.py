import extract
import transform
import load
# run create_tables.py first

if __name__ == '__main__':
    extract.main()
    print('')
    transform.main()
    print('')
    load.main()
