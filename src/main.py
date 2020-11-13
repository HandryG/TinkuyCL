from update_medoids import update_medoids
import sys,getopt
def main(argv):
    
    minutes = int(sys.argv[1])        
    update_medoids(minutes)

if __name__ == "__main__":
    main(sys.argv)
