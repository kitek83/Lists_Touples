#This program uses writlines() method
#to write in the file list of text strings
def main():
    cities = ['Szczecin', 'New Yourk','Warsaw','Gdynia']
    cit_file = open('cities.txt','a')
    cit_file.writelines(cities)
    cit_file.close()
    #use for loop to save list elements in file
    cit_file = open('cities.txt', 'a')
    for city in cities:
        cit_file.write(city + '\n')
    cit_file.close()


main()